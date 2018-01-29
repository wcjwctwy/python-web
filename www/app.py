import logging

from flask import Flask, request, render_template, redirect, url_for
from www import reg_opt

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def find(name):
    return 'Hello %s' % name


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def do_register():
    reg_opt.do_reg(request)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_login():
    result = reg_opt.do_login(request)
    if result == 'failed':
        return render_template('login.html', message='用户名密码错误！！')
    else:
        return render_template('index.html', name=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
