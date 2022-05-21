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

const addProductToCard = (productId) => {
    if($(`.${productId}`).length === 1) {
        $.ajax({
            type: 'POST',
            url: `/update/ajax/cart/`,
            dataType: "json",
            data: {
                "phoneId": productId,
            },
            success: function (response) {
                console.log(response);
                $(".header .cart-list").html("");
                getUserCartData();
            },
            error: function (response) {
                console.log(response);
            }
        })
    } else {
        $.ajax({
            type: 'POST',
            url: `/post/ajax/cart/`,
            dataType: "json",
            data: {
                "phoneId": productId,
                "quantity": 1,
            },
            success: function (response) {
                console.log(response);
                $(".header .cart-list").html("");
                getUserCartData();
            },
            error: function (response) {
                console.log(response);
            }
        })
    }
}