<script setup>
import { ref, onMounted } from 'vue';

const emit = defineEmits(['error', 'offline', 'online', 'reboot']);

const currentId = ref(1);
const terminalLines = ref([
    {id: 0, text: "Welcome to the terminal !!!", input: false},
    {id: 1, text: "Loading packages : [>\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0]", input: false},
]);

const inputText = ref("");
const terminalActive = ref(false)
const myInput = useTemplateRef('my-input');

const eventuallySendMessage = (command) => {
    if (command.startsWith("error ")) {
        emit('error', command.replaceAll("error ", ""));
        return true;
    } else if (command.startsWith("offline ")) {
        emit("offline", command.replaceAll("offline ", ""));
        return true;
    } else if (command.startsWith("online")) {
        emit("online", command.replaceAll("online ", ""));
        return true;
    } else if (command.startsWith("reboot")) {
        emit("reboot", command.replaceAll("reboot", ""));
        return true;
    }
    return false;
}

const submitCommand = () => {
    const command = myInput.value.innerText.replaceAll("\n", "").replaceAll("\r", "");
    const recognizedCommand = eventuallySendMessage(command);
    myInput.value.innerText = "";
    if (command !== "") {
        terminalLines.value.push({id: currentId.value, text: '> ' + command, input: true});
        currentId.value++;
        if (recognizedCommand) {
            terminalLines.value.push({id: currentId.value, text: 'Command sent successfully', input: false});
        } else {
            terminalLines.value.push({id: currentId.value, text: 'Menfou + Palu', input: false});
        }
        currentId.value++;
    } else {
        terminalLines.value.push({id: currentId.value, text: "> ", input: true});
        currentId.value++;
    }
}

onMounted(() => {
    for (let i = 0; i < 15; i++) {
        setTimeout(() => {
            terminalLines.value.push({id: currentId.value, text: "Loading packages : [" + "-".repeat(i+1) + ">" + "\xa0".repeat(15-i-1) + "]", input: true});
            currentId.value++;
        }, 100 * (i+1));
    }
    setTimeout(() => {
        terminalLines.value.push({id: currentId.value, text: "Packages loaded successfully !", input: true});
        currentId.value++;
        terminalLines.value.push({id: currentId.value, text: "Waiting for instructions...", input: true});
        currentId.value++;
        terminalActive.value = true
    }, 1600)
    myInput.value.focus();
    myInput.value.addEventListener('blur', (e) => {
        setTimeout(() => {
            myInput.value.focus();
            myInput.value.selectionStart = 100000;
            myInput.value.selectionEnd = 100000;
        }, 0);
    });
})

</script>

<template>
    <div class="terminal">
        <div class="linesContainer">
            <div v-for="line in terminalLines" :class="{typein: !line.input}" :key="line.id">
                <span>{{ line.text }}</span>
            </div>
            <div :class="{editionLineHidden: !terminalActive}">
                <div v-on:blur="myInput.focus" ref="my-input" class="terminalInput" contenteditable="true" spellcheck="false" @keyup.enter.stop.prevent="submitCommand"></div>
                <button class="caret">&nbsp;</button>
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
    padding: 10px;
    font-family: monospace;
    font-size: 16px;
}

.linesContainer {
    position: absolute;
    bottom: 0;
}

.typein {
  background: linear-gradient(#39FF14 0 0) no-repeat;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
  background-size: 0% 100%;
  animation: typein 1s both;
}

.editionLineHidden {
    height: 0;
}

.terminalInput {
    display: inline;
    caret-color: transparent;
    word-break: break-all;
}

.terminalInput::before {
    content: "\00a0>\00a0";
}

.terminalInput:focus-visible {
    outline: none;
}

.caret {
  border: 0;
  padding: 0;
  outline: none;
  font-family: monospace;
  animation: caretBlink 1s infinite steps(1, jump-both);
}

@keyframes caretBlink {
  0% {
    background-color: black;
  }
  50% {
    background-color: black;
  }
  51% {
    background-color: #39FF14;
  }
  100% {
    background-color: #39FF14;
  }
}

@keyframes typein{
  to {background-size: 100% 100%} /* we animate to 100% 100%*/
}
</style>