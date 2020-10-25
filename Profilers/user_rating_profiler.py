from Profilers.profiler import Profiler
from CodeforcesAPI import UserAPI
from Entities import RatingChange


class UserRatingProfiler(Profiler):
    """
      Creates statistics about an user's rating
      Based on the user's rating changes
    """

    def __init__(self, username):
        self.user = username
        self._contests = self._fetch_contests(UserAPI.get_contests(self.user))

    @staticmethod
    def _fetch_contests(contests_data):
        return [RatingChange(**contest) for contest in contests_data]

    def _get_insights_for_filtered(self, criteria):
        """"
            Takes all rating changes of the user, satisfying "criteria"
            Returns none if contestant was inactive
            Otherwise returns a dictionary with 3 fields:
            firstChange (integer), lastChange (integer), averageChange(float)
        """
        filtered = [contest for contest in self._contests if criteria(contest)]

        if len(filtered) == 0:
            return None

        def time_key(contest): return contest.get_time()

        first_change = min(filtered, key=time_key).get_new_rating()
        last_change = max(filtered, key=time_key).get_new_rating()

        max_change=max([contest.get_new_rating() for contest in filtered])

        average_change = round(sum(elem.get_new_rating() for elem in filtered) / len(filtered), 2)

        return dict(
            firstChange=first_change,
            lastChange=last_change,
            maxChange=max_change,
            averageChange=average_change,
        )
