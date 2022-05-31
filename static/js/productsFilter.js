const filter = (brand = null, price = null, order = null, accessoryCategory = null, page = 1) => {
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

    if (accessoryCategory) {
        urlParams.set('accessoryCategory', accessoryCategory)
    }

    urlParams.set('page', page)

    window.location.assign(`?${urlParams.toString()}`)
}