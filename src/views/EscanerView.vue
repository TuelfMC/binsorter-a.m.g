//empiece acá el frontend del escaner bb
<script setup>
import { ref, onBeforeUnmount } from 'vue'

const API_URL = location.hostname.endsWith('trycloudflare.com')
  ? '/api'
  : 'http://localhost:8000'

const video = ref(null)
const canvas = ref(null)
const fase = ref('inactivo') // inactivo | listo | analizando | resultado
const resultado = ref(null)
const mensaje = ref('')
let stream = null

async function activarCamara() {
  mensaje.value = ''
  if (!navigator.mediaDevices?.getUserMedia) {
    mensaje.value = 'Este navegador no permite usar la cámara (requiere HTTPS o localhost).'
    return
  }
  try {
    stream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: { ideal: 'environment' } },
      audio: false,
    })
    video.value.srcObject = stream
    await video.value.play()
    fase.value = 'listo'
  } catch (e) {
    mensaje.value =
      e.name === 'NotAllowedError'
        ? 'Permiso de cámara denegado. Actívalo en el navegador.'
        : 'No se pudo acceder a la cámara.'
  }
}

async function capturar() {
  const v = video.value
  if (!v || !v.videoWidth) return
  mensaje.value = ''

  // Recorte cuadrado central: lo mismo que el usuario ve en pantalla
  const lado = Math.min(v.videoWidth, v.videoHeight)
  const sx = (v.videoWidth - lado) / 2
  const sy = (v.videoHeight - lado) / 2
  const c = canvas.value
  c.width = 512
  c.height = 512
  c.getContext('2d').drawImage(v, sx, sy, lado, lado, 0, 0, 512, 512)

  fase.value = 'analizando'
  const blob = await new Promise((r) => c.toBlob(r, 'image/jpeg', 0.9))
  if (!blob) {
    mensaje.value = 'No se pudo capturar la imagen.'
    fase.value = 'listo'
    return
  }
  const form = new FormData()
  form.append('imagen', blob, 'captura.jpg')

  try {
    const resp = await fetch(`${API_URL}/predict`, { method: 'POST', body: form })
    if (!resp.ok) {
      const err = await resp.json().catch(() => ({}))
      throw new Error(err.detail || `Error ${resp.status}`)
    }
    resultado.value = await resp.json()
    fase.value = 'resultado'
  } catch (e) {
    mensaje.value =
      e instanceof TypeError ? 'No se pudo conectar con el servicio de IA.' : e.message
    fase.value = 'listo'
  }
}

function reescanear() {
  resultado.value = null
  mensaje.value = ''
  fase.value = 'listo'
}

onBeforeUnmount(() => {
  stream?.getTracks().forEach((t) => t.stop())
  stream = null
})

const porcentaje = (x) => `${Math.round(x * 100)} %`
</script>

<template>
  <main class="flex-1 flex items-center justify-center p-4">
    <div class="bg-contenedor rounded-xl shadow p-6 w-full max-w-md flex flex-col gap-4">
      <h2 class="text-2xl font-bold text-importante">Escáner de botellas</h2>

      <div class="relative aspect-square overflow-hidden rounded-lg bg-black">
        <video ref="video" playsinline muted class="h-full w-full object-cover"></video>
        <div v-if="fase === 'inactivo'" class="absolute inset-0 grid place-items-center text-sm text-white/80">
          La cámara está apagada
        </div>
        <div v-if="fase === 'listo'" class="pointer-events-none absolute inset-6 rounded-lg border-2 border-white/70"></div>
      </div>
      <canvas ref="canvas" class="hidden"></canvas>

      <button v-if="fase === 'inactivo'" @click="activarCamara"
        class="bg-importante text-white rounded-lg py-2 font-semibold hover:opacity-90">
        Activar cámara
      </button>
      <button v-if="fase === 'listo'" @click="capturar"
        class="bg-importante text-white rounded-lg py-2 font-semibold hover:opacity-90">
        Capturar y analizar
      </button>
      <p v-if="fase === 'analizando'" class="text-center text-gray-600">Analizando…</p>

      <div v-if="fase === 'resultado' && resultado"
        class="flex flex-col gap-2 rounded-lg border-2 border-gray-300 p-4">
        <template v-if="resultado.resultado === 'botella_plastica'">
          <p class="text-lg font-bold text-green-700">Botella plástica detectada</p>
          <p>Confianza: {{ porcentaje(resultado.confianza) }}</p>
          <p>Deposítala en la <strong>caneca blanca</strong>.</p>
        </template>
        <template v-else-if="resultado.resultado === 'no_botella'">
          <p class="text-lg font-bold">No parece una botella plástica</p>
          <p>Confianza: {{ porcentaje(resultado.confianza) }}</p>
        </template>
        <template v-else>
          <p class="text-lg font-bold text-amber-700">No pude identificarlo</p>
          <p>Prueba con mejor luz y encuadrando solo el objeto.</p>
        </template>
        <button @click="reescanear"
          class="border-2 border-gray-300 rounded-lg py-2 font-semibold hover:bg-gray-100">
          Volver a escanear
        </button>
      </div>

      <p v-if="mensaje" class="text-sm text-error">{{ mensaje }}</p>
    </div>
  </main>
</template>