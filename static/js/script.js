const menuOpenBtn = document.querySelector("#menu-open-button")
const menuCloseBtn = document.querySelector("#menu-close-button")


menuOpenBtn.addEventListener('click', () => {
    document.body.classList.toggle("show-mobile-menu")
})

menuCloseBtn.addEventListener('click', () => menuOpenBtn.click())


const header = document.querySelector(
    ".header"
)

window.addEventListener("scroll", () => {
    header.classList.toggle(
        "sticky", this.window.scrollY > 0
    )
})


// Initialisae Swiper
const swiper = new Swiper('.slider-wrapper', {

    loop: true,
    grabCursor: true,
    spaceBetween: 25,


    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        dynamicBullets: true,
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // Responsive breakpoints
    breakpoints: {
        0: {
            slidesPerView: 1
        },
        768: {
            slidesPerView: 2
        },
        1024: {
            slidesPerView: 3
        },
    }

});
