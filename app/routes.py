from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm



@app.route('/index', methods=['POST','GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    title = 'HOME'
    return render_template('index.html', title=title)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)