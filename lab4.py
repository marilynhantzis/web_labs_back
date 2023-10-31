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