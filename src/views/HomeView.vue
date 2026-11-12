<script setup>
import { estado } from '../estado'

const pasos = [
  { n: '1', titulo: 'Regístrate', texto: 'Crea tu cuenta con tu correo institucional.' },
  { n: '2', titulo: 'Escanea', texto: 'Apunta la cámara al residuo que quieres desechar.' },
  { n: '3', titulo: 'Aprende', texto: 'La IA te dice en qué caneca va y por qué.' },
]

const canecas = [
  { color: 'bg-green-700 text-white', nombre: 'Verde', texto: 'Residuos orgánicos: restos de comida y material vegetal.' },
  { color: 'bg-white text-neutral-900 border-2 border-neutral-400', nombre: 'Blanca', texto: 'Aprovechables: plástico, papel, cartón, vidrio y metal.' },
  { color: 'bg-neutral-900 text-white', nombre: 'Negra', texto: 'No aprovechables: servilletas sucias, icopor y similares.' },
]

const equipo = [
  'Juan Pablo Gómez Carmona',
  'Juan Fernando Mejia Alvarez',
  'Cristian Duque Lenis',
  'Santiago Munera Rave',
  'Juan Pablo Bedoya Arango',
]

const asesores = ['Jonathan Berthel Castro', 'Feibert Alirio Gúzman']
</script>

<template>
  <div class="flex-1">
    <!-- Portada -->
    <section class="bg-importante text-white px-4 py-16 text-center">
      <h1 class="text-4xl md:text-6xl font-bold">BinSorter A.M.G</h1>
      <p class="mt-4 text-lg md:text-2xl text-parrafo">Escanea, clasifica y transforma el campus</p>
      <RouterLink
        :to="estado.sesionIniciada ? '/escaner' : '/register'"
        class="inline-block mt-8 bg-primario text-white font-semibold rounded-lg px-8 py-3 hover:opacity-90"
      >
        {{ estado.sesionIniciada ? 'Ir al escáner' : 'Empieza ahora' }}
      </RouterLink>
    </section>

    <!-- Problema y objetivos -->
    <section class="max-w-4xl mx-auto px-4 py-12">
      <h2 class="text-3xl font-bold text-importante mb-4">Nuestro propósito</h2>
      <p class="text-white text-lg">
        Muchas veces no sabemos en qué caneca va cada residuo, y eso afecta la limpieza del campus.
        BinSorter motiva a los estudiantes a desechar bien la basura y a aprender dónde va cada cosa,
        porque cuidar el campus es un deber de todos.
      </p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
        <div class="bg-contenedor rounded-xl p-5">
          <h3 class="font-bold text-importante">ODS 4 · Educación de calidad</h3>
          <p class="text-sm mt-1">Aprendes a clasificar residuos mientras usas la app.</p>
        </div>
        <div class="bg-contenedor rounded-xl p-5">
          <h3 class="font-bold text-importante">ODS 11 · Ciudades y comunidades sostenibles</h3>
          <p class="text-sm mt-1">Promovemos un campus más limpio y responsable.</p>
        </div>
      </div>
    </section>

    <!-- Cómo funciona -->
    <section class="bg-primario px-4 py-12">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-3xl font-bold text-white mb-6">¿Cómo funciona?</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div v-for="p in pasos" :key="p.n" class="bg-contenedor rounded-xl p-5">
            <span class="text-3xl font-bold text-importante">{{ p.n }}</span>
            <h3 class="font-bold mt-1">{{ p.titulo }}</h3>
            <p class="text-sm mt-1">{{ p.texto }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Canecas -->
    <section class="max-w-4xl mx-auto px-4 py-12">
      <h2 class="text-3xl font-bold text-importante mb-6">Las tres canecas</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div v-for="c in canecas" :key="c.nombre" :class="c.color" class="rounded-xl p-5 shadow">
          <h3 class="font-bold text-xl">{{ c.nombre }}</h3>
          <p class="text-sm mt-1">{{ c.texto }}</p>
        </div>
      </div>
    </section>

    <!-- Equipo -->
    <section class="bg-importante text-white px-4 py-12">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-3xl font-bold mb-6">Equipo</h2>
        <h3 class="font-semibold text-parrafo mb-2">Desarrolladores</h3>
        <ul class="grid grid-cols-1 md:grid-cols-2 gap-1 mb-6">
          <li v-for="e in equipo" :key="e">{{ e }}</li>
        </ul>
        <h3 class="font-semibold text-parrafo mb-2">Asesores</h3>
        <ul class="mb-6">
          <li v-for="a in asesores" :key="a">{{ a }}</li>
        </ul>
        <p class="text-sm text-parrafo">Desarrollado con la ayuda de Claude Sonnet 5.5.</p>
      </div>
    </section>
  </div>
</template>