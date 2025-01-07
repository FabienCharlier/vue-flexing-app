<script setup>
import { ref } from 'vue';
import logs from '../utils/logs.json';
import machines from '../utils/machines.json';

const { bus } = defineProps(['bus']);

const currentId = ref(0);
const terminalLines = ref([]);
const currentTimerId = ref(0);

const maxBusId = bus.map((message) => message.id).reduce((a, b) => Math.max(a, b), -1);
const lastMessageId = ref(maxBusId);

const addLine = (text, withTimeStamp = true) => {
  if (terminalLines.value.length > 150) {
    terminalLines.value = terminalLines.value.slice(75, 151);
    return true;
  }
  const prefix = withTimeStamp ? (getCurrentDateAsLogString() + " ") : "\xa0"
  terminalLines.value.push({ text: prefix + text, id: currentId.value });
  currentId.value++;
  return false
}

const getNextDelay = () => {
  return Math.floor(Math.random() * 5500) + 500;
}

const refreshTimeout = (delay) => {
  currentTimerId.value = setTimeout(() => {
    const newLineIndex = Math.floor(Math.random() * 1000)
    const hasRefreshed = addLine(logs[newLineIndex].text);
    const nextDelay = hasRefreshed ? 0 : getNextDelay();
    refreshTimeout(nextDelay);
  }, delay);
}

const writeLineAfterDelay = (line, delay, withTimeStamp = true) => {
  setTimeout(() => {
    addLine(line, withTimeStamp);
  }, delay)
}

const isValidMachine = (machineName) => {
  return machines.some((machine) => machine.name.toLowerCase() === machineName.toLowerCase())
}

const getCurrentDateAsLogString = () => {
  const d = new Date();
  return "[" + ("0" + d.getDate()).slice(-2) + "-" + ("0"+(d.getMonth()+1)).slice(-2) + "-" + d.getFullYear() + " " + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2) + ":" + ("0" + d.getSeconds()).slice(-2) + "]";
}

watchEffect(() => {
  if (bus.length === 0) {
    return;
  }
  
  const currentMessage = bus[bus.length - 1];
  if (lastMessageId.value >= currentMessage.id) {
    return;
  }
  switch (currentMessage.type) {
    case "reboot":
      clearTimeout(currentTimerId.value);
      writeLineAfterDelay("", 500, false);
      writeLineAfterDelay("", 500, false);
      writeLineAfterDelay("CRITICAL: Rebooting", 1000);
      writeLineAfterDelay("CRITICAL: Rebooting.", 2000);
      writeLineAfterDelay("CRITICAL: Rebooting..", 3000);
      writeLineAfterDelay("CRITICAL: Rebooting...", 4000);
      writeLineAfterDelay("CRITICAL: Reboot completed", 5000);
      writeLineAfterDelay("", 5000, false);
      writeLineAfterDelay("", 5000, false);
      refreshTimeout(getNextDelay() + 5000);
      break;
    case "error":
      if (!isValidMachine(currentMessage.command)) {
        break;
      }
      clearTimeout(currentTimerId.value);
      writeLineAfterDelay("ERROR: " + currentMessage.command + " has experienced an unexpected error !", 1000);
      refreshTimeout(getNextDelay() + 1000)
      break;
    case "offline":
      if (!isValidMachine(currentMessage.command)) {
        break;
      }
      clearTimeout(currentTimerId.value);
      writeLineAfterDelay("WARNING: " + currentMessage.command + " just lost connection and is now offline !", 1000);
      refreshTimeout(getNextDelay() + 1000)
      break;
    case "online":
      if (!isValidMachine(currentMessage.command)) {
        break;
      }
      clearTimeout(currentTimerId.value);
      writeLineAfterDelay("INFO: " + currentMessage.command + " is now online and fully operational !", 1000);
      refreshTimeout(getNextDelay() + 1000)
      break;
    default:
      break;
  }
  lastMessageId.value = currentMessage.id;
})

onMounted(() => {
  refreshTimeout(getNextDelay());
})

onUnmounted(() => {
  clearTimeout(currentTimerId.value);
})
</script>

<template>
  <div class="terminal">
    <div class="linesContainer">
      <div v-for="line in terminalLines" class="terminalLine" :class="{lastTerminalLine: line.id === currentId - 1}" :key="line.id">
        <span class="typein">{{ line.text }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.terminal {
  background-color: black;
  color: #39FF14;
  border: 1px solid white;
  max-height: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
  font-family: monospace;
}

.linesContainer {
  position: absolute;
  bottom: 0;
}

.terminalLine {
  animation: typein 0.5s linear forwards;
}

.lastTerminalLine::after {
  opacity: 0;
  right: 0;
  bottom: 0.25em;
  content:"a";
  width: 1em;
  height: 1.5em;
  background:#39FF14;
  animation: caretBlink 0.8s 0.5s infinite;
}

.typein {
  background: linear-gradient(#39FF14 0 0) no-repeat;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
  background-size: 0% 100%;
  animation: typein 1s both;
}

@keyframes caretBlink {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 0;
  }
  51% {
    opacity: 1;
  }
  100% {
    opacity: 1;
  }
}

@keyframes typein{
  to {background-size: 100% 100%} /* we animate to 100% 100%*/
}
</style>