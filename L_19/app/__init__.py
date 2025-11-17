from flask import Flask

from auth.views import auth_bp
from survey.views import survey_bp


def create_app():
    app = Flask(__name__)

    from .commands.raw_commands import init_commands
    init_commands(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(survey_bp)

    return app
