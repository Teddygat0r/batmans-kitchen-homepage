<template>
    <div class="w-full h-full overflow-x-hidden">
        <Overlay class="fixed z-10"/>
        <Header />
        <slot/>
        <Footer/>
    </div>
</template>

<script setup>

</script>

<style>

body::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
body {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

</style>