<script setup>
import { estado } from './estado'
import PrincipalHeader from './components/PrincipalHeader.vue'
import MenuHeader from './components/MenuHeader.vue'
</script>

<template>
  <div class="min-h-screen flex flex-col bg-fondo">
    <MenuHeader v-if="estado.sesionIniciada" />
    <PrincipalHeader v-else />
    <RouterView />
  </div>
</template>