<template>
    <div class="w-[80%] m-auto">
        <MainBanner />
        <div class="border-b border-gray-600 m-auto"></div>
        <PostPreview v-for="post in posts" :key="post.id" v-bind="post" class="m-8"/>
    </div>
</template>

<script setup>

definePageMeta({
  layout: "home-overlay",
});
const posts = [
    {
        title: "fake ctf - no 1",
        ctf: "fake ctf",
        category: "web",
        date: 1682236890589,
    },
    {
        title: "fake ctf - no 2",
        ctf: "fake ctf",
        category: "i stole this design from sekai.team",
        date: 1682236890540,
    },
];
</script>

<style lang="scss" scoped></style>
