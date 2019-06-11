$(document).ready(function () {
    var amount = 0;
    var cardLen = 0;
    var cardList = {};
    var cardListJson = localStorage.getItem('cardList');

    $('#order_list').val(cardListJson);

    if (cardListJson != null || cardListJson === '') {
        cardList = JSON.parse(cardListJson);
    }

    for (var key in cardList) {
        var sum_price = parseInt(cardList[key]['price']) * parseInt(cardList[key]['quantity']);
        var productHtml = '<div class="row"><div class="col-6">' +
            '<image class="picture" width="100" height="100" data-was-processed="true" ' +
            'src="/static/images/' + cardList[key]['image'] + '">' +
            '<div class="productName">' + cardList[key]['name'] + '</div></div>' +
            '<div class="col-3 productQuantity quantity-column">' + cardList[key]['quantity'] + '</div>' +
            '<div class="col-3 productPrice price-column">' + sum_price + ' тг.</div>' + '</div><hr>';
        $('#cards-body').append(productHtml);
        cardLen++;

        amount += sum_price;
    }

    if (cardLen > 0) {
        $('#products-title').text('ТОВАРОВ В КОРЗИНЕ (' + cardLen + ')')
        $('#submitBtn').attr('disabled', false);
    }

    $('#amount').text('Общая сумма ' + amount + ' тг.');
    $('#order_amount').val(amount);
});

function deliveryTypeChange(el) {
    console.log(el.value);
    if (el.value === '0') {
        $('#address-area').hide();
    } else {
        $('#address-area').show();
    }
}
