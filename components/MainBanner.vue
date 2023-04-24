<template>
    <div class="w-full flex flex-col">
        <div class="m-auto my-8 pr-60">
            <div class="min-w-min w-[60%] flex flex-col m-auto">
                <p class="m-auto text-lg tracking-wide">
                    <span class="text-white text-3xl font-bold">
                        University of Washington's<br />
                    </span>
                    <span class="text-justify">
                        cybersecurity team! We compete against other nationally
                        ranked teams in online capture the flag events. In
                        addition, we hold workshops to teaching exploitation
                        techniques in a wide variety of categories: web, binary,
                        cryptography - you name it, we do it!
                    </span>
                </p>

                <div class="flex gap-4 my-4">
                    <NuxtLink
                        class="bg-stone-400 text-white px-2 py-1 rounded-lg"
                        href="#">
                        <div class="flex m-auto">
                            <p class="m-auto">Discord</p> <i class="ri-discord-fill ml-1 m-auto" />
                        </div>
                    </NuxtLink>

                    <NuxtLink
                        class="bg-stone-400 text-white px-2 py-1 rounded-lg"
                        href="#">
                        <div class="flex m-auto">
                            <p class="m-auto">Instagram</p> <i class="ri-instagram-line ml-1 m-auto" />
                        </div>
                    </NuxtLink>
                    <NuxtLink
                        class="bg-stone-400 text-white px-2 py-1 rounded-lg"
                        href="#">
                        <div class="flex m-auto">
                            <p class="m-auto">CTFTime</p>
                        </div>
                    </NuxtLink>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup></script>

<style lang="scss" scoped></style>
