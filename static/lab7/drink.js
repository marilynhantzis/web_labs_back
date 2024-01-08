function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const obj = {
        'method': 'get-price',
        'params': {
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    }
};


fetch('/lab7/api', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(obj)
})
.then(function(resp) {
    return resp.json();
})
.then(function(data) {
    document.querySelector('#price').innerHTML = 'Цена напитка: ${data.result} руб';
})



function pay() {
    const drink = document.querySelector('name=drink:checked').value;
    const milk = document.querySelector('name=milk').checked;
    const sugar = document.querySelector('name=sugar').checked;
    const cardNumber = document.querySelector('name=cardNumber').value;
    const cvv = document.querySelector('name=cvv').value;

    const obj = {
        'method': 'pay',
        'params': {
            drink: drink,
            milk: milk,
            sugar: sugar,
            cardNumber: cardNumber,
            cvv: cvv
        }
    }

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        if (resp.ok) {
            return resp.json();
        } else {
            throw new Error('Ошибка при оплате');
        }
    })
    .then(function(data) {
        document.querySelector('#payment-status').innerHTML = data.result;
    })
    .catch(function(error) {
        document.querySelector('#payment-status').innerHTML = error.message;
    });
}