<script setup>
const { bus } = defineProps(['bus']);

const maxBusId = bus.map((message) => message.id).reduce((a, b) => Math.max(a, b), -1);
const lastMessageId = ref(maxBusId);

const multipleBarsValues = ref([4, 5, 7, 6, 8, 2, 5, 3, 6, 7]);
const currentMultipleBarsTimerId = ref(0);
const bigBarsValues = ref([10]);
const currentBigBarsTimerId = ref(0);
const circularGraphsValues = ref([52]);
const currentCircularGraphsTimerId = ref(0);

const distributeInteger = (total, parts) => {
  const result = [];
  for (let i = 0; i < parts; i++) {
    result.push(0);
  }
  if (total > 0) {
    for (let i = 0; i < total; i++) {
      result[i % parts]++;
    }
    return result;
  }
  else if (total === 0) {
    return result;
  }
  else {
    for (let i = 0; i > total; i--) {
      result[Math.abs(i) % parts]--;
    }
    return result;
  }
}

const getNextDelay = () => {
  return Math.floor(Math.random() * 4500) + 500;
}

const getNextDelayForCircularGraph = () => {
  return Math.floor(Math.random() * 3000) + 2000;
}

const getNewValue = (valuesArray, numberOfBars, maxValue, minValue, maxPower) => {
  const index = Math.floor(Math.random() * numberOfBars);
  const currentValue = valuesArray.value[index];
  const power = Math.floor(Math.random() * maxPower) + 1;
  let newValue;
  if (currentValue === maxValue) {
    newValue = maxValue - power;
  } else if (currentValue === minValue) {
    newValue = minValue + power;
  } else {
    newValue = Math.random() > 0.5 ? currentValue + power : currentValue - power;
    newValue = Math.min(Math.max(minValue, newValue), maxValue);
  }

  return [index, newValue];
}

const updateValues = (valuesArray, numberOfBars, maxValue, minValue, maxPower) => {
  const indexAndNewValue = getNewValue(valuesArray, numberOfBars, maxValue, minValue, maxPower);
  valuesArray.value[indexAndNewValue[0]] = indexAndNewValue[1];
}

const resetValue = (valuesArray, index, minValue, maxValue) => {
  const newValue = Math.floor(Math.random() * (maxValue - minValue + 1)) + minValue;
  valuesArray.value[index] = newValue;
}

const refreshMultipleBarsTimeout = (delay) => {
    currentMultipleBarsTimerId.value = setTimeout(() => {
    updateValues(multipleBarsValues, 10, 10, 1, 2);
    refreshMultipleBarsTimeout(getNextDelay());
  }, delay);
}

const refreshBigBarsTimeout = (delay) => {
    currentBigBarsTimerId.value = setTimeout(() => {
    updateValues(bigBarsValues, 1, 15, 1, 2);
    refreshBigBarsTimeout(getNextDelay());
  }, delay);
}

const refreshCircularGraphsTimeout = (delay) => {
  currentCircularGraphsTimerId.value = setTimeout(() => {
    const newValue = getNewValue(circularGraphsValues, 1, 85, 15, 15);
    refreshCircularGraphsTimeoutWithSteps(newValue[0], newValue[1], 5);
    refreshCircularGraphsTimeout(getNextDelayForCircularGraph());
  }, delay);
}

const refreshCircularGraphsTimeoutWithSteps = (index, newValue, stepsNumber) => {
  const steps = distributeInteger(newValue - circularGraphsValues.value[index], stepsNumber);
  for (let i = 0; i < stepsNumber; i++) {
    setTimeout(() => {
      circularGraphsValues.value[index] = circularGraphsValues.value[index] + steps[i];
    }, i * 250);
  }
}

const multipleBarsMean = computed(() => {
  return (100 * multipleBarsValues.value.reduce((acc, value) => acc + value, 0)) / (multipleBarsValues.value.length * 10);
})

const firstTemperature = computed(() => {
  return (Math.round(multipleBarsMean.value * 60 / 100) + 60);
})

const secondTemperature = computed(() => {
  return (Math.round(circularGraphsValues.value[0] * 56 / 100) + 30);
})

onMounted(() => {
    refreshMultipleBarsTimeout(getNextDelay());
    refreshBigBarsTimeout(getNextDelay());
    refreshCircularGraphsTimeout(getNextDelayForCircularGraph());
})

