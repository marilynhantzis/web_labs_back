from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start(): 
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
    <!doctype html>
    <html>
        <head>
            <title> НГТУ, ФБ, Лабораторные работы </title>
        </head>
        <body>
            <header> 
               <h1> НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
            </header>
            <a href = "/lab1"> Лаб ораторная работа 1 </a>
            <footer>
                &copy; Тарбанаков Артем Сергеевич, ФБИ-14, 3 курс, 2023
            </footer>
         </body>
    </html>
    """
@app.route("/lab1")
def lab1():
    return """
    Flask — фреймворк для создания веб-приложений на языке
    программирования Python, использующий набор инструментов
    Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
    называемых микрофреймворков — минималистичных каркасов
    веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
    """
@app.route("/lab1/oak")
def oak():
    return '''
    <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
        </head>
        <body>
            <h1>ДУБ</h1>
            <img src="''' + url_for('static', filename='oak.jpg.jpg') + '''">
        </body>
    </html>    
    '''