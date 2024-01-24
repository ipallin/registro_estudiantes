<script setup>
    import {ref, onMounted} from "vue";
    import Warning from "../components/Warning.vue";
    import {ModalType} from "../types.js";
    import {add_student} from "../apiservice"

    const Studentname = ref();
    const Studentlastname = ref();
    const Studentturn = ref();
    const date = ref();

    const warningtitle = ref("")
    const warningtext = ref("")
    const warningok = ref(Function)
    const warningcancel = ref(Function)
    const attr = ref(new Array())
    const modaltype = ref()

    onMounted(async()=>{
        let turnos = document.getElementsByName("turno")
        for (let turno of turnos){
            turno.addEventListener('change',() => {
                Studentturn.value = turno.value
            })
        }
    })

    function managedatechange(ev) {
        date.value = ev.target.value
    }

    function keepEditting () {
        let modal = document.getElementById("modal")
        modal.style.display = "none"
    }

    function saveStudent() {
        Studentname.value = document.getElementById("name").value
        Studentlastname.value = document.getElementById("lastname").value
        let modal = document.getElementById("modal")
        if (Studentname.value == null  || Studentlastname.value == null || Studentturn.value == null || date.value == null) {
            warningtitle.value = "Campos en Blanco"
            warningtext.value = "Debes rellenar todos los campos solicitados para poder guardar un nuevo estudante"
            warningok.value=keepEditting
            warningcancel.value=keepEditting
            modaltype.value=ModalType['info']
        } else {
            warningtitle.value = "Guardar Estudiante"
            warningtext.value = "Estás a punto de añadir un nuevo estudiante.¿Deseas continuar?"
            warningok.value=overwriteStudent
            warningcancel.value=keepEditting
            modaltype.value=ModalType['warn']
        }
        modal.style.display= "block"
        warningtitle.value = "Guardar Edición"
    }

    function overwriteStudent() {

        let startdate = new Date(date.value)
        let endate = new Date(date.value)
        const theDayOfTheMonthOnNextWeek = Studentturn.value == "Intensivo" ? startdate.getDate() + 7 : startdate.getDate() + 15;
        endate.setDate(theDayOfTheMonthOnNextWeek)
        let ststartdate = startdate.toISOString().split("T")[0]
        let stenddate = endate.toISOString().split("T")[0]
        let stud = {
            name:Studentname.value,
            lastname: Studentlastname.value,
            shift:Studentturn.value,
            startDate: ststartdate,
            endDate: stenddate
        }
        add_student(stud).then(()=> {
            location.reload();
            let modal = document.getElementById("modal")
            modal.style.display= "block"
            warningtitle.value = "Estudiante Guardado"
            warningtext.value = "El estudiante se ha guardado correctamente"
            warningok.value=keepEditting
            warningcancel.value=keepEditting
            modaltype.value=ModalType['info']
        })    
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
    <div id="main">
        <div>
            <label for="name">Nombre: </label>
            <input type=text id="name" :value="Studentname"/>
        </div>
        <div>
            <label for="lastname">Apellido: </label>
            <input type=text id="lastname" :value="Studentlastname"/>
        </div>
        <div>
            <label for="StartDate">Fecha de Inicio: </label>
            <input type=date id="StartDate" @change="(ev) => managedatechange(ev)"/>
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