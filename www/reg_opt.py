from www.orm import UserData, db
import logging


def do_reg(request):
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    logging.info('username:%s,password:%s,email:%s' % (username, password, email))
    db.session.add(UserData(username, password, email))
    db.session.commit()


def do_login(request):
    username = request.form['username']
    password = request.form['password']
    user = UserData.query.filter_by(username=username).all()
    if user and user[0] and user[0].password == password:
        logging.info('[用户登录]用户信息：%s' % user[0])
        return username
    return 'failed'
