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
var fadeTl = gsap.timeline({ defaults: { duration: 1, ease: "power2.out" } });

fadeTl.from("h1", { opacity: 0, delay: 0.3, y: -20 });
fadeTl.from("header h3", { opacity: 0, y: -20 }, "<30%");
fadeTl.from("form", { opacity: 0, y: -20 }, "<30%");
fadeTl.from("#sponsors", { opacity: 0, y: -20, duration: 0.7 }, "<30%");
fadeTl.from("#sponsors aside", { x: "-100vw" }, "<-0.4");

var quotelines = document.querySelectorAll("#quote-text > p > *");
for (let i = 0; i < quotelines.length; i++) {
    const element = quotelines[i];
    if (element.tagName == "BR") {
        continue;
    }
}
