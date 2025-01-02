<script setup>
import { ref } from 'vue';

const { value, title } = defineProps(['value', 'title']);

const styleObject = computed(() => {
    return {
        "background-image": `conic-gradient(black 0%, black 100%), conic-gradient(#39FF14 0%, #39FF14 ${value}%, #4a4a4a ${value}%, #4a4a4a 100%)`,
    }
});

</script>

<template>
    <div class="circularGraphAndLabels">
        <div :style="styleObject" class="graph">
            <div class="percentage">{{ value }}%</div>
        </div>
        <div>{{ title }}</div>
    </div>
</template>

<style>
.circularGraphAndLabels {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
    justify-content: center;
}

.graph {
    width: 100px;
    height: 100px;
    border: solid 8px transparent;
    border-radius: 50%;
    background-origin: border-box;
    background-clip: content-box, border-box;
    display: flex;
    align-items: center;
    justify-content: center;
}

.percentage {
    font-weight: bold;
    font-size: 22px;
}
</style>