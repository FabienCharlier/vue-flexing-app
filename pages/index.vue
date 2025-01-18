<script setup>
import { ref } from 'vue';

const bus = ref([]);
const messageId = ref(0);
const configurationPanelOpened = ref(false);

const widgetList = ref(["machine-pool", "logs-terminal", "writable-terminal", "bars"]);
const templateType = ref("twoByTwoGrid");

const allWidgetsList = [
    {code: "machine-pool", name: "Parc de machines"},
    {code: "logs-terminal", name: "Terminal d'affichage de logs"},
    {code: "writable-terminal", name: "Terminal d'émission de commandes"},
    {code: "bars", name: "Divers graphiques de performance"}
];
const allTemplateTypes = [
    {
        code: "twoByTwoGrid",
        size: 4,
        name: "quatre widgets en 2x2",
        styles: {}
    },
    {
        code: "oneByOneGrid",
        size: 1,
        name: "un seul widget",
        styles: {}
    },
    {
        code: "oneLeftThreeRight",
        size: 4,
        name: "un gros widget principal à gauche, trois petits à droite",
        styles: {0: {gridColumn: "1 / 2", gridRow: "1 / 4"}}
    },
]
const completeFullTemplateType = computed(() => {
    return allTemplateTypes.find((element) => element.code === templateType.value) ?? {};
})

const updateGivenWidget = (widgetName, position) => {
    widgetList.value[position] = widgetName;
}

const updateTowardsTemplate = (template) => {
    templateType.value = template.code;
    const currentWidgetNumber = widgetList.value.length;
    if (currentWidgetNumber === template.size) {
        return;
    } else if (currentWidgetNumber < template.size) {
        for (let i = currentWidgetNumber; i < template.size; i++) {
            widgetList.value.push("bars");
        }
    } else {
        widgetList.value = widgetList.value.slice(0, template.size);
    }
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
    <div class="grid-main-container" :class="templateType">
        <template v-for="(widget, index) in widgetList" :key="index">
            <EditableWidget
                :type="widget"
                :bus="bus"
                :handlingFunctions="handlingFunctions"
                :style="index in completeFullTemplateType.styles ? completeFullTemplateType.styles[index] ?? {} : {}"
            />
        </template>
    </div>
    <div v-if="configurationPanelOpened" class="configurationPanel">
        <h3>Panneau de configuration {{ widgetList.length }}</h3>
        <div>Template d'affichage</div>
        <template v-for="template in allTemplateTypes" :key="template.code">
            <button @click="() => updateTowardsTemplate(template)" class="stylishButton">{{ template.code }}</button>
        </template>
        <template v-for="slot in widgetList.length" :key="slot">
            <div>Widget à mettre dans l'emplacement : {{  slot }}</div>
            <template v-for="widget in allWidgetsList" :key="slot.toString() + widget.code">
                <button @click="() => updateGivenWidget(widget.code, slot - 1)" class="stylishButton">{{ widget.name }}</button>
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
        gap: 20px;
        height: calc(100% - 40px);
        padding: 20px;
    }

    .twoByTwoGrid {
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr 1fr;
    }

    .oneByOneGrid {
        grid-template-columns: 1fr;
        grid-template-rows: 1fr;
    }

    .oneLeftThreeRight {
        grid-template-columns: 2fr 1fr;
        grid-template-rows: 1fr 1fr 1fr;
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

    .stylishButton {
        border-radius: 10px;
        border: 1px solid white;
        background-color: black;
        color: white;
    }

    .stylishButton:hover {
        border: 2px solid white;
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