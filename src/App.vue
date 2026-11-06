<script setup>
import { ref } from 'vue';

import PrincipalHeader from './components/PrincipalHeader.vue';
import MenuHeader from './components/MenuHeader.vue';

const SesionIniciada = ref(false);
</script>

<template>
  <div class="min-h-screen flex flex-col bg-fondo">
    <MenuHeader v-if="SesionIniciada" />
    <PrincipalHeader v-else />
    <RouterView />
  </div>
</template>
