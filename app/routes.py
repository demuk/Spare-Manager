from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegisterForm, AddSpareForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Spare, User
from werkzeug.urls import url_parse


@app.route('/index', methods=['POST','GET'])
@app.route('/', methods=['POST', 'GET'])
@login_required
def index():
    title = 'HOME'
    return render_template('index.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/addspare', methods=['GET', 'POST'])
@login_required
def addspare():
    form = (AddSpareForm)
    if form.validate_on_submit():
        spare = Spare(brand=form.brand.data, model=form.model.data, code=form.code.data, description=form.description.data, 
            location=form.location.data)
        db.session.add(spare)
        db.session.commit()
        flash('Spare has been successfully added')
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form)