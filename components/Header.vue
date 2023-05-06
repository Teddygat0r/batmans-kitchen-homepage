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
            <NuxtLink class="m-auto text-lg max-sm:hidden" to="/blog"
                >Blog</NuxtLink
            >
            <NuxtLink class="m-auto text-lg max-sm:hidden" to="#"
                >Filler</NuxtLink
            >
            <NuxtLink class="m-auto text-lg max-sm:hidden" to="/about"
                >What We Do</NuxtLink
            >
            <i
                class="hidden max-sm:block m-auto"
                @click="openMenu" :class="menu ? 'ri-close-line':'ri-menu-line'"/>
            <div
                class="absolute top-20 w-full h-full bg-black opacity-50 justify-end duration-500 overflow-hidden" :class="menu ? 'flex left-[0%]' : 'left-[200%]'">
                <div class="relative w-[60%] p-4">
                    <div>
                        <NuxtLink class="m-auto text-lg" to="/blog"
                            >Blog</NuxtLink
                        >
                    </div>
                    <div>
                        <NuxtLink class="m-auto text-lg" to="#"
                            >Filler</NuxtLink
                        >
                    </div>
                    <div>
                        <NuxtLink class="m-auto text-lg" to="/about"
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

<style lang="scss" scoped></style>
