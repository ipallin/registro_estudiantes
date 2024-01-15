<script setup>
import {ModalType} from "../types.js"
 defineProps({
    confirmaction: Function,
    confirmationparams: Array,
    cancelaction: Function,
    cancelactionparams: Array,
    title:String,
    Text:String,
    messagetype: String,
})
</script>
<template>
    <div>
        <div id="modal" class="modal">
            <div class="modal-content">
                <div id="titlearea">{{ title }}</div>
                <div id="contentarea">{{ Text }}</div>
                <div id="buttonarea">
                    <button class="button" @click="confirmaction(...confirmationparams)">
                        <i class="fa fa-check" aria-hidden="true"></i>
                        {{messagetype == ModalType['warn'] ? 'Si' : 'Ok'}}
                    </button>
                    <button v-show="messagetype == ModalType['warn']" class="button" @click="cancelaction(...cancelactionparams)">
                        <i class="fa fa-ban" aria-hidden="true"></i>
                        No
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
#titlearea{
    display: flex;
    background-color: var(--color-accent);
    color:white;
    height: 25%;
    align-items: center;
    padding-inline: 5%;
    font-size: 1.17em;
    font-weight: bold;
}

#contentarea {
    display: flex;
    height: 40%;
    padding: 1em;
    flex-shrink: 1;
}
</style>