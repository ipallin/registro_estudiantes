<script setup>
import { ref, onMounted } from "vue"
import {useRouter} from 'vue-router'
import alumnos from "../assets/mockdata/studentts.json"
import Warning from "../components/Warning.vue"
import {ModalType} from "../types.js"

const stdlist = ref(alumnos.alumnos);
const router = useRouter();

const studentmap = ref({});

const namelist = ref(new Array());
const filteredlist = ref(new Array);
const array = ref(new Array);

const modaltype = ref();
const warningtitle = ref("");
const okattr = ref(new Array)
const cancelattr = ref(new Array)
const warningtext = ref("");
const warningok = ref(Function);
const warningcancel = ref(Function);

onMounted(() => {

    studentmap.value = stdlist.value.map((obj) => studentmap.value[obj.id]=obj);
    namelist.value = stdlist.value.map(({nombre, apellido}) => `${apellido} ${nombre}`);
    
    let nameinput = document.getElementById("nameinput")
    array.value = Object.values(studentmap.value)
    autocomplete(nameinput, array.value)
})

function autocomplete(inp, arr) {
    inp.addEventListener("input", function() {
        var val = this.value;
        if (!val || val == "") {
            filteredlist.value = [];
        } else{
            filteredlist.value = arr.filter((elem) => {
                let name = `${elem.apellido} ${elem.nombre}`
                return name.toUpperCase().includes(val.toUpperCase())
            })
        }
    })
}

function handleDelete (id){
    let modal = document.getElementById("modal")
    modal.style.display= "block"
    warningtitle.value = "Borrar Alumno"
    warningtext.value = "Estás a punto de eliminar permanentemente un alumno. ¿Deseas continuar?"
    okattr.value = [id]
    cancelattr.value = []
    warningok.value=deleteStudent
    warningcancel.value=closeModal
    modaltype.value=ModalType['warn']
}

function closeModal () {
    let modal = document.getElementById("modal")
    modal.style.display= "none"
}

function deleteStudent(id) {
    let nameinput = document.getElementById("nameinput")
    delete studentmap.value[id];
    namelist.value = Object.values(studentmap.value).map(({nombre, apellido}) => `${apellido} ${nombre}`);
    nameinput.value = ""
    const newimput = nameinput.cloneNode(true);
    nameinput.parentNode.replaceChild(newimput, nameinput);
    array.value = Object.values(studentmap.value)
    autocomplete(newimput, array.value)
    filteredlist.value = []
    let modal = document.getElementById("modal")
    modal.style.display= "block"
    warningtitle.value = "Alumno Borrado"
    warningtext.value = "El alumno se ha eliminado correctamente"
    warningok.value=closeModal
    warningcancel.value=closeModal
    okattr.value = []
    cancelattr.value = []
    modaltype.value=ModalType['info']
}

function openEdit(id) {
    const MyPath =`Editstudent/${id}`;
    const routeData = router.resolve({path: MyPath});
    window.open(routeData.href,'Edit','toolbar=no,status=no,menubar=no,location=center,scrollbars=no,resizable=no,height=500,width=657');
}
</script>
<template>
    <Warning
        :title="warningtitle"
        :Text= "warningtext"
        :cancelaction="warningcancel"
        :cancelactionparams="cancelattr"
        :confirmaction="warningok"
        :confirmationparams="okattr"
        :messagetype="modaltype">
    </Warning>
    <fieldset>
        <legend>Buscador:</legend>
        <div class="filterrow">
            <label for="nameinput">Apellido [Nombre]:</label>
            <input type="text" id="nameinput" autocomplete="on"/>
        </div>
    </fieldset>
    <fieldset id="results">
        <legend>Resultados:</legend>
        <div id="autocomplete" class="autocomplete">
            <div v-for="elem in filteredlist" :key="elem.id" class="autocomplete-items">
                <div class="itemcontainer">
                    {{elem.apellido}} {{elem.nombre}}
                    <div id="buttonarea">
                        <button class="button" @click="() => {
                            handleDelete(elem.id)
                        }">
                            <i class="fa fa-trash" aria-hidden="true"></i>
                        </button>
                        <button class="button" @click="() => {
                            openEdit(elem.id)
                        }">
                            <i class="fa fa-pencil" aria-hidden="true"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </fieldset>
</template>
<style scoped>
label{
    display: flex;
    margin-left: 5px;
    margin-right: 10px;
    align-items: center;
}
legend{
    text-decoration: solid;
    text-transform: uppercase;
    font-weight: bolder;
}
input {
  border: 1px solid var(--color-border);
  padding: 10px;
  font-size: 16px;
}
input[type=text] {
  background-color: var(--color-background);
  width: 80%;
}
button{
    margin-inline: 2px;
}
.filterrow{
    display: flex;
    flex-direction: row;
    margin-bottom: 10px;
}

#results {
    margin-block: 5px;
    height: 80%;
}

#buttonarea {
    width: 20%;
    margin: 0;
    padding: 0;
    justify-content: end;
}
</style>