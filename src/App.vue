<script setup>
import PrincipalHeader from './components/PrincipalHeader.vue';
</script>

<template>
  <div class="min-h-screen flex flex-col bg-fondo">
    <PrincipalHeader />
    <RouterView />
  </div>
</template>
