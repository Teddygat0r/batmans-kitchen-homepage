<template>
    <div class="w-[80%] m-auto">
        <MainBanner />
        <div class="border-b border-gray-600 m-auto"></div>
        <PostPreview
            v-for="post in posts"
            :key="post.id"
            v-bind="post"
            class="m-8" />
    </div>
</template>

<script setup>
definePageMeta({
    layout: "home-overlay",
});

useHead({
    title: "Home | Batman's Kitchen",
    meta: [{ name: "Homepage", content: "Homepage for Batman's Kitchen, University of Washington's CTF Team" }],
});

const posts = ref([]);
$fetch("/ctf_data/ctf_data.json").then((data) => {
    posts.value = data.ctfs;
});
</script>

<style lang="scss" scoped></style>
