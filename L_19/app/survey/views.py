from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from app.auth.views import login_required

from app.db.survey_logic import LogicProvider as SurveyLogicProvider

survey_logic = SurveyLogicProvider('raw')

survey_bp = Blueprint('survey', name, template_folder='templates', url_prefix='')

@survey_bp.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        surveys = survey_logic.get_all_surveys()

        return render_template('surveys.html', all_surveys=surveys)
    raise Exception('Invalid method')

@survey_bp.route('/create-survey', methods=['GET', 'POST'])
@login_required
def create_survey():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        is_anonymous = bool(request.form.get('is_anonymous', False))
        created_by = session.get('user_id')
        survey_input = {
            'title': title,
            'description': description,
            'is_anonymous': is_anonymous,
            'created_by': created_by
        }
        survey = survey_logic.create_survey(**survey_input)
        flash('Survey created successfully! Add options')
        return redirect(url_for('survey.add_option', survey_id=survey['id']))
    return render_template('create_survey.html')

@survey_bp.route('/survey/<int:survey_id>', methods=['GET'])
def get_survey(survey_id):
    user_id = session.get('user_id')
    user_ip = request.remote_addr

    user_voted = survey_logic.is_already_voted(survey_id, user_id, user_ip)
    survey = survey_logic.get_survey(survey_id)
    options = survey_logic.get_survey_options(survey_id)
    context = {
        "survey": survey,
        "options": options,
        "is_voted": user_voted
    }

    return render_template('survey.html', **context)

@survey_bp.route('/submit_vote', methods=['POST'])
def submit_vote():
    survey_id = request.form['survey_id']
    user_id = session.get('user_id')  # user_id is optional
    voter_ip = request.remote_addr
    option_id = request.form.get('option')
    option_ids = [option_id] if option_id else request.form.getlist('options')

    if not option_ids:
        flash('Please select option to vote.')
        return redirect(url_for('survey.get_survey', survey_id=survey_id))

    vote_input = {
        'survey_id': survey_id,
        'user_id': user_id,
        'voter_ip': voter_ip,
        'option_id': option_id,
        'option_ids': option_ids
    }
    survey_logic.create_vote(**vote_input)

    flash('Vote cast successfully!')
    return redirect(url_for('survey.get_survey', survey_id=survey_id))

@survey_bp.route('/survey/<int:survey_id>/votes', methods=['GET'])
def get_votes_for_survey(survey_id):
    votes = survey_logic.get_votes_for_survey(survey_id)
    return render_template('votes.html', votes=votes, survey={"id": survey_id})

@survey_bp.route('/add-option/<int:survey_id>', methods=['GET', 'POST'])
def add_option(survey_id):
    if request.method == 'POST':
        description = request.form['description']
        survey_id = request.form['survey_id']
        survey_logic.add_option(survey_id, description)
        flash('Option added successfully!')
        return redirect(url_for('survey.add_option', survey_id=survey_id))

    options = survey_logic.get_survey_options(survey_id)

    return render_template('add_option.html', survey_id=survey_id, options=options)

@survey_bp.route('/delete-survey/<int:survey_id>', methods=['POST'])
def delete_survey(survey_id):
    survey_logic.delete_survey(survey_id)
    flash('Survey deleted successfully!')
    return redirect(url_for('survey.index'))
