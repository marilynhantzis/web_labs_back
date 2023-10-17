from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)


@app.route("/lab2/example")
def example():
    name = 'Артем Тарбанаков'
    num = 2
    course = 3
    name, num, course, group = 'Артем Тарбанаков', 2, 3, 'ФБИ-14'
    fruits = [
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120}, 
        {'name': 'апельсин', 'price': 80}, 
        {'name': 'мандарины', 'price': 95}, 
        {'name': 'манго', 'price': 321}
        ]
    books = [
        {'book': 'Мастер и Маргарита', 'author': 'Булгаков М.А.', 'genre': 'Роман', 'pages': 576 },
        {'book': 'Белая гвардия', 'author': 'Булгаков М.А.', 'genre': 'Роман', 'pages': 278 },
        {'book': 'Идиот', 'author': 'Достоевский Ф.М.', 'genre': 'Роман', 'pages': 864 },
        {'book': 'Братья Карамазовы', 'author': 'Достоевский Ф.М.', 'genre': 'Роман', 'pages': 1488 },
        {'book': 'Игрок', 'author': 'Достоевский Ф.М.', 'genre': 'Роман', 'pages': 369 },
        {'book': 'Стихотворения и поэмы', 'author': 'Есенин С.А.', 'genre': 'Поэзия', 'pages': 124 },
        {'book': 'Черный человек', 'author': 'Есенин С.А.', 'genre': 'Поэзия', 'pages': 169 },
        {'book': 'Лирика', 'author': 'Пастернак Б.Л.', 'genre': 'Поэзия', 'pages': 98 },
        {'book': 'Доктор Живаго', 'author': 'Пастернак Б.Л.', 'genre': 'Роман', 'pages': 269 },
        {'book': 'Евгений Онегин', 'author': 'Пушкин А.С.', 'genre': 'Роман', 'pages': 333 }
    ]
    return render_template('example.html', 
                           name = name, num = num, course = course, group = group,
                           fruits = fruits, books = books)


@app.route('/lab2/flowers') 
def flowers():
    return render_template('flowers.html')


@app.route('/lab2') 
def lab2():
    return render_template('lab2.html')