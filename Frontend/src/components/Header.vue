<script setup>
    const props = defineProps({
        text:String
    })
</script>
<template>
    <div>
        <h1> {{ props.text }}</h1>
    </div>
</template>
<style scoped>
div{
    display: flex;
    flex-direction: row;
    align-content: center;
    align-items: center;
    padding-inline: 5%;
    width: 100%;
    height: 10%;
    background-color: var(--color-accent);
    border-style: outset;
    border-width: 10px;
    border-color: var(--color-accent);
}

h1 {
    color: white;
}
</style>