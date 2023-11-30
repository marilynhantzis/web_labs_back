from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route("/lab3/")
def labb3():
    return render_template('lab3.html')


@lab3.route("/lab3/form1/")
def form1():
    errors = {}
    user = request.args.get('user')
    age = request.args.get('age')
    if user == '':
        errors['user'] = 'Заполните поле!'
    if age== '':
        errors['age'] = 'Заполните поле!'
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route("/lab3/order/")
def order():
    price1=0
    price2=0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price1 += 120
    elif drink == 'black-tea':
        price1 += 80
    elif drink == 'green-tea':
        price1 += 70

    if request.args.get('milk') == 'on' and request.args.get('sugar') == 'on':
        price2 += 40
    elif request.args.get('milk') == 'on':
        price2 += 30
    elif request.args.get('sugar') == 'on':
        price2 += 10

    return render_template('order.html', price1=price1, price2=price2)


@lab3.route("/lab3/pay/")
def pay():
    price=0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price = price)


@lab3.route("/lab3/success/")
def thanks():
    return render_template('success.html')


@lab3.route("/lab3/buy")
def buy():
    errors = {}
    name = request.args.get('name')
    type = request.args.get('type')
    bag = request.args.get('bag')
    age = request.args.get('age')
    start = request.args.get('start')
    finish = request.args.get('finish')
    date = request.args.get('date')
    place = request.args.get('place')
    if name == '':
        errors['name'] = 'Введите имя!'
    if age == '':
        errors['age'] = 'Введите возраст!'
    if start == '':
        errors['start'] = 'Введите место отправления!'
    if finish == '':
        errors['finish'] = 'Введите место прибытия!'
    if date == '':
        errors['date'] = 'Введите дату!'
    return render_template('buy.html', name = name, type = type, bag = bag, age = age, start = start, finish = finish, date = date, errors=errors, place = place)