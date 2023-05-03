<template>
    <div class="flex justify-around p-4">
        <div class="flex gap-4">
            <a href="/" >
                <img
                    src="../assets/static/low-res-logo-lmao.webp"
                    class="w-12" />
            </a>
            <a href="/" class="m-auto">
                <h1 class="text-3xl font-semibold m-auto">Batman's Kitchen</h1>
            </a>
        </div>
        <div class="flex gap-8">
            <NuxtLink class="m-auto text-lg" to="/blog">Blog</NuxtLink>
            <NuxtLink class="m-auto text-lg" to="#">Filler</NuxtLink>
            <NuxtLink class="m-auto text-lg" to="/about">What We Do</NuxtLink>
        </div>
    </div>
    <div class="border-b border-white w-[80%] m-auto"></div>
</template>

<script setup></script>

<style lang="scss" scoped></style>
