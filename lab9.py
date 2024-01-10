from flask import Blueprint, render_template, request, abort, jsonify

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9')
def main1():
    return render_template('/lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/404.html'), 404

@lab9.route('/lab9/500')
def server_error():
    raise Exception("Произошла некоторая ошибка")

@lab9.app_errorhandler(Exception)
def er500(e):
   return render_template('lab9/500.html'), 500


@lab9.route('/lab9', methods=['GET', 'POST'])
def main():
    if request.method =='GET':
        return render_template('lab9/index.html')
    if request.method == 'POST':
        recipient_name = request.form.get("recipient_name")
        recipient_gender = request.form.get("recipient_gender")
        sender_name = request.form.get("sender_name")

        return render_template('lab9/post.html', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name)