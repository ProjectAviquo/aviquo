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
function fade_scroll(selector) {
    fadeTl.from(selector, {
        opacity: 0,
        y: "-40px",
        scrollTrigger: {
            trigger: selector,
            start: "bottom bottom",
            end: "+=100",
            scrub: 1,
            once: true
        }
    });
}
for (let i = 0; i < quotelines.length; i++) {
    const element = quotelines[i];
    if (element.tagName == "BR") {
        continue;
    }
    fade_scroll(element)
}

fade_scroll("#introducing h5");
fade_scroll("#introducing h2");

const productBoxes = document.querySelectorAll('.product-box');
const prevButton = document.getElementById('prev-btn');
const nextButton = document.getElementById('next-btn');
let currentBox = 1; // Initial box at the center

function updateProductBoxStyles() {
    productBoxes.forEach((box, index) => {
        const distance = Math.abs(currentBox - index);
        const scale = 1 - distance * 0.1;
        const background = index === currentBox ? '#ffcfcf' : '#ccadbe';
        const zIndex = index === currentBox ? 1 : 0;

        box.style.transform = `scale(${scale})`;
        box.style.background = background;
        box.style.zIndex = zIndex;
    });
}

function navigate(direction) {
    if (direction === 'prev' && currentBox > 0) {
        currentBox--;
    } else if (direction === 'next' && currentBox < productBoxes.length - 1) {
        currentBox++;
    }

    updateProductBoxStyles();
}

prevButton.addEventListener('click', () => navigate('prev'));
nextButton.addEventListener('click', () => navigate('next'));

document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowLeft") {
        // Handle left arrow key press (previous item)
        navigate("prev");
    } else if (event.key === "ArrowRight") {
        // Handle right arrow key press (next item)
        navigate("next");
    }
});

// Initial update
updateProductBoxStyles();