onUnmounted(() => {
    clearTimeout(currentMultipleBarsTimerId.value);
    clearTimeout(currentBigBarsTimerId.value);
    clearTimeout(currentCircularGraphsTimerId.value);
})

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
      clearTimeout(currentMultipleBarsTimerId.value);
      for (let i = 0; i < multipleBarsValues.value.length; i++) {
        multipleBarsValues.value[i] = 10;
        setTimeout(() => {
          resetValue(multipleBarsValues, i, 3, 7);
        }, 2500 + Math.random() * 3500);
      }
      refreshMultipleBarsTimeout(getNextDelay() + 6000);

      clearTimeout(currentBigBarsTimerId.value);
      for (let i = 0; i < bigBarsValues.value.length; i++) {
        bigBarsValues.value[i] = 15;
        setTimeout(() => {
          resetValue(bigBarsValues, i, 6, 10);
        }, 2500 + Math.random() * 3500);
      }
      refreshBigBarsTimeout(getNextDelay() + 6000);

      clearTimeout(currentCircularGraphsTimerId.value);
      for (let i = 0; i < circularGraphsValues.value.length; i++) {
        circularGraphsValues.value[i] = 5;
        setTimeout(() => {
          const randomNewValue = Math.floor(Math.random() * (60 - 25 + 1)) + 25;
          refreshCircularGraphsTimeoutWithSteps(i, randomNewValue, 5);
        }, 2500 + Math.random() * 3500);
      }
      refreshCircularGraphsTimeout(getNextDelayForCircularGraph() + 6000);
      break;
    default:
      break;
  }
  lastMessageId.value = currentMessage.id;
})

</script>

<template>
    <div class="terminal">
        <div class="circularGraphs">
            <CircularGraph :value="multipleBarsMean" title="Processors" />
            <CircularGraph :value="circularGraphsValues[0]" title="GPU" />
        </div>
        <div class="horizontalBars">
          <SingleBarHorizontal :value="bigBarsValues[0]" title="RAM usage"/>
          <SingleBarHorizontal value="13" title="Disk storage"/>
        </div>
        <div class="multipleBars">
            <SingleBarVertical :value="multipleBarsValues[0]" title="CPU 1"/>
            <SingleBarVertical :value="multipleBarsValues[1]" title="CPU 2"/>
            <SingleBarVertical :value="multipleBarsValues[2]" title="CPU 3"/>
            <SingleBarVertical :value="multipleBarsValues[3]" title="CPU 4"/>
            <SingleBarVertical :value="multipleBarsValues[4]" title="CPU 5"/>
            <SingleBarVertical :value="multipleBarsValues[5]" title="CPU 6"/>
            <SingleBarVertical :value="multipleBarsValues[6]" title="CPU 7"/>
            <SingleBarVertical :value="multipleBarsValues[7]" title="CPU 8"/>
            <SingleBarVertical :value="multipleBarsValues[8]" title="CPU 9"/>
            <SingleBarVertical :value="multipleBarsValues[9]" title="CPU 10"/>
        </div>
        <div class="textInfo">
            <div>Processors temperature: {{ firstTemperature }}°</div>
            <div>GPU temperature: {{ secondTemperature }}°</div>
            <div>RAM: 128 Go</div>
            <div>GPU Clock: 1065 MHz</div>
            <div>VRAM Clock: 7000 MHz</div>
            <div>LAN: 21.9 MB/s</div>
        </div>
    </div>
</template>

<style scoped>
.terminal {
  background-color: black;
  border: 1px solid white;
  padding: 15px;
  min-height: calc(100vh - 20px);
  max-height: calc(100vh - 20px);
  max-width: calc(100vw - 20px);
  font-family: monospace;
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr;
  gap: 10px;
}
@media (min-width: 921px) {
    .terminal {
        min-height: unset;
        max-height: calc(50vh - 30px);
        max-width: unset;
        grid-template-columns: 2fr 1fr;
        grid-template-rows: 1fr 1fr;
    }
}

.circularGraphs {
    display: flex;
    gap: 15px;
    justify-content: space-around;
    align-items: center;
    color: white;
}

.horizontalBars {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}
@media (max-width: 920px) {
    .horizontalBars {
      align-items: flex-start;
      padding-left: 10px;
    }
}

.multipleBars {
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: space-around;
    align-items: end;
}

.textInfo {
    display: flex;
    flex-direction: column;
    gap: 5px;
    padding: 15px 10px;
    justify-content: center;
}
@media (max-width: 920px) {
    .textInfo {
        grid-row: 2 / 3;
    }
}
</style>