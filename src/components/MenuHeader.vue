<template>
    <header class="bg-parrafo m-1 p-6 flex items-center justify-between rounded-4xl opacity-85">
        <div class="flex items-center">
            <img src="/logo.svg" alt="Logo BinSorter" class="h-24 w-24">
        </div>
        <nav>
            <RouterLink to="/home" class="p-1 text-sm">Inicio</RouterLink>
            <RouterLink to="/escaner" class="p-1 text-sm">Escaner</RouterLink>
            <RouterLink to="/" class="p-1 text-sm">Perfil</RouterLink>
        </nav>
    </header>
</template>