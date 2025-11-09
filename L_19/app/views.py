import functools
from flask import request, render_template, redirect, url_for, session, flash
from app.config import SECRET_KEY
from werkzeug.security import generate_password_hash, check_password_hash

from .db.raw_connection import connect, close_connection
from .db import queries


def init_views(app, provider='raw'):
    app.teardown_appcontext(close_connection)
    app.secret_key = SECRET_KEY

    survey_logic = R if provider == 'raw'
    def login_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if session.get('loggedin') is None:
                return redirect(url_for('login'))
            return view(**kwargs)
        return wrapped_view

    @app.route("/")
    def index():
        if request.method == 'GET':
            conn = connect()
            with conn.cursor() as cursor:
                cursor.execute(queries.ALL_SURVEYS)
                surveys = cursor.fetchall()          
            return render_template('surveys.html', all_surveys=surveys)         
        raise Exception('Invalid method')
    
    @app.route('/create-survey', methods=['GET', 'POST'])
    @login_required
    def create_survey():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            is_anonymous = True if 'on' == request.form.get('is_anonymous', False) else False
            created_by = session.get('user_id')
            conn = connect()
            with conn.cursor() as cursor:
                cursor.execute(queries.CREATE_SURVEY, (title, description, created_by, is_anonymous))
                result = cursor.fetchone()
                conn.commit()
            flash('Survey created successfully! Add options')
            return redirect(url_for('add_option', survey_id=result[0]))
        return render_template('create_survey.html')
    
    @app.route('/add-option/<int:survey_id>', methods=['GET', 'POST'])
    def add_option(survey_id):
        if request.method == 'POST':
            description = request.form['description']
            survey_id = request.form['survey_id']
            conn = connect()
            with conn.cursor() as cursor:
                cursor.execute(queries.CREATE_OPTION, (survey_id, description))
                conn.commit()
            flash('Option added successfully!')
            return redirect(url_for('add_option', survey_id=survey_id))

        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_OPTIONS_FOR_SURVEY, (survey_id,))
            options = cursor.fetchall()

        return render_template('add_option.html', survey_id=survey_id, options=options)
    
    @app.route('/survey/<int:survey_id>', methods=['GET'])
    @login_required
    def get_survey(survey_id):
        user_id = session.get('user_id')
        user_ip = request.remote_addr
        is_voted = False

        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_SURVEY, (survey_id,))
            survey = cursor.fetchone()

            cursor.execute(queries.GET_OPTIONS_FOR_SURVEY, (survey_id,))
            options = cursor.fetchall()

            if user_id:
                cursor.execute(queries.CHECK_USER_VOTED, (survey_id, user_id,))
                is_voted = bool(cursor.fetchone())

            if not user_id and user_ip:
                cursor.execute(queries.CHECK_ANONYMOUS_USER_VOTED, (survey_id, user_ip,))
                is_voted = bool(cursor.fetchone())

            context = {
                'survey': survey,
                'options': options,
                'is_voted': is_voted
            }

            return render_template('survey.html', **context)
    
    @app.route('/submit_vote', methods=['POST'])
    def submit_vote():
        survey_id = request.form['survey_id']
        options_ids = request.form.getlist('options')
        voter_ip = request.remote_addr
        user_id = session.get('user_id')

        if not options_ids:
            flash('Please select option to vote.')
            return redirect(url_for('get_survey', survey_id=survey_id))
        
        conn = connect()
        with conn.cursor() as cursor:
            if user_id:
                cursor.execute(queries.CREATE_VOTE, (survey_id, user_id, None))
                vote_id = cursor.fetchone()[0]

            if not user_id and voter_ip:
                cursor.execute(queries.CREATE_VOTE, (survey_id, None, vote_id))
                vote_id = cursor.fetchone()[0]

            for option_id in options_ids:
                cursor.execute(queries.CREATE_VOTE_OPTIONS, (vote_id, option_id))

        conn.commit()

        flash('Vote submitted')
        return redirect(url_for('get_survey', survey_id=survey_id))
   
    @app.route('/survey/<int:survey_id>/votes', methods=['GET'])
    def get_votes_for_survey(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_VOTES_FOR_SURVEY, (survey_id,))
            votes = cursor.fetchall()
            cursor.execute(queries.GET_SURVEY, (survey_id,))
            survey = cursor.fetchone()
        return render_template('votes.html', votes=votes, survey=survey)
    
    @app.route('/delete-survey/<int:survey_id>', methods=['POST'])
    def delete_survey(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.DELETE_SURVEY, (survey_id,))
            conn.commit()
        flash('Survey deleted successfully!')
        return redirect(url_for('index'))
    
    # ######### Registration ##########
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            user_name = request.form['user_name']
            password = request.form['password']
            conn = connect()
            with conn.cursor() as cursor:
                cursor.execute(queries.CREATE_USER, (user_name, generate_password_hash(password)))
                conn.commit()
            flash('User created successfully!')
            return redirect(url_for('login'))
        return render_template('registration.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user_name = request.form['user_name']
            password = request.form['password']

            conn = connect()
            with conn.cursor() as cursor:
                cursor.execute(queries.GET_USER_BY_USERNAME, (user_name,))
                user_id, user_name, user_password = cursor.fetchone()
                if check_password_hash(user_password, password):
                    session['user_id'] = user_id
                    session['user_name'] = user_name
                    session['loggedin'] = True
                    return redirect(url_for('index'))
                else:
                    flash('Incorrect username or password!')
        return render_template('login.html')

    @app.route('/logout', methods=['GET'])
    def logout():
        # session.clear()
        session.pop('loggedin', None)
        session.pop('user_id', None)
        session.pop('username', None)
        return redirect(url_for('login'))

