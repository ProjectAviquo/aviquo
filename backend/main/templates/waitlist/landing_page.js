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
$("#sponsors").css("transform", "translate(0, 20px)");

var fadeTl = gsap.timeline({ defaults: { duration: 1 } });

fadeTl.to("h1", { opacity: 1, delay: 0.3, y: 0 });
fadeTl.to("header h3", { opacity: 1, y: 0 }, "<30%");
fadeTl.to("form", { opacity: 1, y: 0 }, "<50%");
fadeTl.to("#sponsors", { opacity: 1, y: 0 }, "<50%");
