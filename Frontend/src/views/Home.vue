<script setup>
    import {ref, onMounted, computed, onUnmounted} from "vue"
    import {get_Current_Students, get_Students} from "../apiservice"

    const date = ref()
    const interval = ref()
    const stlist = ref(new Array)
    const curweekstudents = ref(new Array)
    const nextweekstudent = ref(new Array)


    const morning = computed(()=>(list)=>{
            return list.filter((alum) => { return alum.shift =="Mañana"}).length
        }
    )
    const afternoon = computed(()=>(list)=>{
            return list.filter((alum) => { return alum.shift =="Tarde"}).length
        }
    )
    const fullday = computed(()=>(list)=>{
            return list.filter((alum) => { return alum.shift =="Intensivo"}).length
        }
    )

    onMounted(async () => {
        stlist.value = await get_Current_Students()
        interval.value = setInterval (()=>{
            date.value = new Date(Date.now()).toLocaleString()
        }, 1000)
        let mon = getMonday(new Date())
        let currstart = mon.toISOString().split("T")[0]
        let fri = new Date(mon)
        let diff = fri.getDate() + 4;
        fri.setDate(diff);
        let currend = fri.toISOString().split("T")[0]
        let nextm = new Date(mon)
        diff = nextm.getDate() + 7;
        nextm.setDate(diff);
        let nextstart = nextm.toISOString().split("T")[0]
        let nextf = new Date(nextm)
        diff = nextf.getDate() + 4;
        nextf.setDate(diff);
        let nextend = nextf.toISOString().split("T")[0]
        curweekstudents.value= await get_Students(currstart, currend)
        console.log(curweekstudents.value)
        nextweekstudent.value= await get_Students(nextstart, nextend)
        console.log(nextweekstudent.value)
    })

    onUnmounted(()=>{
        clearInterval(interval.value);
    })

    function getMonday(d) {
        d = new Date(d);
        var day = d.getDay(),
            diff = d.getDate() - day + (day == 0 ? -6 : 1); // adjust when day is sunday
        return new Date(d.setDate(diff));
    }
</script>
<template>
    <div id="header">
        {{ date }}
    </div>
    <div id="tablecontainer">
        <table>
            <thead>
                <tr>
                    <td colspan="2">Numero total de estudiantes registrados</td>
                </tr>
                <tr>
                    <th> Turno</th>
                    <th> Nº de alumnos</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th> Mañana</th>
                    <td> {{morning(stlist)}}</td>
                </tr>
                <tr>
                    <th> Tarde</th>
                    <td> {{afternoon(stlist)}}</td>
                </tr>
                <tr>
                    <th> Intensivo</th>
                    <td> {{fullday(stlist)}}</td>
                </tr>
            </tbody>
        </table>
        <table>
            <thead>
                <tr>
                    <td colspan="2">Numero de estudiantes de semana actual</td>
                </tr>
                <tr>
                    <th> Turno</th>
                    <th> Nº de alumnos</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th> Mañana</th>
                    <td> {{morning(curweekstudents)}}</td>
                </tr>
                <tr>
                    <th> Tarde</th>
                    <td> {{afternoon(curweekstudents)}}</td>
                </tr>
                <tr>
                    <th> Intensivo</th>
                    <td> {{fullday(curweekstudents)}}</td>
                </tr>
            </tbody>
        </table>
        <table>
            <thead>
                <tr>
                    <td colspan="2">Numero de estudiantes de semana próxima</td>
                </tr>
                <tr>
                    <th> Turno</th>
                    <th> Nº de alumnos</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th> Mañana</th>
                    <td> {{morning(nextweekstudent)}}</td>
                </tr>
                <tr>
                    <th> Tarde</th>
                    <td> {{afternoon(nextweekstudent)}}</td>
                </tr>
                <tr>
                    <th> Intensivo</th>
                    <td> {{fullday(nextweekstudent)}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<style scoped>

#header{
    text-align: end;
    font-style: italic;
    font-size: 18px;
}

#tablecontainer{
    display: flex;
    flex-direction: column;
}
</style>