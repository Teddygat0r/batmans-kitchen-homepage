<template>
<<<<<<< Updated upstream
    <div class="w-full min-h-screen h-full">
        <Header />
=======
    <div class="w-full h-full overflow-x-hidden" :class="disableScroll ? 'overflow-y-hidden h-screen-border':''">
        <Header @disableScroll="disableScroll = !disableScroll"/>
>>>>>>> Stashed changes
        <slot />
        <Footer/>
    </div>
</template>

<script setup>
const disableScroll = ref(false);

</script>

<style scoped>

.h-screen-border {
    height: calc(100vh - 3px);
}

</style>