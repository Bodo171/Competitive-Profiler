from Profilers.profiler import Profiler
from CodeforcesAPI import UserAPI
from Entities import Submission
from enums import CFVerdict


class UserSubmissionProfiler(Profiler):
    def __init__(self, username, fetch=True):
        self._user = username
        if fetch:
            self._submissions = self._fetch_submissions(UserAPI.get_submissions(self._user))

    @staticmethod
    def _fetch_submissions(submissions_data):
        return [Submission(**submission) for submission in submissions_data]

    def get_most_solved_topics(self, submissions=None):
        if not submissions:
            submissions=self._submissions

        count = dict()

        for submission in submissions:
            if submission.get_verdict() == CFVerdict.OK:
                for tag in submission.get_tags():
                    count[tag] = count.get(tag, 0)+1

        sorted_list = list(count.items())
        sorted_list.sort(key=lambda item: item[1], reverse=True)

        return [element[0] for element in sorted_list]

    def _get_insights_for_filtered(self, criteria):
        """
        Takes all the submissions satisfying "criteria"
        Returns a dict with the following information:
            favouriteTopics: list of at most 3 topics with most accepted submissions
        """
        filtered = [submission for submission in self._submissions if criteria(submission)]
        if filtered:
            favourite_topics = self.get_most_solved_topics(submissions=filtered)[:3]
            return dict(favouriteTopics=favourite_topics)
        return dict()


