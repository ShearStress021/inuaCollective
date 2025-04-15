const menuOpenBtn = document.querySelector("#menu-open-button")
const menuCloseBtn = document.querySelector("#menu-close-button")


menuOpenBtn.addEventListener('click', () => {
    document.body.classList.toggle("show-mobile-menu")
})

menuCloseBtn.addEventListener('click', () => menuOpenBtn.click())