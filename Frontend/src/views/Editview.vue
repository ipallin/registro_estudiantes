<script setup>
    import {ref, onMounted} from "vue";
    import { useRoute } from 'vue-router'; 
    import Header from "../components/Header.vue";
    import Warning from "../components/Warning.vue";
    import {ModalType} from "../types.js";
    import {get_Student, edit_student} from "../apiservice"

    const route = useRoute();

    const student = ref({});

    const Studentname = ref();
    const Studentlastname = ref();
    const Studentturn = ref();
    const startdate = ref();
    const enddate = ref();
    
    

    const warningtitle = ref("")
    const warningtext = ref("")
    const warningok = ref(Function)
    const warningcancel = ref(Function)
    const attr = new Array()
    const modaltype = ref()

    onMounted(async()=>{
        const param = Number(route.params.student);
        student.value = await get_Student(param)
        Studentname.value = student.value.name
        Studentlastname.value = student.value.lastname
        Studentturn.value = student.value.shift
        startdate.value = student.value.startDate
        enddate.value = student.value.endDate
        let turnos = document.getElementsByName("turno")
        for (let turno of turnos){
            turno.checked = turno.value == Studentturn.value;
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
        const param = Number(route.params.student);
        let stardate = new Date(startdate.value)
        let endate = new Date(enddate.value)
        let ststartdate = stardate.toISOString().split("T")[0]
        let stenddate = endate.toISOString().split("T")[0]
        let stud = {
            id:param,
            name:Studentname.value,
            lastname: Studentlastname.value,
            shift:Studentturn.value,
            startDate: ststartdate,
            endDate: stenddate
        }
        edit_student(stud).then(()=> {
            let modal = document.getElementById("modal")
            modal.style.display= "block"
            warningtitle.value = "Edición Guardada"
            warningtext.value = "Tus cambios se han guardado correctamente"
            warningok.value=exitEditing
            warningcancel.value=exitEditing
            modaltype.value=ModalType['info']
        })    
    }

    function saveStudent() {
        Studentname.value = document.getElementById("name").value
        Studentlastname.value = document.getElementById("lastname").value
        let modal = document.getElementById("modal")
        if (Studentname.value == student.value.name && Studentlastname.value == student.value.lastname && Studentturn.value == student.value.turno && startdate.value == student.value.startDate && enddate.value == student.value.endDate) {
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

    function startdatehandler(ev) {
        startdate.value = ev.target.value
    }

    function enddatehandler(ev) {
        enddate.value = ev.target.value
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
        <div style="display: flex; flex-direction: row;">
            <div>
                <label for="startdate">Fecha de inicio: </label>
                <input type="date" id="startdate" :value="startdate" @change="(ev) => startdatehandler(ev)"/>
            </div>
            <div>
                <label for="enddate">Fecha de fin: </label>
                <input type="date" id="enddate" :value="enddate" @change="(ev) => enddatehandler(ev)"/>
            </div>
        </div>
        <fieldset>
            <legend>Turno:</legend>
            <div id="radiocontainer">
                <div>
                    <input type=radio id="Mañana" value="Mañana" name="turno"/>
                    <label for="Mañana">Mañana </label>
                </div>
                <div>
                    <input type=radio id="Tarde" value="Tarde" name="turno"/>
                    <label for="Tarde">Tarde </label>
                </div>
                <div>
                    <input type=radio id="Intensivo" value="Intensivo" name="turno"/>
                    <label for="Intensivo">Intensivo </label>
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