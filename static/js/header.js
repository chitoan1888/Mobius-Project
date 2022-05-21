var cartItems = null;

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
        $("#toggleMenu").prop('checked', false);
        $('.header__navbar').removeClass("active");
        $('.overlay').removeClass("active");
    }
})

$('#toggleLoginMenu').click(() => {
    $('.navbar__mobile-login').toggleClass("active");
})

window.onload = () => {
    // Check active navlink
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

    // Get user cart data
    getUserCartData();
}

const getUserCartData = () => {
    $.ajax({
        type: 'GET',
        url: cartUrl,
        data: null,
        success: function (response) {
            if(!response["valid"]){
                cartItems = JSON.parse(response.cartItems);
                createCartHeaderItem(cartItems);
            }
        },
        error: function (response) {
            cartItems = null;
        }
      })
}

const createCartHeaderItem = (cartItems) => {
    $(".cart__total-num").text(cartItems.length);

    cartItems.forEach(cartItem => {
        $.ajax({
            type: 'GET',
            url: `/get/ajax/phone/${cartItem.fields.phone}/`,
            data: null,
            success: function (response) {
                if(!response["valid"]){
                    const phoneData = JSON.parse(response.phone)[0];

                    const li = document.createElement("li");
                    li.className = `cart-item ${phoneData.pk}`;

                    const a = document.createElement("a");
                    a.className="cart-item__link";
                    a.href = `dien-thoai/${phoneData.fields.name.split(" ").join("-")}`
                    li.append(a);

                    const img = document.createElement("img");
                    img.className = "cart-item__thumb";
                    img.src = `/media/${phoneData.fields.thumbnail}`;
                    a.append(img)

                    const div1 = document.createElement("div");
                    div1.className = "cart-item__info";

                    const h5 = document.createElement("h5");
                    h5.className = "cart-item__name text-gradient";
                    h5.innerText = phoneData.fields.name;
                    div1.append(h5);

                    const div2 = document.createElement("div");
                    div2.className = "cart-item__price-wrap";

                    const span1 = document.createElement("span");
                    span1.className = "cart-item__price";
                    span1.innerText = new Intl.NumberFormat().format(parseInt(phoneData.fields.price, 10)) + "đ";
                    div2.append(span1);

                    const span2 = document.createElement("span");
                    span2.className = "cart-item__qnt";
                    span2.innerText = ` x ${cartItem.fields.quantity}`;
                    div2.append(span2);

                    div1.append(div2);

                    a.append(div1);
                    $(".header .cart-list").append(li);
                }
            },
        })
    })
}
