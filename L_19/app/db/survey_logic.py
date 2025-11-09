from .raw_data_provider import RawDataProvider
from .orm_data_provider import OrmDataProvider


class LogicProvider:
    def init(self, provider):
        self.data_provider = RawDataProvider if provider == 'raw' else OrmDataProvider

    def create_survey(self, **kwargs):
        return self.data_provider.create_survey(**kwargs)

    def get_all_surveys(self):
        return self.data_provider.get_all_surveys()

    def get_survey(self, survey_id):
        return self.data_provider.get_survey(survey_id)

    def is_already_voted(self, survey_id, user_id, user_ip):
        return self.data_provider.is_already_voted(survey_id, user_id, user_ip)

    def get_survey_options(self, survey_id):
        return self.data_provider.get_survey_options(survey_id)

    def create_vote(self, **kwargs):
        return self.data_provider.create_vote(**kwargs)

    def get_votes_for_survey(self, survey_id):
        return self.data_provider.get_votes_for_survey(survey_id)

    def add_option(self, survey_id, description):
        return self.data_provider.add_option(survey_id, description)

    def delete_survey(self, survey_id):
        return self.data_provider.delete_survey(survey_id)