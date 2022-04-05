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