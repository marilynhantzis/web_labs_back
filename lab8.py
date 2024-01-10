from flask import Blueprint, render_template, request, abort

lab7 = Blueprint('lab7', __name__)

@lab8.route('/lab8')
def main():
    return render_template('/lab8/index.html')