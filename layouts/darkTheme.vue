<template>
    <div class="dark-theme-container">
        <slot />
    </div>
</template>

<style>
    html {
        box-sizing: border-box;
    }
    body {
        margin: 0;
        padding: 0;
    }
    .dark-theme-container {
        background-color: black;
        color: white;
        width: 100%;
        height: 100vh;
    }
</style>