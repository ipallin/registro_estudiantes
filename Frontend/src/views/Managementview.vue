<script setup>
</script>
<template>
    <div id="main">
        <div>
            <label for="name">Nombre: </label>
            <input type=text id="name"/>
        </div>
        <div>
            <label for="lastname">Apellido: </label>
            <input type=text id="lastname"/>
        </div>
        <div>
            <label for="StartDate">Fecha de Inicio: </label>
            <input type=date id="StartDate"/>
        </div>
        <fieldset>
            <legend>Turno:</legend>
            <div id="radiocontainer">
                <div>
                    <input type=radio id="manana" value="Mañana" name="turno"/>
                    <label for="manana">Mañana </label>
                </div>
                <div>
                    <input type=radio id="tarde" value="Tarde" name="turno"/>
                    <label for="tarde">Tarde </label>
                </div>
                <div>
                    <input type=radio id="intensivo" value="Intensivo" name="turno"/>
                    <label for="intensivo">Intensivo </label>
                </div>
            </div>
        </fieldset>
        <div id="buttonarea">
            <button class="button">
                <i class="fa fa-plus" aria-hidden="true"></i>
                Añadir Estudiante
            </button>
        </div>
    </div>
</template>
<style scoped>
#main {
    flex-direction: column;
    padding: 2%;
}

#radiocontainer {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

div {
    display: flex;
    flex-direction: row;
}

label{
    display: flex;
    margin-left: 5px;
    margin-right: 10px;
    align-items: center;
}

input {
  border: 1px solid var(--color-border);
  padding: 10px;
  font-size: 16px;
}

input[type=text] {
  background-color: white;
  width: 40%;
  margin-block: 1%;
}
</style>