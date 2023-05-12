<template>
    <div class="w-[80%] m-auto">
        <div class="w-[50%] m-auto text-lg font-medium max-sm:w-[80%] max-sm:text-base max-sm:text-center">
            <br />
            <h1 class="font-bold text-2xl text-center mb-2">Our Goals</h1>
            <p>
                Our primary goal is to foster an active, interesting community
                to
                <span class="font-bold text-cyan-200"
                    >learn and discuss security principles</span
                >
                at the Univeristy of Washington.
            </p>
            <br />
            <p>
                We aim to create an environment welcoming to all ranges of
                experience - whether you're a veteran in the field or haven't
                the foggiest about security, join us! Everyone is welcome!
                Regardless of prior experience, you'll have a good time.
            </p>
            <br />

            <h1 class="font-bold text-2xl text-center my-2">
                But... What is a CTF?
            </h1>
            <p>
                CTFs or
                <span class="font-bold text-cyan-200">Capture The Flag</span>
                competitions are online security/hacking events. Teams compete
                to find and exploit the most vulnerabilities in various
                challenges.
            </p>
            <br />
            <p>
                There are a plethora of beginner-friendly CTFs, and even some of
                the more advanced competitions have one or two challenges geared
                towards people with little to no experience! For more
                information, a great resource to check out is
                <NuxtLink
                    to="https://ctf101.org/"
                    target="_blank"
                    rel="noopener"
                    class="font-bold text-cyan-400 hover:text-cyan-500"
                    >ctf101.org</NuxtLink
                >.
            </p>
            <br />
            <h1 class="font-bold text-2xl text-center my-2">Join Us!</h1>
            <p>
                Whether you want to compete in CTFs with us or just learn about
                how to break stuff, feel free to join us on
                <NuxtLink
                    to="https://discord.com/invite/u9USAb3PF7"
                    target="_blank"
                    rel="noopener"
                    class="font-bold text-cyan-400 hover:text-cyan-500"
                    >Discord</NuxtLink
                >. We meet
                <span class="font-bold text-cyan-200"
                    >Wednesdays from 5-7 PM</span
                >, and occasionally on Friday afternoons for CTFs and other
                events.
            </p>
            <br />
            <br />
        </div>
    </div>
</template>

<script setup>

useHead({
    title: "About | Batman's Kitchen",
    meta: [{ name: "About", content: "About page, has team & CTF information." }],
});

</script>

<style lang="scss" scoped></style>
