from flask import Blueprint, redirect, url_for, render_template
lab3 = Blueprint('lab3',__name__)


@lab3.route("/lab3")
def labb3():
    return render_template('lab3.html')