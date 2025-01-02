<script setup>
const { value, title } = defineProps(['value', 'title']);
</script>

<template>
    <div class="singleBar">
        <div class="barCell" :class="[value >= 10 ? 'color10' : 'black']">
            &nbsp;
        </div>
        <div class="barCell" :class="[value >= 9 ? 'color9' : 'black']">
            &nbsp;
        </div>
        <div class="barCell" :class="[value >= 8 ? 'color8' : 'black']">
            &nbsp;
        </div>
        <div class="barCell" :class="[value >= 7 ? 'color7' : 'black']">
            &nbsp;
        </div>
        <div class="barCell" :class="[value >= 6 ? 'color6' : 'black']">
            &nbsp;
        </div>
        <div class="barCell" :class="[value >= 5 ? 'color5' : 'black']">
            &nbsp;
        </div>
        <div class="barCell" :class="[value >= 4 ? 'color4' : 'black']">
            &nbsp;
        </div>
        <div class="barCell" :class="[value >= 3 ? 'color3' : 'black']">
            &nbsp;
        </div>
        <div class="barCell" :class="[value >= 2 ? 'color2' : 'black']">
            &nbsp;
        </div>
        <div class="barCell" :class="[value >= 1 ? 'color1' : 'black']">
            &nbsp;
        </div>
        <div>
            {{ title }}
        </div>
    </div>
</template>

<style scoped>
.singleBar {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 3px;
}

.barCell {
    width: 20px;
    height: 8px;
}

.black {
    background-color: black;
}

.color1 {
    background-color: #002fba;
}
.color2 {
    background-color: #084da2;
}
.color3 {
    background-color: #106a8b;
}
.color4 {
    background-color: #188873;
}
.color5 {
    background-color: #21a65b;
}
.color6 {
    background-color: #29c443;
}
.color7 {
    background-color: #31e12c;
}
.color8 {
    background-color: #39ff14;
}
.color9 {
    background-color: #39ff14;
}
.color10 {
    background-color: #39ff14;
}
</style>