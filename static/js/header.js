var cartItems = null;

// $(".header__search-btn").click(() => {
//     $(".header__search-btn").toggleClass("active");
//     $(".header__search-bar-wrap").toggleClass("active");
// })

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

const getUserCartData = () => {
    $(".header .cart-list").html("");
    const cartOrder = $(".cart-order__list");
    if (cartOrder) {
        cartOrder.html("");
    }

    if (is_authenticated) {
        $.ajax({
            type: 'GET',
            url: '/get/ajax/cart/',
            data: null,
            success: function (response) {
                if(!response["valid"]){
                    cartItems = JSON.parse(response.cartItems);
                    totalPrice = new Intl.NumberFormat().format(
                        Math.round(JSON.parse(response.totalPrice))
                    ) + "đ";
                    createCartHeaderItem(cartItems);
                    $('.cart__total-price').text(totalPrice)
                    finalTotalPrice = Math.round(JSON.parse(response.totalPrice))

                    const cartOrder = $(".cart-order__list");
                    if (cartOrder) {
                        $('.cart-order__total-price').text(totalPrice)
                    }
                }
            },
            error: function (response) {
                cartItems = null;
            }
          })
    } else {
        let cartItems = sessionStorage.getItem('cart');
        let totalPrice = sessionStorage.getItem('totalPrice');
        if (!cartItems && !totalPrice) {
            sessionStorage.setItem('cart', JSON.stringify([]));
            sessionStorage.setItem('totalPrice', '0');
            cartItems = []
            totalPrice = 0
        }

        createCartHeaderItem(JSON.parse(cartItems));
        finalTotalPrice = Math.round(JSON.parse(totalPrice))
        totalPrice = new Intl.NumberFormat().format(
            Math.round(JSON.parse(totalPrice))
        ) + "đ";
        $('.cart__total-price').text(totalPrice)

        const cartOrder = $(".cart-order__list");
        if (cartOrder) {
            $('.cart-order__total-price').text(totalPrice)
        }
    }
}

const checkAtiveNavLink = () => {
    const path = window.location.pathname;
    const navItems = $(".navbar__link");
    let index = -1;

    if (path === "/") {
        index = 0;
    } else if (path.includes("/dien-thoai")) {
        index = 1;
    } else if (path.includes("/phu-kien")) {
        index = 2;
    }else if (path.includes("/tin-tuc")) {
        index = 3;
    } else if (path.includes("/lien-he")) {
        index = 4;
    }

    if (index !== -1) {
        navItems[index].classList.add("active");
    }
}

const createCartHeaderItem = (cartItems) => {
    $(".cart__total-num").text(cartItems.length);

    if (cartItems.length > 0) {
        $(".header .cart-container").addClass("active");
        cartItems.forEach(cartItem => {
            if (cartItem.fields.phone) {
                $.ajax({
                    type: 'GET',
                    url: `/get/ajax/phone/${cartItem.fields.phone}/`,
                    data: null,
                    success: function (response) {
                        if(!response["valid"]){
                            const phoneData = JSON.parse(response.phone)[0];
                            renderCartItem(
                                phoneData,
                                cartItem.fields.quantity,
                                1
                            )
                        }
                    },
                })
            } else if (cartItem.fields.accessory) {
                $.ajax({
                    type: 'GET',
                    url: `/get/ajax/accessory/${cartItem.fields.accessory}/`,
                    data: null,
                    success: function (response) {
                        if(!response["valid"]){
                            const accessoryData = JSON.parse(response.accessory)[0];
                            renderCartItem(
                                accessoryData,
                                cartItem.fields.quantity,
                                2
                            )
                        }
                    },
                })
            }
        })
    } else {
        $(".header .cart-container").removeClass("active");
        const div = document.createElement("div");
        div.className = 'cart-no-item'
        div.innerText = 'Chưa có sản phẩm nào được thêm vào'
        $(".header .cart-list").append(div);
    }

}

const renderCartItem = (productData, quantity, type) => {
    const li = document.createElement("li");
    li.className = `cart-item ${productData.pk}`;

    const img = document.createElement("img");
    img.className = "cart-item__thumb";
    img.src = `/media/${productData.fields.thumbnail}`;
    li.append(img)

    const div1 = document.createElement("div");
    div1.className = "cart-item__info";

    const a = document.createElement("a");
    a.className="cart-item__link";
    a.href = `/dien-thoai/${productData.fields.name.split(" ").join("-")}`

    const h5 = document.createElement("h5");
    h5.className = "cart-item__name text-gradient";
    h5.innerText = productData.fields.name;
    a.append(h5)
    div1.append(a);

    const div2 = document.createElement("div");
    div2.className = "cart-item__price-wrap";

    const span1 = document.createElement("span");
    span1.className = "cart-item__price";
    span1.innerText = new Intl.NumberFormat().format(
        Math.round(parseInt(productData.fields.price, 10) - parseInt(productData.fields.price, 10) * parseFloat(productData.fields.saleOff))
    ) + "đ";

    const span2 = document.createElement("span");
    span2.className = "cart-item__qnt";
    span2.innerText = ` x ${quantity}`;

    const deleteBtn = document.createElement("button")
    deleteBtn.className = "cart-item__remove-btn"
    deleteBtn.innerText = 'Xóa'
    deleteBtn.onclick = () => removeProductFromCart(productData.pk, type, quantity)

    div2.append(span1, span2, deleteBtn);


    div1.append(div2);

    li.append(div1);
    $(".header .cart-list").append(li);

    const cartOrder = $(".cart-order__list");
    if (cartOrder) {
        const clone = li.cloneNode(true)
        clone.querySelector(".cart-item__remove-btn").onclick = () => removeProductFromCart(productData.pk, type, quantity)

        cartOrder.append(clone);
    }
}