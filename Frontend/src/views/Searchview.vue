<script setup>
import { ref, onMounted } from "vue"
import {useRouter} from 'vue-router'
import Warning from "../components/Warning.vue"
import {ModalType} from "../types.js"
import {get_Students, delete_student} from "../apiservice"

const stdlist = ref(new Array);
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

    get_Students().then((res)=>{
        stdlist.value = res
        studentmap.value = stdlist.value.map((obj) => studentmap.value[obj.id]=obj);
        namelist.value = stdlist.value.map(({name, lastname}) => `${lastname} ${name}`);
        
        let nameinput = document.getElementById("nameinput")
        array.value = Object.values(studentmap.value)
        autocomplete(nameinput, array.value)
    })
    
})

function autocomplete(inp, arr) {
    inp.addEventListener("input", function() {
        var val = this.value;
        if (!val || val == "") {
            filteredlist.value = [];
        } else{
            filteredlist.value = arr.filter((elem) => {
                let name = `${elem.lastname} ${elem.name}`
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
    delete_student(id).then((ok) => {
        if (ok) {
                get_Students().then((res)=>{
                    let nameinput = document.getElementById("nameinput")
                    nameinput.value = ""
                    stdlist.value = res
                    studentmap.value = stdlist.value.map((obj) => studentmap.value[obj.id]=obj);
                    namelist.value = stdlist.value.map(({name, lastname}) => `${lastname} ${name}`);
                    autocomplete(nameinput, namelist.value)
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
                })
        } else {
            let modal = document.getElementById("modal")
            modal.style.display= "block"
            warningtitle.value = "Error"
            warningtext.value = "El alumno no ha podido eliminarse"
            warningok.value=closeModal
            warningcancel.value=closeModal
            okattr.value = []
            cancelattr.value = []
            modaltype.value=ModalType['info']
        }
    })
}

function openEdit(id) {
    let nameinput = document.getElementById("nameinput")
    nameinput.value = ""
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
                    {{elem.lastname}} {{elem.name}}
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