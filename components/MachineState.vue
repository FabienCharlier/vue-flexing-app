<script setup>
const props = defineProps({
  state: Number
})
</script>

<template>
    <span v-if="state === 1" class="status online">online</span>
    <span v-if="state === 2" class="status offline">offline</span>
    <span v-if="state === 3" class="status criticalError">critical error</span>
</template>

<style scoped>
.status {
    text-transform: capitalize;
    text-align: center;
}
.online {
    color: #39FF14;
}
.offline {
    color: #FFCD00;
}
.criticalError {
    color: red;
}
</style>