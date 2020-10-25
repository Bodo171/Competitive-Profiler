from datetime import datetime


class RatingChange:
    def __init__(self, **kwargs):
        self.contest_id = kwargs['contestId']
        self.contest_name = kwargs['contestName']
        self.handle = kwargs['handle']
        self.rank = kwargs['rank']
        self.time = datetime.utcfromtimestamp(kwargs['ratingUpdateTimeSeconds'])
        self.old_rating = kwargs['oldRating']
        self.new_rating = kwargs['newRating']

    def get_new_rating(self):
        return self.new_rating

    def get_time(self):
        return self.time
