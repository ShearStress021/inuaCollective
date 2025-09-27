    AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true
        });
        
        feather.replace();
        
        // Initialize Vanta.js globe effect
        VANTA.GLOBE({
            el: "#vanta-globe",
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x3a82ff,
            backgroundColor: 0x1665d8,
            size: 0.8
        });


document.addEventListener('DOMContentLoaded', function () {
  const button = document.getElementById('mobile-menu-button');
  const menu = document.getElementById('mobile-menu');

  button.addEventListener('click', function () {
    button.name = button.name === 'menu' ? 'close' : 'menu'
    menu.classList.toggle('hidden');
  });
});
  

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