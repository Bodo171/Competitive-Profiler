from copy import deepcopy


class Problem:
    def __init__(self,**kwargs):
        self._contest_id =kwargs.get('contestId',None)
        self._name = kwargs['name']
        self._rating = kwargs.get('rating', None)
        self._tags = kwargs['tags']

    def get_contest(self):
        return self._contest_id

    def get_name(self):
        return self._name

    def get_rating(self):
        return self._rating

    def get_tags(self):
        return deepcopy(self._tags)
