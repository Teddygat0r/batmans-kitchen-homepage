<template>
    <div class="flex mt-6 mb-12 max-sm:hidden">
        <p class="w-[30%] my-auto pb-4">{{ date }}</p>
        <div class="flex gap-6">
            <img :src="logo" class="w-16 h-16 rounded-full" />
            <div class="">
                <h1 class="text-white text-2xl font-bold">{{ ctf }}</h1>
                <h2 class="text-cyan-500">{{ convertPlacementToText(placement) }} Place | <NuxtLink :to=desc target="_blank" class="hover:text-cyan-600">{{ desc }}</NuxtLink></h2>
            </div>
        </div>
    </div>
    <div class="mt-6 mb-12 hidden max-sm:flex">
        <img :src="logo" class="w-16 h-16 rounded-full flex-none" />
        <div class="w-full text-center m-auto grow">
            <h1 class="text-white text-xl font-bold"><NuxtLink :to=desc target="_blank" class="hover:text-gray-100">{{ ctf }}</NuxtLink></h1>
            <h2 class="text-cyan-500">{{ convertPlacementToText(placement) }} Place</h2>
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    ctf: String,
    placement: Number,
    data: Object,
});
const date = new Date(props.data.date).toDateString();
const logo = props.data.logo;
const desc = props.data.desc;

const convertPlacementToText = (num) => {
    if(num.slice(-1) == '1') return `${ num }st`;
    else if(num.slice(-1) == '2') return `${ num }nd`;
    else if(num.slice(-1) == '3') return `${ num }rd`;
    else return `${ num }th`
}

onMounted(async () => {});
</script>

<style lang="scss" scoped></style>
