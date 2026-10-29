<template>
    <header class="bg-parrafo m-1 p-6 flex items-center justify-between rounded-4xl opacity-85">
        <div class="flex items-center">
            <img src="/favicon.svg" alt="Logo BinSorter" class="h-12 w-12">
            <h1 class="text-xl font-bold p-1">BinSorter A.M.G</h1>
        </div>
        <nav>
            <RouterLink to="/login" class="p-1 text-sm">Iniciar Sesion</RouterLink>
            <RouterLink to="/" class="p-1 text-sm">Registrarse</RouterLink>
        </nav>
    </header>
</template>