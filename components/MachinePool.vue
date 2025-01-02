<script setup>
import { ref, watch } from 'vue';
import MachineState from './MachineState.vue';
import machines from '../utils/machines.json';

const { bus } = defineProps(['bus']);

const allMachines = ref(machines);
const currentTimerId = ref(0);
const lastMessageId = ref(-1);

const selectMachineIndex = () => {
    const erroredMachineIndexes = [];
    const offlineMachineIndexes = [];
    const onlineMachineIndexes = [];
    allMachines.value.forEach((machine, index) => {
        if (machine.state === 3) {
            erroredMachineIndexes.push(index);
        } else if (machine.state === 2) {
            offlineMachineIndexes.push(index);
        } else {
            onlineMachineIndexes.push(index);
        }
    });

    if (erroredMachineIndexes.length > 5) {
        return erroredMachineIndexes[Math.floor(Math.random() * erroredMachineIndexes.length)];
    } else if (offlineMachineIndexes.length > 12) {
        return offlineMachineIndexes[Math.floor(Math.random() * offlineMachineIndexes.length)];
    } else {
        return Math.floor(Math.random() * allMachines.value.length);
    }
}

const findNewState = (oldState) => {
    let newState = Math.floor(Math.random() * 3) + 1
    while (newState === oldState) {
        newState = Math.floor(Math.random() * 3) + 1
    }

    return newState;
}

const getNextDelay = () => {
  return Math.floor(Math.random() * 2500) + 1500;
}

const refreshTimeout = (delay) => {
  currentTimerId.value = setTimeout(() => {
    const selectedIndex = selectMachineIndex();
    const selectedMachine = allMachines.value[selectedIndex];
    const newState = findNewState(selectedMachine.state);
    allMachines.value[selectedIndex].state = newState;
    refreshTimeout(getNextDelay());
  }, delay);
}

const createOnlineTimeout = (machineIndex) => {
    const delay = Math.floor(Math.random() * 7000) + 3000;
    const expectedState = Math.random() <= 0.97 ? 1 : 3;
    setTimeout(() => {
        allMachines.value[machineIndex].state = expectedState;
    }, delay);
}

watchEffect(() => {
    if (bus.length === 0) {
        return;
    }

    const currentMessage = bus[bus.length - 1];
    if (lastMessageId.value >= currentMessage.id) {
        return;
    }
    
    let machineToUpdate;
    switch (currentMessage.type) {
        case "reboot":
            clearTimeout(currentTimerId.value);
            allMachines.value.forEach((machine, machineIndex) => {
                machine.state = 2;
                createOnlineTimeout(machineIndex);
            });
            refreshTimeout(getNextDelay() + 10000)
            break;
        case "online":
            machineToUpdate = allMachines.value.find((machine) => machine.name.toLowerCase() === currentMessage.command.toLowerCase())
            if (undefined === machineToUpdate) {
                break;
            }
            machineToUpdate.state = 1;
            break;
        case "offline":
            machineToUpdate = allMachines.value.find((machine) => machine.name.toLowerCase() === currentMessage.command.toLowerCase())
            if (undefined === machineToUpdate) {
                break;
            }
            machineToUpdate.state = 2;
            break;
        case "error":
            machineToUpdate = allMachines.value.find((machine) => machine.name.toLowerCase() === currentMessage.command.toLowerCase())
            if (undefined === machineToUpdate) {
                break;
            }
            machineToUpdate.state = 3;
            break;
        default:
            break;
    }
    lastMessageId.value = currentMessage.id;
})

onMounted(() => {
  refreshTimeout(getNextDelay());
})
</script>

<template>
    <div class="machine-pool">
        <div class="criticalMachines">
            <div class="criticalMachineLine" v-for="machine in allMachines.filter((machine) => {return machine.critical})" :key="machine.name">
                <span>{{  machine.name }}</span>
                <div class="machineLogo">
                    <img :src="'_nuxt/public/' + machine.image + '.svg'" width="40" height="40"/>
                    <img class="stateLogo" v-if="machine.state === 1" src="public/success.svg" width="20" height="20"/>
                    <img class="stateLogo" v-if="machine.state === 2" src="public/warning.svg" width="20" height="20"/>
                    <img class="stateLogo" v-if="machine.state === 3" src="public/error.svg" width="20" height="20"/>
                </div>
                <MachineState :state="machine.state" />
            </div>
        </div>
        <div class="allMachines">
            <div class="allMachineLine" v-for="machine in allMachines" :key="machine.name">
                <span>{{ machine.name }}</span>
                <MachineState :state="machine.state" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.machine-pool {
    color: white;
    border: 1px solid white;
    display: grid;
    grid-template-columns: 8fr 3fr;
    max-height: 100%;
    gap: 2px;
    background-color: white;
    min-height: 0;
}
.criticalMachines {
    background-color: black;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 10px
}
.criticalMachineLine {
    display: flex;
    gap: 10px;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.machineLogo {
    position: relative;
}
.stateLogo {
    position: absolute;
    bottom: 0;
    right: -5px;
}
.allMachines {
    display: flex;
    flex-direction: column;
    border: 1px solid white;
    padding: 10px;
    font-size: 12px;
    background-color: black;
    overflow: scroll;
    min-height: 0;
}
.allMachineLine {
    display: flex;
    justify-content: space-between;
}
</style>