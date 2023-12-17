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
