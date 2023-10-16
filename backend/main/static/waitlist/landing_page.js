gsap.registerPlugin(ScrollTrigger);

let tl = gsap.timeline({ defaults: { ease: "power1.inOut" } });

tl.from("h1", {
    opacity: 0,
    y: 50,
    scale: 0.8,
    duration: 1,
    onStart() {
        $("body").css("overflow-y", "hidden");
    }
})
    .from(
        "h3",
        {
            opacity: 0,
            y: 30,
            duration: 0.7
        },
        "+=0.3"
    )
    .from(
        "form",
        {
            opacity: 0,
            y: 30,
            scale: 0.95,
            duration: 0.6,
            onComplete() {
                $("body").css("overflow-y", "auto");
            }
        },
        "<30%"
    );

/*tl.from("#sponsors", {
    x: "-100vw",
    scrollTrigger: {
        trigger: "#sponsor-wrap",
        start: "top bottom",
        end: "+=40%",
        scrub: true,
        markers: false,
        once: true
    }
});*/

let figures = $("#sponsors").get(0).children;

for (let i = 0; i < figures.length; i++) {
    const figure = figures[i];
    tl.from(figure, {
        x: "-100vw",
        scrollTrigger: {
            trigger: "#sponsor-wrap",
            start: 50 + i * 10 + "% bottom",
            end: "+=25%",
            scrub: true,
            markers: false,
            once: true
        }
    });
}

let quotetexts = $("#quote-text p").get(0).children;

for (let i = 0; i < quotetexts.length; i++) {
    const quotetext = quotetexts[i];
    tl.from(quotetext, {
        y: -50,
        opacity: 0,
        scrollTrigger: {
            trigger: quotetext,
            start: "bottom bottom",
            end: "+=15%",
            scrub: true,
            markers: false
        }
    });
}

tl.from("#introducing h5", {
    y: -50,
    opacity: 0,
    scale: 0.9,
    scrollTrigger: {
        trigger: "#introducing h5",
        start: "bottom bottom",
        end: "+=250",
        once: true,
        scrub: true,
        markers: false
    }
});

tl.from("#introducing h2", {
    y: -50,
    opacity: 0,
    scale: 0.9,
    scrollTrigger: {
        trigger: "#introducing h2",
        start: "bottom bottom",
        end: "+=250",
        once: true,
        scrub: true,
        markers: false
    }
});

tl.from(".product-box", {
    opacity: 0,
    scrollTrigger: {
        trigger: "#product-boxes",
        start: "center bottom",
        end: "+=50",
        once: true,
        scrub: true,
        markers: false
    }
});
