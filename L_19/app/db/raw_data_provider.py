from werkzeug.security import generate_password_hash

from .raw_connection import connect
from app.db import queries


class RawDataProvider:
    @staticmethod
    def create_survey(**kwargs):
        title, description, is_anonymous, created_by = kwargs.values()
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.CREATE_SURVEY, (title, description, created_by, is_anonymous))
            survey = cursor.fetchone()
            conn.commit()
            return {
                'id': survey[0],
                'title': survey[1],
                'description': survey[2],
                'created_by': survey[3],
                'is_anonymous': survey[4]
            }
        
    @staticmethod
    def get_all_surveys():
        conn = connect()
        surveys = []

        with conn.cursor() as cursor:
            cursor.execute(queries.ALL_SURVEYS)
            raw_surveys = cursor.fetchall()

            for survey in raw_surveys:
                surveys.append({
                    'id': survey[0],
                    'title': survey[1],
                    'description': survey[2],
                    'created_by': survey[3],
                    'created_at': survey[4],
                    'is_anonymous': survey[5]
                })
        return surveys
    
    @staticmethod
    def get_survey(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_SURVEY, (survey_id,))
            survey = cursor.fetchone()
            return {
                'id': survey[0],
                'title': survey[1],
                'description': survey[2],
                'created_by': survey[3],
                'created_at': survey[4],
                'is_anonymous': survey[5],
                'user_name': survey[6]
            }
        
    @staticmethod
    def is_already_voted(survey_id, user_id, user_ip):
        conn = connect()
        with conn.cursor() as cursor:
            if user_id:
                cursor.execute(queries.CHECK_USER_VOTED, (survey_id, user_id))
                return bool(cursor.fetchone())
            
            else:
                cursor.execute(queries.CHECK_ANONYMOUS_USER_VOTED, (survey_id, user_ip))


    @staticmethod
    def get_survey_options(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_OPTIONS_FOR_SURVEY, (survey_id,))
            options = cursor.fetchall()
            return [{'id': option[0], 'description': option[1]} for option in options]
        
    @staticmethod
    def create_vote(**kwargs):
        survey_id, user_id, voter_ip, option_id, option_ids = kwargs.values()
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.CREATE_VOTE, (survey_id, user_id, voter_ip))
            vote_id = cursor.fetchone()[0]
            for option_id in option_ids:
                cursor.execute(queries.CREATE_VOTE_OPTIONS, (vote_id, option_id))
            conn.commit()
            return vote_id
        
    @staticmethod
    def get_votes_for_survey(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_VOTES_FOR_SURVEY, (survey_id,))
            votes = cursor.fetchall()
            return [{'description': vote[0], 'count': vote[1]} for vote in votes]
        
    @staticmethod
    def add_option(survey_id, description):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.CREATE_OPTION, (survey_id, description))
            conn.commit()

    @staticmethod
    def delete_survey(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.DELETE_SURVEY, (survey_id,))
            conn.commit()

    @staticmethod
    def create_user(**kwargs):
        user_name, password = kwargs.values()

        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.CREATE_USER, (user_name, generate_password_hash(password)))
            conn.commit()

    @staticmethod
    def get_user(user_name):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_USER_BY_USERNAME, (user_name,))
            user_id, user_name, user_password = cursor.fetchone()

            return {
                'id': user_id,
                'user_name': user_name,
                'password': user_password
            }

