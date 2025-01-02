<script setup>
const { value, title } = defineProps(['value', 'title']);
</script>

<template>
    <div class="singleBar">
        <div>
            {{ title }}
        </div>
        <div class="cellsContainer">
            <div class="barCell" :class="[value >= 1 ? 'color1' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 2 ? 'color2' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 3 ? 'color3' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 4 ? 'color4' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 5 ? 'color5' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 6 ? 'color6' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 7 ? 'color7' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 8 ? 'color8' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 9 ? 'color9' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 10 ? 'color10' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 11 ? 'color11' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 12 ? 'color12' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 13 ? 'color13' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 14 ? 'color14' : 'black']">
                &nbsp;
            </div>
            <div class="barCell" :class="[value >= 15 ? 'color15' : 'black']">
                &nbsp;
            </div>
        </div>
        <div>
            {{ value }}%
        </div>
    </div>
</template>

<style scoped>
.singleBar {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 10px;
}

.cellsContainer {
    display: flex;
    flex-direction: row;
    gap: 3px;
    align-items: center;
    justify-content: center;
}

.barCell {
    width: 8px;
    height: 20px;
}

.black {
    background-color: black;
}

.color1 {
    background-color: #002fba;
}
.color2 {
    background-color: #0542ab;
}
.color3 {
    background-color: #0a559c;
}
.color4 {
    background-color: #10688d;
}
.color5 {
    background-color: #157b7e;
}
.color6 {
    background-color: #1a8e6f;
}
.color7 {
    background-color: #1fa05f;
}
.color8 {
    background-color: #24b350;
}
.color9 {
    background-color: #29c641;
}
.color10 {
    background-color: #2fd932;
}
.color11 {
    background-color: #34ec23;
}
.color12 {
    background-color: #39ff14;
}
.color13 {
    background-color: #39ff14;
}
.color14 {
    background-color: #39ff14;
}
.color15 {
    background-color: #39ff14;
}
</style>