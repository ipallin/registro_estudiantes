<script setup>

</script>
<template>
    <div id="box">
        <dl>
            <dt>
                <router-link
                    to="/Home"
                    custom
                    v-slot="{ href, route, navigate, isActive, isExactActive }"
                    >
                    <NavLink :class="isActive ? 'active':'nonactive'" :active="isActive" :href="href" @click="navigate">
                        <i class="fa fa-home navicon" aria-hidden="true"></i>
                        <label style="cursor: pointer;">HOME</label>
                    </NavLink>
                </router-link>
            </dt>

            <dt>
                <router-link
                    to="/List"
                    custom
                    v-slot="{ href, route, navigate, isActive, isExactActive }"
                    >
                    <NavLink :class="isActive ? 'active':'nonactive'" :active="isActive" :href="href" @click="navigate">
                        <i class="fa-solid fa-clipboard navicon"></i>
                        <label style="cursor: pointer;">LISTA DE ALUMNOS</label>
                    </NavLink>
                </router-link>
            </dt>

            <dt>
                <router-link
                    to="/Search"
                    custom
                    v-slot="{ href, route, navigate, isActive, isExactActive }"
                    >
                    <NavLink :class="isActive ? 'active':'nonactive'" :active="isActive" :href="href" @click="navigate">
                        <i class="fa-solid fa-magnifying-glass navicon"></i>
                        <label style="cursor: pointer;">BUSCADOR</label>
                    </NavLink>
                </router-link>
            </dt>

            <dt>
                <router-link
                    to="/Management"
                    custom
                    v-slot="{ href, route, navigate, isActive, isExactActive }"
                    >
                    <NavLink :class="isActive ? 'active':'nonactive'" :active="isActive" :href="href" @click="navigate">
                        <i class="fa-solid fa-people-roof navicon"></i>
                        <label style="cursor: pointer;">GESTION</label>
                    </NavLink>
                </router-link>
            </dt>

        </dl>
    </div>
</template>
<style scoped>
div{
    display: flex;
}

dt{
    display: flex;
    width: auto;
    height: 60px;
    margin-block: 10px;
    padding: 5px;
}

label{
    padding-right: 10px;
}
.navicon {
    width: 24px;
    height: 24px;
    padding-inline: 5%;
}

NavLink{
    display: flex;
    height: 100%;
    width: 100%;
    align-items: center;
    border-style: inset;
    border-width: 4px;
    border-color: var(--color-accent);
    border-radius: 3px;
    cursor: pointer;
}

NavLink:hover {
    background-color: var(--color-hover);
}

.active {
    background-color: var(--color-accent);
    color: white;
}

#box {
    display: flex;
    flex-direction: column;
    border-right-style: double;
    width: 20%;
}
</style>