from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect('signup')


@main.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html', name=current_user.name)
