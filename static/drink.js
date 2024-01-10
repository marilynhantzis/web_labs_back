function getPrice(){
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const obj = {
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar
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
        document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб`;
        document.querySelector('#price').style.display = '';
        document.querySelector('#pay').style.display = '';
    })
}
function Pay() {
    const card = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    const obj = {
        "method": "pay",
        "params": {
            card_num: card,
            cvv:cvv,
            drink: drink,
            milk: milk,
            sugar: sugar
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
        if (data.result) {
            document.querySelector('#position').style.display = 'none';
            document.querySelector('#calc').style.display = 'none';
            document.querySelector('#price').style.display = 'none';
            document.querySelector('#pay').style.display = 'block';
            document.querySelector('#pay_result').style.display = '';
            document.querySelector('#pay').innerHTML = `${data.result}`;
        }
        if(data.error) {
            document.querySelector('#erros').style.display = '';
            document.querySelector('#error').innerHTML = `${data.error}`;
        }
    })
}