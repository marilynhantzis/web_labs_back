from flask import Blueprint, render_template, request, abort, jsonify

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9')
def main():
    return render_template('/lab9/index.html')

@lab9.errorhandler(404)
def not_found(err):
    return 'нет такой страницы', 404
