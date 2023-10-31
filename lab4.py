from flask import Blueprint, redirect, url_for, render_template, request
lab4 = Blueprint('lab4',__name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'marilynhantzis' and password == '1337':
        return render_template('success1.html', username = username)
    elif username == '' or password == '':
        error1 = 'Заполните поля!'
        return render_template('login.html', error1=error1, username = username, password = password)
    else:
        error2 = 'Неверные логин и/или пароль'
        return render_template('login.html', username = username, error2=error2, password = password)


@lab4.route('/lab4/fridge', methods= ['GET', 'POST'])
def fridge():
    temp = request.form.get('temp')
    head = ''
    foot = ''
    src=''
    if request.method == 'GET':
        return render_template('fridge.html')
    if temp == '':
        error = 'Указано пустое значение'
        return render_template('fridge.html', temp=temp, error = error)
    elif float(temp) < -12:
        head = 'Не удалось установить температуру'
        foot = 'Слишком низкое значение'
        return render_template('fridge_temp.html', temp=temp, head=head, foot=foot)
    elif float(temp) > -1:
        head = 'Не удалось установить температуру'
        foot = 'Слишком высокое значение'
        return render_template('fridge_temp.html', temp=temp, head=head, foot=foot)
    elif -12 <= float(temp) <= -9:
        head = 'Установлена температура'
        foot = 'Установлена температура: ' + temp +'°C'
        src= 'blue_snowflake.jpg'
        return render_template('fridge_temp.html', temp=temp, head=head, foot=foot, src=src)
    elif -8 <= float(temp) <= -5:
        head = 'Установлена температура'
        foot = 'Установлена температура: ' + temp +'°C'
        src = 'blue_snowflake.jpg'
        src2 = 'blue_snowflake.jpg'
        return render_template('fridge_temp.html', temp=temp, head=head, foot=foot, src=src, src2=src2)
    elif -4 <= float(temp) <= -1:
        head = 'Установлена температура'
        foot = 'Установлена температура: ' + temp +'°C'
        src= 'blue_snowflake.jpg'
        src2 = 'blue_snowflake.jpg'
        src3 = 'blue_snowflake.jpg'
        return render_template('fridge_temp.html', temp=temp, head=head, foot=foot, src=src, src2=src2, src3=src3)
    
@lab4.route('/lab4/zerno', methods= ['GET', 'POST'])
def zerno(): 
    weight = request.form.get('weight')
    zerno = request.form.get('zerno')
    order = 0
    sum=0
    sale=0
    if request.method == 'GET':
        return render_template('order_zerno.html')
    if weight == '':
        order = 1
        return render_template('zerno.html', order = order)
    elif float(weight) > 500:
        order = 2
        return render_template('zerno.html', order = order)
    elif float(weight) <= 0:
        order = 3
        return render_template('zerno.html', order = order)
    elif float(weight) > 50:
        order = 4 
        if zerno == 'first':
            sum= 12000 * float(weight)
            zerno = 'Ячмень'
        elif zerno == 'second':
            sum = 8500 * float(weight)
            zerno = 'Овес'
        elif zerno == 'third':
            sum = 8700 * float(weight)
            zerno = 'Пшеница'
        elif zerno == 'four':
            sum = 14000 * float(weight)
            zerno = 'Рожь'
        sale=0.1*sum
        sum= sum - sale
        return render_template('zerno.html', order = order, sum=sum, sale=sale, weight=weight, zerno=zerno)
    else:
        order = 5 
        if zerno == 'first':
            sum= 12000 * float(weight)
            zerno = 'Ячмень'
        elif zerno == 'second':
            sum = 8500 * float(weight)
            zerno = 'Овес'
        elif zerno == 'third':
            sum = 8700 * float(weight)
            zerno = 'Пшеница'
        elif zerno == 'four':
            sum = 14000 * float(weight)
            zerno = 'Рожь'
        return render_template('zerno.html', order = order, sum=sum, weight=weight, zerno=zerno)
    
@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies():
    if request.method=='GET':
        return render_template('cookies.html')
    
    color = request.form.get('color')
    headers = {
        'Set-Cookie': 'color=' + color + '; path=/',
        'Location': '/lab4/cookies'
    }
    return '', 303, headers 