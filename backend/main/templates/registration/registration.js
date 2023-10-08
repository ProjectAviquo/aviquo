let tl = gsap.timeline({
    delay: 0.5,
    defaults: {
        duration: 1
    }
});

let appHeight = document.getElementById("App").clientHeight;

tl.to(
    "#App", {
    duration: 0,
    y: -50,
    height: 0
}
);

tl.to(
    "#App", {
    y: 0,
    opacity: 1,
    height: appHeight
}
);

tl.to(
    "h2", {
    duration: 0.3,
    opacity: 1
}, "<+0.4"
);

let formChild = document.getElementsByTagName("form")[0].children;

for (let i = 0; i < formChild.length; i++) {
    const cur_label = formChild[i];

    tl.to(
        cur_label, {
        duration: 0.2,
        opacity: 1
    }, "<50%"
    );
}
/* Looks ugly

function getRandomNumber(min, max) {
    return Math.random() * (max - min) + min;
}

const radialGradients = [];
const amt = 10;

for (let i = 0; i < amt; i++) {
    const x = getRandomNumber(0, 100);
    const y = getRandomNumber(0, 100);

    radialGradients.push(
        "radial-gradient(circle at " +
        getRandomNumber(i*(100/amt), (i+1)*(100/amt)) +
        "% " +
        getRandomNumber(0, 100) +
        "%, #FFFAFA40 " +
        getRandomNumber(3/5, 4/5) +
        "%, transparent " +
        getRandomNumber(6/5, 7/5) +
        "%)"
    );
}

const bodyDiv = document.getElementById("body");
bodyDiv.style.background = radialGradients.join(", ") + ", repeating-linear-gradient(90deg, #fdb9db, #E5D1FF, rgb(219, 202, 214), #fdb9db 25%)";
*/
