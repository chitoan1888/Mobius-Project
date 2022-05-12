$(".header__search-btn").click(() => {
    $(".header__search-btn").toggleClass("active");
    $(".header__search-bar-wrap").toggleClass("active");
})

$("#toggleMenu").change(() => {
    $('.overlay').toggleClass("active");
    $('.header__navbar').toggleClass("active");
})

$('.overlay').click(() => {
    if ($('.header__navbar').hasClass("active")) {
        console.log("clicked");
        $("#toggleMenu").prop('checked', false);
        $('.header__navbar').removeClass("active");
        $('.overlay').removeClass("active");
    }
})

$('#toggleLoginMenu').click(() => {
    $('.navbar__mobile-login').toggleClass("active");
})

window.onload = () => {
    const path = window.location.pathname;
    const navItems = $(".navbar__link");
    let index = -1;

    if (path === "/") {
        index = 0;
    } else if (path.includes("/dien-thoai")) {
        index = 1;
    } else if (path.includes("/phu-kien")) {
        index = 2;
    } else if (path.includes("/lien-he")) {
        index = 3;
    }

    if (index !== -1) {
        navItems[index].classList.add("active");
    }
}