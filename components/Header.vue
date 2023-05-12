<template>
    <div class="flex justify-around p-4 max-sm:justify-between max-sm:px-12">
        <div class="flex gap-4">
            <a href="/">
                <img
                    src="../assets/static/low-res-logo-lmao.webp"
                    class="w-12 h-12" />
            </a>
            <a href="/" class="m-auto max-sm:hidden">
                <h1 class="text-3xl font-semibold m-auto">Batman's Kitchen</h1>
            </a>
        </div>
        <div class="flex gap-8 text-right">
            <NuxtLink class="m-auto text-lg max-sm:hidden" to="/"
                >Home</NuxtLink
            >
            <NuxtLink class="m-auto text-lg max-sm:hidden" to="/blog"
                >Blog</NuxtLink
            >
            <NuxtLink class="m-auto text-lg max-sm:hidden" to="/about"
                >What We Do</NuxtLink
            >
            <i
                class="hidden max-sm:block m-auto"
                @click="openMenu" :class="menu ? 'ri-close-line':'ri-menu-line'"/>
            <div
                class="absolute flex top-20 w-full h-full bg-black justify-end duration-200 overflow-hidden left-[0%]" :class="menu ? 'opacity-80 z-[10]' : 'opacity-0 z-[-10]'">
                <div class="relative w-[60%] p-4 opacity-100 text-2xl text-white">
                    <div class="p-6 mt-0 border-b border-slate-500 border-opacity-50">
                        <NuxtLink class="m-auto" to="/" @click="openMenu"
                            >Home</NuxtLink
                        >
                    </div>
                    <div class="p-6">
                        <NuxtLink class="m-auto" to="/blog"  @click="openMenu"
                            >Blog</NuxtLink
                        >
                    </div>
                    <div class="p-6">
                        <NuxtLink class="m-auto" to="/about" @click="openMenu"
                            >What We Do</NuxtLink
                        >
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="border-b border-white w-[80%] m-auto"></div>
</template>

<script setup>
const menu = ref(false)
const emit = defineEmits(['disableScroll'])

const openMenu = () => {
    menu.value = !menu.value;
    emit('disableScroll');
};
</script>

<style scoped>

</style>
