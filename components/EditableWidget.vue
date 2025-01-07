<script setup>
const { type, bus, handlingFunctions } = defineProps(['type', 'bus', 'handlingFunctions']);
</script>

<template>
    <MachinePool v-if="type === 'machine-pool'" :bus="bus" />
    <WritableTerminal 
        v-else-if="type === 'writable-terminal'"
        @reboot="handlingFunctions.handleReboot" 
        @online="handlingFunctions.handleOnline" 
        @offline="handlingFunctions.handleOffline" 
        @error="handlingFunctions.handleError" 
        @settings="handlingFunctions.handleSettings" 
        @closesettings="handlingFunctions.handleCloseSettings"
    />
    <Bars v-else-if="type === 'bars'" :bus="bus" />
    <LogsTerminal v-else :bus="bus" />
</template>