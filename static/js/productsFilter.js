const filter = (brand = null, price = null, order = null) => {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);

    if (brand) {
        urlParams.set('brand', brand)
    }

    if (price) {
        urlParams.set('price', JSON.stringify(price))
    }

    if (order) {
        urlParams.set('order', order)
    }



    window.location.assign(`?${urlParams.toString()}`)
}