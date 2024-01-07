from Db import db
from Db.models import users, artickles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, redirect, url_for, render_template, request, session
import psycopg2


lab6 = Blueprint('lab6',__name__)


@lab6.route('/lab6/')
def main_page():
    visiblename = 'Аноним'
    return render_template('baza_main.html', visiblename = visiblename)


@lab6.route('/lab6/check')
def main():
    my_users = users.query.all()
    print(my_users)
    return 'result in console!'


@lab6.route('/lab6/checkarticles')
def checkArticles():
    my_articles = artickles.query.all()
    print(my_articles)
    return 'result in console!'


@lab6.route('/lab6/register', methods=["GET", "POST"])
def register():

    errors=[]

    if request.method == 'GET':
        return render_template('register.html', errors=errors)
    
    username_form = request.form.get('username')
    password_form = request.form.get('password')

    if not (username_form or password_form):
        errors.append('Пожалуйста, заполните все поля')
        return render_template('register.html', errors=errors)
    
    if len(password_form) < 5:
        errors.append('Пароль должен быть не менее 5 символов')
        return render_template('register.html', errors=errors)


    isUserExist = users.query.filter_by(username=username_form).first()

    if isUserExist is not None:
        errors.append('Пользователь с данным именем уже существует')
        return render_template('register.html', errors=errors)
    

    
    hashedPswd = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db.session.commit()

    return redirect('/lab6/login')



@lab6.route('/lab6/login', methods=["GET", "POST"])
def login():

    errors=[]

    if request.method == "GET":
        return render_template("log_in.html", errors=errors)
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not (username_form or password_form):
        errors.append('Пожалуйста, заполните все поля')
        return render_template('log_in.html', errors=errors)

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect('/lab6/articles')
        else:
            errors.append('Неправильный пароль')
            return render_template('log_in.html', errors=errors)
    if my_user is None:
        errors.append('Пользователь не найден')
        return render_template('log_in.html', errors=errors)
    return render_template("log_in.html") 


@lab6.route('/lab6/articles')
@login_required
def article_list():
    my_articles = artickles.query.filter_by(user_id = current_user.id).all()
    print(my_articles)
    return render_template('check_notes.html', lists=my_articles)


@lab6.route('/lab6/new_articles', methods=["GET", "POST"])
@login_required
def add_article():

    errors = []

    if request.method == 'GET':
        return render_template('add_note.html')
    

    text_article = request.form.get('text_article')
    title = request.form.get('title_article')
    user_id = current_user.id


    if len(text_article) == 0:
        errors.append('Заполните текст')
        return render_template('add_note.html', errors = errors)
    
    newArticle = artickles(title=title, article_text=text_article, user_id=user_id)

    db.session.add(newArticle)
    db.session.commit()

    return redirect("/lab5/articles")


@lab6.route('/lab6/logout')
@login_required
def logout():
    logout_user()
    return redirect ('/lab6')


@lab6.route('/lab6/articles/<int:article_id>')
@login_required
def seeArticle(article_id):
    my_article = artickles.query.filter_by(id=article_id).first()

    if current_user.id == my_article.user_id:
        return render_template('articleN_orm.html', article_text = my_article.article_text, article_title = my_article.title)
    else:
        return render_template("log_in.html") 

