<script setup>
const props = defineProps({
  state: Number,
  textAlign: {
    type: String,
    default: 'center',
    validator: (value) => ['left', 'center', 'right'].includes(value)
  }
})
</script>

<template>
    <span v-if="state === 1" class="status online" :style="{textAlign}">online</span>
    <span v-if="state === 2" class="status offline" :style="{textAlign}">offline</span>
    <span v-if="state === 3" class="status criticalError" :style="{textAlign}">critical error</span>
</template>

<style scoped>
.status {
    text-transform: capitalize;
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