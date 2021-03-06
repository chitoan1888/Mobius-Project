$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

const addProductToCard = (productId, type) => {
    if (is_authenticated) {
        if($(`.${productId}`).length === 1) {
            $.ajax({
                type: 'POST',
                url: `/update/ajax/cart/${type}`,
                dataType: "json",
                data: {
                    "productId": productId,
                },
                success: function (response) {
                    // console.log(response);
                    getUserCartData();
                },
                error: function (response) {
                    // console.log(response);
                }
            })
        } else {
            $.ajax({
                type: 'POST',
                url: `/post/ajax/cart/${type}`,
                dataType: "json",
                data: {
                    "productId": productId,
                    "quantity": 1,
                },
                success: function (response) {
                    // console.log(response);
                    getUserCartData(is_authenticated);
                },
                error: function (response) {
                    // console.log(response);
                }
            })
        }
    } else {
        const cart = JSON.parse(
            sessionStorage.getItem('cart')
        );

        let totalPrice = JSON.parse(
            sessionStorage.getItem('totalPrice')
        );

        const productType = type === 1 ? 'phone' : 'accessory'

        if($(`.${productId}`).length === 1) {
            cart.map((cartItem) => {
                if (cartItem.fields.phone === productId || cartItem.fields.accessory === productId) {
                    cartItem.fields.quantity = cartItem.fields.quantity + 1

                }
            })
        } else {
            cart.push({
                fields: {
                    phone: type === 1 ? productId : null,
                    accessory: type === 2 ? productId : null,
                    quantity: 1
                }
            })
        }

        $.ajax({
            type: 'GET',
            url: `/get/ajax/${productType}/${productId}/`,
            data: null,
            success: function (response) {
                if(!response["valid"]){
                    const productData = JSON.parse(response.phone)[0];
                    totalPrice += (productData.fields.price - productData.fields.price * productData.fields.saleOff)

                    sessionStorage.setItem(
                        'cart',
                        JSON.stringify(cart)
                    )
                    sessionStorage.setItem(
                        'totalPrice',
                        JSON.stringify(totalPrice)
                    )
                    getUserCartData();
                }
            },
        })
    }
}


const removeProductFromCart = (productId, type, quantity) => {
    if (is_authenticated) {
        $.ajax({
            type: 'POST',
            url: `/remove/ajax/cart/${type}`,
            dataType: "json",
            data: {
                "productId": productId,
            },
            success: function (response) {
                // console.log(response);
                $(`.header .cart-list .cart-item.${productId}`).remove();
                getUserCartData();
            },
            error: function (response) {
                // console.log(response);
            }
        })
    } else {
        const cart = JSON.parse(
            sessionStorage.getItem('cart')
        );

        let totalPrice = JSON.parse(
            sessionStorage.getItem('totalPrice')
        );

        const newCart = cart.filter((cartItem) => (
            cartItem.fields.phone !== productId &&
            cartItem.fields.accessory !== productId
        ))

        const productType = type === 1 ? 'phone' : 'accessory'

        $.ajax({
            type: 'GET',
            url: `/get/ajax/${productType}/${productId}/`,
            data: null,
            success: function (response) {
                if(!response["valid"]){
                    const productData = JSON.parse(response.phone)[0];
                    totalPrice = totalPrice - (productData.fields.price - productData.fields.price * productData.fields.saleOff) * quantity

                    sessionStorage.setItem(
                        'cart',
                        JSON.stringify(newCart)
                    )
                    sessionStorage.setItem(
                        'totalPrice',
                        JSON.stringify(totalPrice)
                    )
                    getUserCartData();
                }
            },
        })
    }
}