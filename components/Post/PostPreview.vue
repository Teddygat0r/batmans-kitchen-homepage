<template>
    <div class="flex mt-6 mb-12">
        <p class="w-[30%] my-auto pb-4">{{ date }}</p>
        <div class="flex gap-6">
            <img :src="logo" class="w-16 h-16 rounded-full" />
            <div class="">
                <h1 class="text-white text-2xl font-bold">{{ ctf }}</h1>
                <h2 class="text-cyan-500">Place: {{ placement }} | <NuxtLink :to=desc target="_blank" class="hover:text-cyan-600">{{ desc }}</NuxtLink></h2>
            </div>
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    ctf: String,
    placement: String,
    link: String,
});

const date = ref("");
const logo = ref("");
const desc = ref("");

const repeatRequest = async () => {
    const { data } = await useJsonPlaceholderData(props.link, {
        onResponse({ request, response, options }) {
            // Process the response data
            if (!response._data.finish) {
                repeatRequest();
            } else {
                date.value = new Date(response._data.finish).toDateString();
                logo.value = response._data.logo;
                desc.value = response._data.url;
                console.log((new Date()).getTime())
            }
        },
    });
};

repeatRequest();

<<<<<<< Updated upstream
onMounted(async () => {});
=======
onMounted(async () => {
});
>>>>>>> Stashed changes
</script>

<style lang="scss" scoped></style>
