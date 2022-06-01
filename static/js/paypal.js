var finalTotalPrice = 0

const checkFieldsAndSubmit = () => {
    $('.checkout-payment__btn').click();
}

const checkout = () => {
    const paymentMethod = getPaymentMethod()

    if (paymentMethod === 1) {
        checkoutByPaypal()
    } else {

    }
}

const checkoutByPaypal = () => {
    // Render the PayPal button into #paypal-button-container
    paypal.Buttons({

        // Set up the transaction
        createOrder: function(data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: (finalTotalPrice/23000).toFixed(2)
                    }
                }]
            });
        },

        // Finalize the transaction
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(orderData) {
                // Successful capture! For demo purposes:
                console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
                var transaction = orderData.purchase_units[0].payments.captures[0];
                alert('Transaction '+ transaction.status + ': ' + transaction.id + '\n\nSee console for all available details');

                // Replace the above to show a success message within this page, e.g.
                // const element = document.getElementById('paypal-button-container');
                // element.innerHTML = '';
                // element.innerHTML = '<h3>Thank you for your payment!</h3>';
                // Or go to another URL:  actions.redirect('thank_you.html');
            });
        }


    }).render('#paypal-button-container');
}

const setupBeforeCheckout = () => {
    $('#paypal-button-container').html("");

    const formInputEls = $('#payment-form input')
    Array.from(formInputEls).forEach(el => {
        el.disabled = true;
    })

    const removeCartDelBtn = $('.cart-order__container .cart-item__remove-btn')
    Array.from(removeCartDelBtn).forEach(el => {
        el.onClick = null;
        el.innerHTML = ""
    })
}

const getPaymentMethod = () => {
    const paymentMethodEls = Array.from($('.payment-method input'))
    const check = paymentMethodEls.find(el => el.checked)

    return paymentMethodEls.indexOf(check)
}