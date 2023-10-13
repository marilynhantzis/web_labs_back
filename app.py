from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start(): 
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return '''
    <!doctype html>
    <html>
        <head>
            <title> НГТУ, ФБ, Лабораторные работы </title>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
        </head>
        <body>
            <header> 
                НГТУ, ФБ, WEB-программирование, часть 2
            </header>
            <h2 class="hh">Список лабораторных</h2>
            <ul class='labs'>
            <li><a href = "/lab1"> Лабораторная работа 1."Простые страницы на Flask" </a></li>
            <li><a href = "/lab2"> Лабораторная работа 2."Шаблоны в Flask" </a></li>
            </ul>
            <footer>
                &copy; Тарбанаков Артем Сергеевич, ФБИ-14, 3 курс, 2023
            </footer>
         </body>
    </html>
    '''
@app.route("/lab1")
def lab1():
    return '''
    <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
        </head>
        <body>
            <header> 
                НГТУ, ФБ, WEB-программирование, часть 2
            </header>
            <h2>Информация про Flask</h2>
            <div class="flask">
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </div>
            <a href="/menu"> Вернуться в меню </a>
            <h2> Реализованные роуты </h2>
            <ul>
            <li><a href="/lab1/oak">/lab1/oak - ДУБ</a></li>   
            <li><a href="/lab1/student">/lab1/student - СТУДЕНТ</a> </li>  
            <li><a href="/lab1/python">/lab1/python - PYTHON</a> </li> 
            <li><a href="/lab1/web">/lab1/web - ВЕБ-программирование</a></li>
            </ul>
            <footer>
                &copy; Тарбанаков Артем Сергеевич, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>    
    '''
@app.route("/lab1/oak")
def oak():
    return '''
    <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
        </head>
        <body>
            <header> 
                НГТУ, ФБ, WEB-программирование, часть 2
            </header>
            <h1>ДУБ</h1>
            <img src="''' + url_for('static', filename='oak.jpg.jpg') + '''">
            <footer>
                &copy; Тарбанаков Артем Сергеевич, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>    
    '''
@app.route("/lab1/student")
def student():
    return '''
    <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
        </head>
        <body>
            <header> 
                НГТУ, ФБ, WEB-программирование, часть 2
            </header>
            <h1>Тарбанаков Артем Сергеевич</h1>
            <img src="''' + url_for('static', filename='nstu.jpg') + '''">
            <footer>
                &copy; Тарбанаков Артем Сергеевич, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>    
    '''
@app.route("/lab1/python")
def python():
    return '''
    <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
        </head>
        <body>
            <header> 
                НГТУ, ФБ, WEB-программирование, часть 2
            </header>
            <h2> Что такое Python? </h2>
            <div class="py">
            Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью языка является выделение блоков кода пробельными отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++.
            </div>
            <div class="py">
            Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, объектно-ориентированное программирование, метапрограммирование и функциональное программирование. Задачи обобщённого программирования решаются за счёт динамической типизации. Аспектно-ориентированное программирование частично поддерживается через декораторы, более полноценная поддержка обеспечивается дополнительными фреймворками. Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений. Основные архитектурные черты — динамическая типизация, автоматическое управление памятью, полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL), высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты.
            </div>
            <div class="py">
            Эталонной реализацией Python является интерпретатор CPython, который поддерживает большинство активно используемых платформ и являющийся стандартом де-факто языка. Он распространяется под свободной лицензией Python Software Foundation License, позволяющей использовать его без ограничений в любых приложениях, включая проприетарные. CPython компилирует исходные тексты в высокоуровневый байт-код, который исполняется в стековой виртуальной машине. К другим трём основным реализациям языка относятся Jython (для JVM), IronPython (для CLR/.NET) и PyPy. PyPy написан на подмножестве языка Python (RPython) и разрабатывался как альтернатива CPython с целью повышения скорости исполнения программ, в том числе за счёт использования JIT-компиляции. Поддержка версии Python 2 закончилась в 2020 году. На текущий момент активно развивается версия языка Python 3. Разработка языка ведётся через предложения по расширению языка PEP (англ. Python Enhancement Proposal), в которых описываются нововведения, делаются корректировки согласно обратной связи от сообщества и документируются итоговые решения.
            </div>

            <img src="''' + url_for('static', filename='python.jpg') + '''">
            <footer>
                &copy; Тарбанаков Артем Сергеевич, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>    
    '''
@app.route("/lab1/web")
def web():
    return '''
    <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
        </head>
        <body>
            <header> 
                НГТУ, ФБ, WEB-программирование, часть 2
            </header>
            <h2>Веб-программирование</h2>
            <div>
            Веб-программирование — раздел программирования, ориентированный на разработку веб-приложений (программ, обеспечивающих функционирование динамических сайтов Всемирной паутины)
            Языки веб-программирования — это языки, которые в основном предназначены для работы с веб-технологиями. Языки веб-программирования можно условно разделить на две пересекающиеся группы: клиентские и серверные.
            </div>
            <h2>Колиентские языки</h2>
            <div>
            Как следует из названия, программы на клиентских языках обрабатываются на стороне пользователя, как правило, их выполняет браузер. Это и создает главную проблему клиентских языков — результат выполнения программы (скрипта) зависит от браузера пользователя. То есть, если пользователь запретил выполнять клиентские программы, то они исполняться не будут, как бы ни желал этого программист. Кроме того, может произойти такое, что в разных браузерах или в разных версиях одного и того же браузера один и тот же скрипт будет выполняться по-разному. С другой стороны, если программист возлагает надежды на серверные программы, то он может упростить их работу и снизить нагрузку на сервер за счет программ, исполняемых на стороне клиента, поскольку они не всегда требуют перезагрузку (генерацию) страницы.
            </div>
            <h2>Серверные языки</h2>
            <div>
            Когда пользователь дает запрос на какую-либо страницу (переходит на неё по ссылке или вводит адрес в адресной строке своего браузера), то вызванная страница сначала обрабатывается на сервере, то есть выполняются все программы, связанные со страницей, и только потом возвращается к посетителю по сети в виде файла. Этот файл может иметь расширения HTML, PHP, ASP, ASPX, Perl, SSI, XML, DHTML, XHTML.
            Работа программ уже полностью зависима от сервера, на котором расположен сайт, и от того, какая версия того или иного языка поддерживается. Важной стороной работы серверных языков является возможность организации непосредственного взаимодействия с системой управления базами данных (или СУБД) — сервером базы данных, в которой упорядоченно хранится информация, которая может быть вызвана в любой момент.
            </div>

            <img src="''' + url_for('static', filename='webb.jpg') + '''">
            <footer>
                &copy; Тарбанаков Артем Сергеевич, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>    
    '''
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