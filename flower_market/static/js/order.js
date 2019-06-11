$(document).ready(function() {

    $('.buy-button').click(function (event) {
        var id = event.target.id;
        var idx = id.split('_')[1];
        var name = titles[idx];
        var price = prices[idx];
        var image = images[idx];

        var cardLen = 0;
        var cardList = {};
        var cardListJson = localStorage.getItem('cardList');

        if (cardListJson != null || cardListJson === '') {
            cardList = JSON.parse(cardListJson);
        }

        $('#cardList').empty();

        for (var key in cardList) {
            if (key !== id) {
                var sum_price = parseInt(cardList[key]['price']) * parseInt(cardList[key]['quantity']);
                var productHtml = '<div class="row">' + '<div class="col-8"><p class="float-left"><image src="/static/images/' + cardList[key]['image'] +
                    '" class="picture" width="100" height="100" data-was-processed="true"></p> ' +
                    '<br><div class="productName">' + cardList[key]['name'] + '</div></div>' +
                    '<div class="productQuantity col-1">' + cardList[key]['quantity'] + '</div>' +
                    '<div class="productPrice col-3">' + sum_price + '</div>' + '</div>';
                $('#cardList').append(productHtml);
                cardLen++;
            }
        }

        if (cardLen > 0) {
            $('#cardListTitle').text('У ВАС В КОРЗИНЕ ЕЩЕ ' + cardLen + ' ТОВАРА');
        }

        var quantity = 1;
        if (cardList[id] != null) {
            quantity = cardList[id]['quantity'] + 1;
        }

        $('#lastProductName').text(name);
        $('#lastProductPrice').text(parseInt(price) * parseInt(quantity));
        $('#lastProductQuantity').text(quantity);
        $('#lastProductImage').attr('src', '/static/images/' + image);

        cardList[id] = {'name': name, 'price': price, 'image': image, 'quantity': quantity};
        localStorage.setItem('cardList', JSON.stringify(cardList));
    });


    $('#cancel').click(function () {
        $('#modalCardList').modal('hide');
    });

});

