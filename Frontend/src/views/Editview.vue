<script setup>
    import {ref, onMounted, h} from "vue";
    import { useRoute } from 'vue-router'; 
    import Header from "../components/Header.vue";
    import Warning from "../components/Warning.vue";
    import alumnos from "../assets/mockdata/studentts.json";
    import {ModalType} from "../types.js";

    const route = useRoute();

    const stdlist = ref(alumnos.alumnos);
    const student = ref({});

    const studentmap = ref({});
    const Studentname = ref();
    const Studentlastname = ref();
    const Studentturn = ref()
    const modaltype = ref()

    const warningtitle = ref("")
    const warningtext = ref("")
    const warningok = ref(Function)
    const warningcancel = ref(Function)
    const attr = new Array()

    onMounted(()=>{
        const param = Number(route.params.student);
        studentmap.value = stdlist.value.map((obj) => studentmap.value[obj.id]=obj);
        student.value = studentmap.value[param]
        Studentname.value = student.value.nombre
        Studentlastname.value = student.value.apellido
        Studentturn.value = student.value.turno
        let turnos = document.getElementsByName("turno")
        for (let turno of turnos){
            turno.checked = turno.value.toLowerCase() == Studentturn.value.toLowerCase();
            turno.addEventListener('change',() => {
                Studentturn.value = turno.value
            })
        }
    })

    function keepEditting () {
        let modal = document.getElementById("modal")
        modal.style.display = "none"
    }

    function exitEditing () {
        var owner = window.self;
        owner.opener = window.self;
        owner.close();
    }

    function overwriteStudent() {
        let modal = document.getElementById("modal")
        modal.style.display= "block"
        warningtitle.value = "Edición Guardada"
        warningtext.value = "Tus cambios se han guardado correctamente"
        warningok.value=exitEditing
        warningcancel.value=exitEditing
        modaltype.value=ModalType['info']
    }

    function saveStudent() {
        Studentname.value = document.getElementById("name").value
        Studentlastname.value = document.getElementById("lastname").value
        let modal = document.getElementById("modal")
        if (Studentname.value == student.value.nombre && Studentlastname.value == student.value.apellido && Studentturn.value == student.value.turno) {
            warningtext.value = "No hay cambios en la información del estudiate"
            warningok.value=keepEditting
            warningcancel.value=keepEditting
            modaltype.value=ModalType['info']
        } else {
            warningtext.value = "Estás a punto de sobreescribir este estudiante.¿Deseas continuar?"
            warningok.value=overwriteStudent
            warningcancel.value=keepEditting
            modaltype.value=ModalType['warn']
        }
        modal.style.display= "block"
        warningtitle.value = "Guardar Edición"
    }

    function closeEdit() {
        var owner = window.self;
        owner.opener = window.self;
        Studentname.value = document.getElementById("name").value
        Studentlastname.value = document.getElementById("lastname").value
        if (Studentname.value == student.value.nombre && Studentlastname.value == student.value.apellido && Studentturn.value == student.value.turno) {
            owner.close();
        } else {
            let modal = document.getElementById("modal")
            modal.style.display= "block"
            warningtitle.value = "Cancelar Edición"
            warningtext.value = "Tus cambios se perderán. ¿Deseas cerrar la ventana de edición sin guardar?"
            warningok.value=exitEditing
            warningcancel.value=keepEditting
            modaltype.value=ModalType['warn']
        }
    }
</script>
<template>
    <Warning 
        :title="warningtitle"
        :Text= "warningtext"
        :cancelaction="warningcancel"
        :cancelactionparams="attr"
        :confirmaction="warningok"
        :confirmationparams="attr"
        :messagetype="modaltype">
    </Warning>
    <Header text="Editar estudiante"></Header>
    <div id="main">
        <div>
            <label for="name">Nombre: </label>
            <input type=text id="name" :value="Studentname"/>
        </div>
        <div>
            <label for="lastname">Apellido: </label>
            <input type=text id="lastname" :value="Studentlastname"/>
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
            <button class="button" @click = "() => saveStudent()">
                <i class="fa fa-check" aria-hidden="true"></i>
                Confirmar
            </button>
            <button class="button" @click = "() => closeEdit()">
                <i class="fa fa-ban" aria-hidden="true"></i>
                Cancelar
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