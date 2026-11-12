<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { estado } from '../estado'

const router = useRouter()

const correo = ref('')
const password = ref('')
const error = ref('')

const campo =
  'border-2 border-gray-300 rounded-lg p-2 outline-none placeholder:text-gray-400 ' +
  'focus:border-importante focus:bg-importante/10'

function iniciarSesion() {
  // Por ahora solo diseño: tu compañero conectará la validación real
  error.value = ''
  estado.sesionIniciada = true
  router.push('/home')
}
</script>

<template>
  <main class="flex-1 flex items-center justify-center p-4">
    <div class="bg-contenedor rounded-xl shadow p-6 w-full max-w-md">
      <h2 class="text-2xl font-bold text-importante mb-4">Iniciar sesión</h2>

      <form class="flex flex-col gap-4" @submit.prevent="iniciarSesion">
        <div class="flex flex-col gap-1">
          <label for="correo" class="text-sm font-semibold">Correo institucional</label>
          <input id="correo" v-model="correo" type="email" placeholder="ejemplo@unilasallista.edu.co" required :class="campo" />
          <p class="text-xs text-gray-500">Usa el correo con el que te registraste.</p>
        </div>

        <div class="flex flex-col gap-1">
          <label for="password" class="text-sm font-semibold">Contraseña</label>
          <input id="password" v-model="password" type="password" placeholder="Tu contraseña" required :class="campo" />
          <p v-if="error" class="text-xs text-red-600">{{ error }}</p>
          <p v-else class="text-xs text-gray-500">La que creaste al registrarte.</p>
        </div>

        <button type="submit" class="bg-importante text-white rounded-lg py-2 font-semibold hover:opacity-90">
          Entrar
        </button>

        <p class="text-sm text-center text-gray-600">
          ¿No tienes cuenta?
          <RouterLink to="/register" class="font-semibold text-importante">Regístrate</RouterLink>
        </p>
      </form>
    </div>
  </main>
</template>