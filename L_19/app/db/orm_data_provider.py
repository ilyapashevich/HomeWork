from werkzeug.security import generate_password_hash
from sqlalchemy import select, func, and_, or_
from app.db.orm_connection import get_session
from app.db.models import User, Survey, Option, Vote, VoteOption


class OrmDataProvider:
    @staticmethod
    def create_survey(**kwargs):
        with get_session() as session:
            survey = Survey(**kwargs)
            session.add(survey)
            session.commit()
            session.refresh(survey)

            return {
                'id': survey.id,
                'title': survey.title,
                'description': survey.description,
                'created_by': survey.created_by,
                'is_anonymous': survey.is_anonymous
            }

    @staticmethod
    def get_all_surveys():
        with get_session() as session:
            stmt = select(
                Survey.id,
                Survey.title,
                Survey.description,
                Survey.created_by,
                Survey.created_at,
                Survey.is_anonymous
            )

            results = session.execute(stmt).all()

            surveys = []
            for survey in results:
                surveys.append({
                    'id': survey.id,
                    'title': survey.title,
                    'description': survey.description,
                    'created_by': survey.created_by,
                    'created_at': survey.created_at,
                    'is_anonymous': survey.is_anonymous
                })

            return surveys

    @staticmethod
    def get_survey(survey_id):
        with get_session() as session:
            stmt = select(
                Survey.id,
                Survey.title,
                Survey.description,
                Survey.created_by,
                Survey.created_at,
                Survey.is_anonymous,
                User.user_name
            ).join(User, Survey.created_by == User.id).where(Survey.id == survey_id)

            result = session.execute(stmt).first()

            if not result:
                return None

            return {
                'id': result.id,
                'title': result.title,
                'description': result.description,
                'created_by': result.created_by,
                'created_at': result.created_at,
                'is_anonymous': result.is_anonymous,
                'user_name': result.user_name
            }

    @staticmethod
    def is_already_voted(survey_id, user_id, user_ip):
        with get_session() as session:
            if user_id:
                stmt = select(Vote.id).where(
                    and_(Vote.survey_id == survey_id, Vote.user_id == user_id)
                )
            else:
                stmt = select(Vote.id).where(
                    and_(Vote.survey_id == survey_id, Vote.voter_ip == user_ip)
                )

            result = session.execute(stmt).first()
            return bool(result)

    @staticmethod
    def get_survey_options(survey_id):
        with get_session() as session:
            stmt = select(Option.id, Option.description).where(Option.survey_id == survey_id)
            results = session.execute(stmt).all()

            return [{'id': option.id, 'description': option.description} for option in results]

    @staticmethod
    def create_vote(**kwargs):
        survey_id, user_id, voter_ip, option_id, option_ids = kwargs.values()
        with get_session() as session:
            # Создаем запись голоса
            vote = Vote(
                survey_id=survey_id,
                user_id=user_id,
                voter_ip=voter_ip
            )
            session.add(vote)
            session.flush()  # Получаем vote_id без коммита

            # Создаем связи с опциями
            for opt_id in option_ids:
                vote_option = VoteOption(
                    vote_id=vote.id,
                    option_id=opt_id
                )
                session.add(vote_option)

            session.commit()
            return vote.id
        
    @staticmethod
    def get_votes_for_survey(survey_id):
        with get_session() as session:
            stmt = select(
                Option.description,
                func.count(VoteOption.option_id).label('count')
            ).select_from(Option).join(
                VoteOption, Option.id == VoteOption.option_id
            ).join(
                Vote, VoteOption.vote_id == Vote.id
            ).where(
                Vote.survey_id == survey_id
            ).group_by(Option.id, Option.description)

            results = session.execute(stmt).all()

            return [{'description': result.description, 'count': result.count} for result in results]

    @staticmethod
    def add_option(survey_id, description):
        with get_session() as session:
            option = Option(
                survey_id=survey_id,
                description=description
            )
            session.add(option)

    @staticmethod
    def delete_survey(survey_id):
        with get_session() as session:
            stmt = select(Survey).where(Survey.id == survey_id)
            survey = session.execute(stmt).scalar_one_or_none()
            session.delete(survey)

    @staticmethod
    def create_user(**kwargs):
        user_name, password = kwargs.values()
        with get_session() as session:
            user = User(
                user_name=user_name,
                password_hash=generate_password_hash(password)
            )
            session.add(user)

    @staticmethod
    def get_user(user_name):
        with get_session() as session:
            stmt = select(User).where(User.user_name == user_name)
            user = session.execute(stmt).scalar_one_or_none()

            if not user:
                return None

            return {
                'id': user.id,
                'user_name': user.user_name,
                'password': user.password_hash
            }