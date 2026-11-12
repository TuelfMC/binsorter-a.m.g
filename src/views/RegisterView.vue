<script setup>

import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { estado } from '../estado'

const router = useRouter()

const nombres = ref('')
const apellidoPaterno = ref('')
const apellidoMaterno = ref('')
const correo = ref('')
const password = ref('')
const confirmacion = ref('')
const error = ref('')

const campo = 
  'border-2 border-gray-300 rounded-lg p-2 outline-none placeholder:text-gray-400 ' +  'focus:border-primario focus:bg-parrafo/20'

function registrar(){
    if (password.value.length < 8){
        error.value = 'La contraseña debe tener minimo 8 caracteres'
        return
    }
    if (!/[A-Z]/.test(password.value)){
        error.value = 'La contraseña debe tener almenos una mayuscula'
        return
    }
    if (!/[0-9]/.test){
        error.value = 'La contraseña debe tener almenos un numero'
        return
    }
    if (password.value !== confirmacion.value){
        error.value = 'las contraseñas deben coincidir'
        return
    }
    error.value = ''
    estado.sesionIniciada = true
    router.push('/HomeView.vue')
}

</script>

<template>
    <main class="flex-1 flex items-center justify-center p-4">
        <div class="bg-contenedor rounded-xl shadow p-6 w-full max-w-md">
            <h2 class="text-2xl font-bold text-principal mb-4">Crear cuenta</h2>

            <form class="flex flex-col gap-4" @submit.prevent="registrar">
                <div class="flex flex-col gap-1">
                    <label for="nombres" class="text-sm font-semibold">Nombre(s)</label>
                    <input id="nombres" v-model="nombres" type="text" placeholder="Maria José" required :class="campo" />
                </div>

                <div class="flex flex-col gap-1">
                    <label for="paterno" class="text-sm font-semibold">Apellido paterno</label>
                    <input id="paterno" v-model="apellidoPaterno" type="text" placeholder="Fernandez" required :class="campo" />
                </div>

                <div class="flex flex-col gap-1">
                    <label for="materno" class="text-sm font-semibold">Apellido materno <span class="font-normal text-gray-500">(opcional)</span></label>
                    <input id="materno" v-model="apellidoMaterno" type="text" placeholder="Martinez" :class="campo" />
                </div>

                <div class="flex flex-col gap-1">
                    <label for="correo" class="text-sm font-semibold">Correo institucional</label>
                    <input id="correo" v-model="correo" type="email" placeholder="ejemplo@unilasallista.edu.co" required :class="campo" />
                </div>

                <div class="flex flex-col gap-1">
                    <label for="password" class="text-sm font-semibold">Contraseña</label>
                    <input id="password" v-model="password" type="password" placeholder="Mínimo 8 caracteres" minlength="8" required :class="campo" />
                    <p class="text-xs text-gray-500">8 caracteres, una mayuscula, un numero.</p>
                </div>

                <div class="flex flex-col gap-1">
                    <label for="confirmacion" class="text-sm font-semibold">Confirmar contraseña</label>
                    <input id="confirmacion" v-model="confirmacion" type="password" placeholder="Repite la contraseña" required :class="campo" />
                    <p v-if="error" class="text-xs text-error">{{ error }}</p>
                    <p v-else class="text-xs text-gray-500">Debe ser igual a la anterior.</p>
                </div>

                 <button type="submit" class="bg-importante text-white rounded-lg py-2 font-semibold hover:bg-principal-oscuro">
                    Registrarme
                </button>
            </form>
        </div>
    </main>
</template>