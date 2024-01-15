<script setup>
    import Header from "./Header.vue"
    import Drawer from "./Drawer.vue";
</script>
<template>
    <Header text="Registro de estudiantes"></Header>
    <div id="maincontainer">
        <Drawer></Drawer>
        <div id="content">
            <router-view></router-view>
        </div>
    </div>
</template>
<style scoped>
Header{
    width: 100%;
    height: 10%;
}
#maincontainer {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 90%;
}

#content {
    width: 80%;
    padding: 2%;
}
</style>