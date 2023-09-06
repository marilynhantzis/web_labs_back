from flask import Flask
app= Flask(__name__)

@app.route("/")
def start(): 
    return """
    <!doctype html>
    <html>
        <head>
            <title> Тарбанаков Артем Сергеевич, Лабораторная 1
        </head>
        <body>
            <header> 
                НГТУ, ФБ, Лабораторная 1
            </header>

            <h1> веб-сервер на flask </h1>

            <footer>
                &copy; Тарбанаков Артем Сергеевич, ФБИ-14, 3 курс, 2023
            </footer>
         </body>
    </html>
    """

        