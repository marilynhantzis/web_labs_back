from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, redirect, url_for, render_template, request, session
import psycopg2


lab5 = Blueprint('lab5',__name__)

def dbConnect(): 
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_tarbanakov",
        port="5432",
        user="tarbanakov_knowledge_base",
        password="123")
    
    return conn

def dbClose(cursor, connection): 
    cursor.close()
    connection.close()




@lab5.route('/lab5/')
def main(): 
    visiblename = 'Аноним'

    return render_template('baza_main.html', visiblename = visiblename)


@lab5.route('/lab5/users')
def main1(): 
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users;')

    result = cur.fetchall()

    dbClose(cur, conn)

    return render_template('result.html', result = result)


@lab5.route('/lab5/register', methods=['GET', 'POST'])
def registerPage():
    errors=[]

    if request.method == 'GET': 
        return render_template('register.html', errors=errors)
    
    username = request.form.get('username')
    password = request.form.get('password')

    if not (username or password):
        errors.append('Пожалуйста, заполните все поля')
        print(errors)
        return render_template('register.html', errors=errors)
    
    hashPassword = generate_password_hash(password)
    
    conn = dbConnect()
    cur = conn.cursor()


    cur.execute(f"SELECT username FROM users WHERE username = '{ username}';")

    if cur.fetchone() is not None:
        errors.append('Пользователь с данным именем уже существует')
        conn.close()
        cur.close()

        return render_template('register.html', errors=errors)
    

    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashPassword}');")

    conn.commit()
    conn.close()
    cur.close()

    return redirect('/lab5/')


@lab5.route('/lab5/login', methods=['GET', 'POST'])
def loginPage():
    errors = []
    if request.method == "GET":
        return render_template("log_in.html", errors = errors)


    username = request.form.get("username")
    password = request.form.get("password")


    if not (username or password):
        errors.append('Пожалуйста, заполните все поля')
        return render_template('log_in.html', errors=errors)


    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username,password FROM users WHERE username = '{ username}';")

    result = cur.fetchone()
    print(result)

    if result is None:
        errors.append('Неправильный логин или пароль')
        dbClose(cur, conn)
        return render_template("log_in.html", errors = errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur,conn)
        return redirect("/lab5")

    else:
        errors.append("Неправильный логин или пароль")
        return render_template("log_in.html", errors=errors)