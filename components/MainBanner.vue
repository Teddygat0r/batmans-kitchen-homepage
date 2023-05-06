<template>
    <div class="w-full flex flex-col">
        <div class="m-auto my-8 pr-60 max-sm:pr-0">
            <div class="min-w-min w-[60%] flex flex-col m-auto">
                <p class="m-auto text-lg tracking-wide">
                    <span class="text-white text-3xl font-bold max-sm:text-xl">
                        University of Washington's<br />
                    </span>
                    <span class="text-justify max-sm:text-base">
                        cybersecurity team! We compete against other nationally
                        ranked teams in online capture the flag events.
                        <span class="max-sm:hidden">
                            In addition, we hold workshops to teaching
                            exploitation techniques in a wide variety of
                            categories: web, binary, cryptography - you name it,
                            we do it!
                        </span>
                    </span>
                </p>

                <div class="flex gap-4 my-4">
                    <NuxtLink
                        class="bg-stone-400 text-white px-2 py-1 rounded-lg"
                        to="https://discord.com/invite/u9USAb3PF7"
                        target="_blank"
                        rel="noopener">
                        <div class="flex m-auto">
                            <p class="m-auto">Discord</p>
                            <i class="ri-discord-fill ml-1 m-auto" />
                        </div>
                    </NuxtLink>

                    <NuxtLink
                        class="bg-stone-400 text-white px-2 py-1 rounded-lg"
                        to="https://www.instagram.com/uw.batmanskitchen/"
                        target="_blank"
                        rel="noopener">
                        <div class="flex m-auto">
                            <p class="m-auto">Instagram</p>
                            <i class="ri-instagram-line ml-1 m-auto" />
                        </div>
                    </NuxtLink>
                    <NuxtLink
                        class="bg-stone-400 text-white px-2 py-1 rounded-lg"
                        to="https://ctftime.org/team/3135"
                        target="_blank"
                        rel="noopener">
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
