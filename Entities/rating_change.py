from datetime import datetime


class RatingChange:
    def __init__(self, **kwargs):
        self._contest_id = kwargs['contestId']
        self._contest_name = kwargs['contestName']
        self._handle = kwargs['handle']
        self._rank = kwargs['rank']
        self._time = datetime.utcfromtimestamp(kwargs['ratingUpdateTimeSeconds'])
        self._old_rating = kwargs['oldRating']
        self._new_rating = kwargs['newRating']

    def get_new_rating(self):
        return self._new_rating

    def get_time(self):
        return self._time
