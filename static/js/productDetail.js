const productThumbContainer = document.querySelectorAll(".product-thumb-container");

productThumbContainer.forEach((container) => {
    const img = container.querySelector(".product-thumb");
    container.addEventListener("mousemove", onZoom);
    container.addEventListener("mouseover", onZoom);
    container.addEventListener("mouseleave", offZoom);

    function onZoom(e) {
        const x = e.clientX;
        const y = e.clientY;
        img.style.transformOrigin = `${x}px ${y}px`;
        img.style.transform = "scale(1.5)";
    }
    function offZoom(e) {
        img.style.transformOrigin = `center center`;
        img.style.transform = "scale(1)";
    }
})

$(".product-description .see-more").click(() => {
    $(".product-description > div").toggleClass("active")
    if ($(".product-description > div").hasClass("active")) {
        $(".product-description .see-more").text("THU GỌN")
    } else {
        $(".product-description .see-more").text("XEM THÊM")
    }
})