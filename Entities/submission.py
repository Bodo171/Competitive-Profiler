from datetime import datetime
from Entities.problem import Problem


class Submission:
    def __init__(self, **kwargs):
        self._time = datetime.utcfromtimestamp(kwargs['creationTimeSeconds'])
        self._verdict = kwargs['verdict']
        self._problem = Problem(**kwargs['problem'])

    def get_time(self):
        return self._time

    def get_verdict(self):
        return self._verdict

    def get_problem(self):
        return self._verdict

    def get_tags(self):
        return self._problem.get_tags()
