<script setup>
import { ref, computed, onMounted } from "vue"
import {get_Current_Students} from "../apiservice"

const entrynum = ref(5)
const currentpage = ref(1)
const open = ref(false)

const alumnos = ref(new Array)

const stdlist = ref(new Array)

const numpages = computed(() => {
    return Math.ceil(stdlist.value.length / entrynum.value)
})

const pendingelements = computed(() => {
    return stdlist.value.length -  (currentpage.value - 1) * entrynum.value
})

const range = computed(() => {
    return Math.min(entrynum.value, pendingelements.value);
})

const offset = computed(() => {
    return (currentpage.value - 1) * entrynum.value;
})

function changetab(_evt, tabname, val){
    entrynum.value = val;
    currentpage.value = currentpage.value >= numpages.value ? numpages.value : currentpage.value;

    const tablinks = document.getElementsByClassName("tab");

    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" selected", "");
    }

    const current = document.getElementById(tabname);

    current.className += " selected";
}

function managefilter() {
    currentpage.value = 1
    let listofchecks = document.getElementsByClassName("checkbox")
    let filterlist = []
    for( var check of listofchecks){
        if (!check.checked) {
            filterlist.push(check.value)
        }
    }
    stdlist.value = alumnos.value.filter((elem)=>{
        return !filterlist.includes(elem.shift)
    })

}

onMounted(async()=>{
    alumnos.value = await get_Current_Students()
    stdlist.value = alumnos.value
    managefilter()
})

</script>
<template>
    <div>
        <table>
            <thead>
                <tr>
                    <th> Apellido</th>
                    <th> Nombre</th>
                    <th>Fecha Inicio</th>
                    <th>Fecha Fin</th>
                    <div id="filtercontainer">
                        <th style="width: 100%; border: none;"> Turno</th>
                        <button style="color: white;" @click="open = !open">
                            <i class="fa-solid fa-filter"></i>
                        </button>
                        <div class="filter" v-show="open">
                            <fieldset>
                                <legend>Turnos:</legend>
                                <label class="container">Mañana
                                    <input class="checkbox" type="checkbox" checked @change="(event) => managefilter(event)" value="Mañana">
                                    <span class="checkmark"></span>
                                </label>

                                <label class="container">Tarde
                                    <input class="checkbox" type="checkbox" checked @change="(event) => managefilter(event)" value="Tarde">
                                    <span class="checkmark"></span>
                                </label>

                                <label class="container">Intensivo
                                    <input class="checkbox" type="checkbox" checked @change="(event) => managefilter(event)" value="Intensivo">
                                    <span class="checkmark"></span>
                                </label>
                            </fieldset>
                        </div>
                    </div>
                </tr>
            </thead>
            <tbody>
                <tr v-for="index in range" >
                    <td> {{ stdlist[index + offset - 1].lastname }}</td>
                    <td> {{ stdlist[index + offset - 1].name }}</td>
                    <td> {{ stdlist[index + offset - 1].startDate }}</td>
                    <td> {{ stdlist[index + offset - 1].endDate }}</td>
                    <td> {{ stdlist[index + offset - 1].shift }}</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <th colspan="5">
                        <div class="tablediv">
                            <button @click="currentpage--" :disabled="currentpage <= 1"><i class="fa-solid fa-angles-left"></i></button>
                            <label>{{ numpages == 0 ? numpages : currentpage }}/{{ numpages }}</label>
                            <button @click="currentpage++" :disabled="currentpage >= numpages"><i class="fa-solid fa-angles-right"></i></button>
                        </div>
                    </th>
                </tr>
                <tr>
                    <td colspan="5"> 
                        <div style="display: flex; flex-direction: row; justify-content: space-around;">
                            <div id="5" class="tablediv tab selected"  @click="changetab(event, '5', 5)">
                                <span>5</span>
                            </div>
                        
                            <div id="10" class="tablediv tab" @click="changetab(event, '10', 10)">
                                <span>10</span>
                            </div>
                        </div>
                    </td>
                </tr>
            </tfoot>
        </table>
    </div>
</template>
<style scoped>
div{
    display: flex;
    justify-items:baseline;
    text-align: center;
}

fieldset {
    display: flex;
    flex-direction: column;
    color:black;
    width: 100%;
    text-align: left;
}

table {
    height: 80vh;
}

tfoot{
    text-align: center;
}

tfoot td {
    border: none;
}

tfoot th {
    border-top: 2px groove var(--color-accent);
    border-bottom: none;
    border-inline: none;
}

tbody tr:nth-child(even) {
  background-color: var(--color-background-soft);
}

td, th {
  width:20%;
  height:42px;
}

button{
    margin-inline: 10px;
    cursor: pointer;
    border: none;
    background-color: transparent;
}

button:disabled {
    cursor: default;
}

legend {
    text-align: center;
}

.filter{
    position: absolute;
    top: 19vh;
    right: 7vw;
    height: 25vh;
    width: 15vw;
    background-color: var(--color-background);
}
.tablediv {
    display: flex; 
    flex-direction: row; 
    justify-content: center;
    justify-content: center;
}

.tab{
    width: 15%;
    border-style: inset;
    border-width: 4px;
    border-color: var(--color-border);
    border-radius: 3px;
    cursor: pointer;
}

.tab:hover {
    background-color: var(--color-hover);
}

.selected {
    background-color: var(--color-accent);
    color: white;
}

 /* Customize the label (the container) */
 .container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 22px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Hide the browser's default checkbox */
.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 25px;
  width: 25px;
  background-color: var(--color-background);
}

/* On mouse-over, add a grey background color */
.container:hover input ~ .checkmark {
  background-color: var(--color-background-soft);
}

/* When the checkbox is checked, add a blue background */
.container input:checked ~ .checkmark {
  background-color: var(--color-accent);
}

/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the checkmark when checked */
.container input:checked ~ .checkmark:after {
  display: block;
}

/* Style the checkmark/indicator */
.container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
} 

#filtercontainer {
    border: 2px solid var(--color-border);
    padding-top: 4%;
}
</style>