from .raw_data_provider import RawDataProvider


class LogicProvider:
    def __init__(self, provider):
        self.data_provider = RawDataProvider

    def create_user(self, **kwargs):
        return self.data_provider.create_user(**kwargs)
    
    def get_user(self, user_name):
        return self.data_provider.get_user(user_name)