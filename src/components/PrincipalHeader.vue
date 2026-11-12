<template>
    <header class="bg-parrafo m-1 p-1 flex items-center justify-between rounded-4xl opacity-85">
        <div class="flex items-center">
            <img src="/logo.svg" alt="Logo BinSorter" class="h-24 w-24">
        </div>
        <nav>
            <RouterLink to="/login" class="p-1 text-sm">Iniciar Sesion</RouterLink>
            <RouterLink to="/register" class="p-1 text-sm">Registrarse</RouterLink>
        </nav>
    </header>
</template>