<script setup>
import { ref } from 'vue';

const bus = ref([]);
const messageId = ref(0);

const handleReboot = (command) => {
    bus.value.push({id: messageId.value, type: 'reboot', command: command});
    messageId.value++;
}
const handleError = (command) => {
    bus.value.push({id: messageId.value, type: 'error', command: command});
    messageId.value++;
}
const handleOffline = (command) => {
    bus.value.push({id: messageId.value, type: 'offline', command: command});
    messageId.value++;
}
const handleOnline = (command) => {
    bus.value.push({id: messageId.value, type: 'online', command: command});
    messageId.value++;
}

</script>

<template>
    <div class="grid-main-container">
        <MachinePool :bus="bus" />
        <LogsTerminal :bus="bus" />
        <WritableTerminal @reboot="handleReboot" @online="handleOnline" @offline="handleOffline" @error="handleError"/>
        <Bars :bus="bus" />
    </div>
</template>

<style scoped>
    .title {
        margin: 0 auto;
        padding: 30px 10px;
        grid-column: 1 / 3;
    }

    .grid-main-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 9fr 9fr;
        gap: 20px;
        height: calc(100% - 40px);
        padding: 20px;
    }

    .single-widget {
        grid-column: 1 / 3;
        grid-row: 2 / 4;
    }
</style>