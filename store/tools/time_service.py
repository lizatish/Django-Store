from datetime import datetime


class TimeService:
    def __init__(self):
        self.dt_template = '%Y-%m-%dT%H:%M:%S.%f'

    def get_datetime(self, dt):
        return datetime.strptime(dt[:-1], self.dt_template)

    def __get_time_slice(self, datetime_object):
        return datetime_object.strftime(self.dt_template)[:-4] + 'Z'

    def get_assign_time(self, dt=datetime.utcnow()):
        return self.__get_time_slice(dt)
