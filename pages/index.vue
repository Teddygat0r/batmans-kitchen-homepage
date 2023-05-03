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
import { parse } from "node-html-parser";

definePageMeta({
    layout: "home-overlay",
});
const posts = ref([]);

const { data } = useFetch("https://ctftime.org/team/3135");

onMounted(async () => {
    console.log((new Date()).getTime())
    const soup = parse(data.value);
    const children = soup.childNodes[1].querySelector(
        `#rating_${new Date().getFullYear()}`
    ).childNodes[4];

    let counter = 0;
    for (const child of children.childNodes) {
        if (child.tagName && child.childNodes.length == 5) {
            if(counter == 5) break;
            counter++;

            posts.value.push({
                ctf: child.childNodes[2].innerText,
                placement: child.childNodes[1].innerText,
                link: `events/${child.childNodes[2].childNodes[0].attrs['href'].substring(7)}/`,
            });
        }
    }
});
</script>

<style lang="scss" scoped></style>
