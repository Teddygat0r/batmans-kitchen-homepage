<template>
    <div class="flex mt-6 mb-12">
        <p class="w-[30%] my-auto pb-4">{{ time.toDateString() }}</p>
        <div class="">
            <h1 class="text-white text-2xl font-bold">{{ title }}</h1>
            <h2 class="text-cyan-500">{{ ctf }} | {{ category }}</h2>
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    title: String,
    ctf: String,
    category: String,
    date: Number,
});

const time = new Date(props.date);

</script>

<style lang="scss" scoped>

</style>