<template>
    <div class="fixed w-full h-full bg-black flex overflow-hidden" id="full-overlay">
        <img src="../assets/static/batman_left.png" class="absolute w-20 top-[50%] duration-300 opacity-0" id="batman-left"/>
        <img src="../assets/static/batman_right.png" class="absolute w-20 top-[50%] duration-300 opacity-0" id="batman-right"/>
        <button class="absolute top-4 right-4 text-2xl" @click="skip">Skip</button>
    </div>
</template>

<script setup>
let velocity = 0;
let opacity = 1;
const ACCELERATION = 0.4;

const skip = () => {
    document.getElementById('batman-left').style.transitionDuration = "0ms";
    document.getElementById('batman-right').style.transitionDuration = "0ms";
    document.getElementById('batman-left').style.visibility = "hidden";
    document.getElementById('batman-right').style.visibility = "hidden";
    document.getElementById('full-overlay').style.visibility = "hidden";
}

onMounted(async() => {
    let marginchange = screen.width / 2 - document.getElementById('batman-left').width / 2;
    const LIMIT = screen.width * 3;

    document.getElementById('batman-left').style.right = marginchange + "px";
    document.getElementById('batman-right').style.left = marginchange + "px";
    document.getElementById('batman-left').style.opacity = "1";
    document.getElementById('batman-right').style.opacity = "1";
    
    await new Promise(r => setTimeout(r, 2000));
    let interval = setInterval(() => {
        marginchange += velocity;
        velocity += ACCELERATION;
        document.getElementById('batman-left').style.right = marginchange + "px";
        document.getElementById('batman-right').style.left = marginchange + "px";

        if(marginchange > LIMIT / 2) {
            document.getElementById('full-overlay').style.opacity = " " + opacity;
            opacity -= 0.01;
        }

        if(marginchange > LIMIT){ 
            document.getElementById('full-overlay').style.visibility = "hidden";
            clearInterval(interval);
        }
    }, 16);
    
});
</script>

<style scoped>

#batman-left{
    transform: translate(-50%, -50%);
}
#batman-right{
    transform: translate(50%, -50%);
}

</style>