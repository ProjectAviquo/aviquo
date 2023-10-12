let tl = gsap.timeline({
    defaults: {
        duration: 0.2
    }
});

gsap.registerPlugin(EaselPlugin);
gsap.registerPlugin(ScrollToPlugin);
gsap.registerPlugin(ScrollTrigger);

function join_the_soviet_union() {
    tl.clear();
    tl.to("#wl-submit", {
        filter: "hue-rotate(0deg)",
        duration: 0
    });
    tl.to(window, { duration: 0.5, scrollTo: "#App" });
    tl.to("#wl-email", {
        scale: 1.2,
        ease: "power2.out"
    });
    tl.to("#wl-email", {
        scale: 1,
        ease: "power2.out"
    });
    tl.to("#wl-submit", {
        scale: 1.2,
        ease: "power2.out"
    });
    tl.to(
        "#wl-submit",
        {
            filter: "hue-rotate(360deg)",
            duration: 0.5
        },
        "<"
    );
    tl.to(
        "#wl-submit",
        {
            scale: 1,
            ease: "power2.out"
        },
        "<0.15"
    );
}

$("header > *").css("opacity", "0");
$("header > *").css("transform", "translate(0, -20px)");
$("#sponsors").css("opacity", "0");
$("#sponsors").css("transform", "translate(0, 40px)");
$("#sponsors aside").css("transform", "translate(-100vw, 0)");
$("#quote-text p > span").css("opacity", "0");
$("#quote-text p > span").css("transform", "translate(0, -40px)");
$("#introducing > *").css("opacity", "0");
$("#introducing > *").css("transform", "translate(0, -40px)");

var fadeTl = gsap.timeline({ defaults: { duration: 1, ease: "power2.out" } });

fadeTl.to("h1", { opacity: 1, delay: 0.3, y: 0 });
fadeTl.to("header h3", { opacity: 1, y: 0 }, "<30%");
fadeTl.to("form", { opacity: 1, y: 0 }, "<30%");
fadeTl.to("#sponsors", { opacity: 1, y: 0, duration: 0.7 }, "<30%");
fadeTl.to("#sponsors aside", { x: 0 }, "<-0.4");

var quotelines = document.querySelectorAll("#quote-text > p > *");
for (let i = 0; i < quotelines.length; i++) {
    const element = quotelines[i];
    if (element.tagName == "BR") {
        continue;
    }
    fadeTl.to(element, { opacity: 1, y: 0 }, "<20%");
}

fadeTl.to(element)