<script setup>
const { bus } = defineProps(['bus']);

const currentId = ref(0);
</script>

<template>
    <div class="terminal">
        <div class="circularGraphs">
            <CircularGraph value="37" title="Puissance" />
            <CircularGraph value="50" title="Puissance" />
        </div>
        <div class="horizontalBars">
            <SingleBarHorizontal value="5" title="Temperature"/>
            <SingleBarHorizontal value="14" title="Temperature"/>
        </div>
        <div class="multipleBars">
            <SingleBarVertical value="1" title="CPU 1/10"/>
            <SingleBarVertical value="5" title="CPU 2/10"/>
            <SingleBarVertical value="5" title="CPU 3/10"/>
            <SingleBarVertical value="5" title="CPU 4/10"/>
            <SingleBarVertical value="5" title="CPU 5/10"/>
            <SingleBarVertical value="5" title="CPU 6/10"/>
            <SingleBarVertical value="5" title="CPU 7/10"/>
            <SingleBarVertical value="10" title="CPU 8/10"/>
            <SingleBarVertical value="10" title="CPU 9/10"/>
            <SingleBarVertical value="10" title="CPU 10/10"/>
        </div>
        <div>
            Toto
            Tata
            Tutu
            Titi
            (random text)
        </div>
    </div>
</template>

<style scoped>
.terminal {
  background-color: black;
  border: 1px solid white;
  padding: 15px;
  max-height: 100%;
  font-family: monospace;
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 10px;
}

.circularGraphs {
    display: flex;
    gap: 15px;
    justify-content: space-around;
    align-items: center;
    color: white;
}

.horizontalBars {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}

.multipleBars {
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: space-around;
    align-items: end;
}
</style>