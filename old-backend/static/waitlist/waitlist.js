$("document").ready(function () {
    $("#boxes").scrollLeft($("#boxes").width() / 2);

    gsap.registerPlugin(ScrollTrigger);

    $(window).scrollTop(0);

    var tl = gsap.timeline({ defaults: { duration: 0.7 } });

    tl.from("header h1", {
        delay: 0.4,
        opacity: 0,
        scale: 0.95,
        y: -20,
        duration: 0.2
    });

    tl.from("header h2", {
        delay: 0.3,
        opacity: 0,
        scale: 0.9,
        y: -20
    });

    tl.from(
        "form",
        {
            opacity: 0,
            scale: 0.9,
            y: -20
        },
        "<30%"
    );

    tl.from(".arrow > *", {
        y: -25,
        opacity: 0,
        ease: "power2.out"
    });

    tl.to(".arrow", {
        opacity: 0,
        y: 25,
        scrollTrigger: {
            trigger: "header",
            start: "90.9% bottom",
            end: "+=100",
            scrub: true
        }
    });

    gsap.fromTo(
        "#box-1",
        {
            scale: 0.75
        },
        {
            scale: 0.9,
            scrollTrigger: {
                scroller: "#boxes",
                trigger: "#boxes",
                start: "0% left",
                end: "+=60%",
                horizontal: true,
                scrub: true,
                snap: {
                    snapTo: 1,
                    duration: { min: 0.2, max: 0.5 },
                    delay: 0
                }
            }
        }
    );

    gsap.fromTo(
        "#box-1",
        {
            scale: 0.9
        },
        {
            scale: 0.75,
            scrollTrigger: {
                scroller: "#boxes",
                trigger: "#boxes",
                start: "160% right",
                end: "+=60%",
                horizontal: true,
                scrub: true,
                snap: {
                    snapTo: 1,
                    duration: { min: 0.2, max: 0.5 },
                    delay: 0
                }
            }
        }
    );

    gsap.fromTo(
        "#box-2",
        {
            scale: 0.9
        },
        {
            scale: 0.75,
            scrollTrigger: {
                scroller: "#boxes",
                trigger: "#boxes",
                start: "0% left",
                end: "+=60%",
                horizontal: true,
                scrub: true
            }
        }
    );
    gsap.fromTo(
        "#box-3",
        {
            scale: 0.75
        },
        {
            scale: 0.9,
            scrollTrigger: {
                scroller: "#boxes",
                trigger: "#boxes",
                start: "160% right",
                end: "+=60%",
                horizontal: true,
                scrub: true
            }
        }
    );
});
