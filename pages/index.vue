<script setup>
import { ref } from 'vue';

const bus = ref([]);
const messageId = ref(0);
const configurationPanelOpened = ref(false);
const widgetList = ref(["machine-pool", "logs-terminal", "writable-terminal", "bars"]);

const allWidgetsList = [
    {code: "machine-pool", name: "Parc de machines"},
    {code: "logs-terminal", name: "Terminal d'affichage de logs"},
    {code: "writable-terminal", name: "Terminal d'émission de commandes"},
    {code: "bars", name: "Divers graphiques de performance"}
];

const updateGivenWidget = (widgetName, position) => {
    widgetList.value[position] = widgetName;
}

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
const handleSettings = () => {
    console.log("Settings");
    configurationPanelOpened.value = true;
}
const handleCloseSettings = () => {
    configurationPanelOpened.value = false;
}
const handlingFunctions = {
    handleReboot,
    handleError,
    handleOffline,
    handleOnline,
    handleSettings,
    handleCloseSettings
}

useSeoMeta({
  title: 'Monitoring dashboard',
  description: 'Monitoring dashboard',
})

</script>

<template>
    <div class="grid-main-container">
        <EditableWidget v-for="(widget, index) in widgetList" :key="index" :type="widget" :bus="bus" :handlingFunctions="handlingFunctions" />
    </div>
    <div v-if="configurationPanelOpened" class="configurationPanel">
        <h3>Panneau de configuration {{ widgetList.length }}</h3>
        <template v-for="slot in widgetList.length" :key="slot">
            <div>Widget à mettre dans l'emplacement : {{  slot }}</div>
            <template v-for="widget in allWidgetsList" :key="slot.toString() + widget.code">
                <button @click="() => updateGivenWidget(widget.code, slot - 1)">{{ widget.name }}</button>
            </template>
        </template>
    </div>
    <button class="configurationPanelButton" @click="configurationPanelOpened = !configurationPanelOpened">&nbsp;</button>
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

    .configurationPanel {
        position: absolute;
        background-color: black;
        color: white;
        border: 2px solid white;
        box-sizing: border-box;
        height: 100%;
        width: 35%;
        top: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        gap: 10px;
        align-items: center;
    }

    .configurationPanelButton {
        position: absolute;
        bottom: 0;
        left: 0;
        background-color: black;
        color: black;
        border: none;
    }
</style>