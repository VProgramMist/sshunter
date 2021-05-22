from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    second_name = request.form.get('second-name')
    gosb = request.form.get('gosb')
    vsp = request.form.get('vsp')
    position = request.form.get('position')
    username = request.form.get('login')
    password = request.form.get('password')

    user = User.query.filter_by(login=username).first()

    if user:
        flash('Данный логин уже зарегистрирован!')
        return redirect(url_for('auth.signup'))

    new_user = User(
        login=username,
        name=name,
        second_name=second_name,
        gosb=gosb,
        vsp=vsp,
        position=position,
        password=generate_password_hash(password, method='sha256'),
    )

    db.session.add(new_user)
    db.session.commit()

    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(login=username).first()
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('login')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(login=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Пожалуйста, проверьте ваш логин/пароль и попробуйте снова.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))
