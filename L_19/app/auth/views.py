from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash

import functools

from app.db.user_logic import LogicProvider as UserLogicProvider

user_logic = UserLogicProvider('orm')


auth_bp = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('loggedin') is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view

# ########### Registration ###########
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        user_input = {'user_name': user_name, 'password': password}

        user_logic.create_user(**user_input)

        flash('User created successfully!')
        return redirect(url_for('auth.login'))
    return render_template('registration.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']

        user = user_logic.get_user(user_name)
        user_id, user_name, user_password = user.values()

        if check_password_hash(user_password, password):
            session['user_id'] = user_id
            session['user_name'] = user_name
            session['loggedin'] = True
            return redirect(url_for('survey.index'))
        else:
            flash('Incorrect username or password!')
    return render_template('login.html')


@auth_bp.route('/logout', methods=['GET'])
def logout():
    # session.clear()
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('auth.login'))
