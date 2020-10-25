from datetime import datetime
from Entities.problem import Problem


class Submission:
    def __init__(self,**kwargs):
        self.time = datetime.utcfromtimestamp(kwargs['creationTimeSeconds'])
        self.verdict = kwargs['verdict']
        self.problem = Problem(**kwargs['problem'])

    def get_time(self):
        return self.time

    def get_verdict(self):
        return self.verdict

    def get_problem(self):
        return self.verdict

    def get_tags(self):
        return self.problem.get_tags()
