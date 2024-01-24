<script setup>
    import {ref, onMounted, computed, onUnmounted} from "vue"
    import {get_Current_Students} from "../apiservice"

    const date = ref()
    const interval = ref()
    const stlist = ref(new Array)

    const morning = computed(()=>{
            return stlist.value.filter((alum) => { return alum.shift =="Mañana"}).length
        }
    )
    const afternoon = computed(()=>{
            return stlist.value.filter((alum) => { return alum.shift =="Tarde"}).length
        }
    )
    const fullday = computed(()=>{
            return stlist.value.filter((alum) => { return alum.shift =="Intensivo"}).length
        }
    )

    const total = computed(()=>{
        return morning.value + afternoon.value + fullday.value
    })

    onMounted(async () => {
        stlist.value = await get_Current_Students()
        interval.value = setInterval (()=>{
            date.value = new Date(Date.now()).toLocaleString()
        }, 1000)
    })

    onUnmounted(()=>{
        clearInterval(interval.value);
    })
</script>
<template>
    <div id="header">
        {{ date }}
    </div>
    <div id="tablecontainer">
        <table>
            <thead>
                <tr>
                    <th> Turno</th>
                    <th> Nº de alumnos</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th> Mañana</th>
                    <td> {{morning}}</td>
                </tr>
                <tr>
                    <th> Tarde</th>
                    <td> {{afternoon}}</td>
                </tr>
                <tr>
                    <th> Intensivo</th>
                    <td> {{fullday}}</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <th colspan="2"> Total: {{total}}</th>
                </tr>
            </tfoot>
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
    justify-items: center;
    justify-content: center;
    margin-top: 10%;
}
</style>