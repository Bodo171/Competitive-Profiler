from datetime import date

from Profilers.user_submission_profiler import UserSubmissionProfiler
from Profilers.user_rating_profiler import UserRatingProfiler
from settings import Settings


class UserProfiler:

    def __init__(self, username):
        self._user = username
        self._submission_profiler = UserSubmissionProfiler(username)
        self._rating_profiler = UserRatingProfiler(username)

    def get_yearly_report_table(self):
        """
           Creates a report of the user stored in the object, which contains
           yearly submission and rating data.
           The report is returned as a dictionary list with the fields:
               - year
               - firstChange (integer), lastChange (integer), averageChange(float)
               - favouriteTopics (list of strings)
        """
        submission_data = self._submission_profiler.get_yearly_report()
        rating_data = self._rating_profiler.get_yearly_report()
        report = list()
        fields = ['firstChange', 'lastChange', 'maxChange', 'averageChange', 'favouriteTopics']

        for year in range(Settings.CF_OPENED_YEAR, date.today().year+1):
            yearly_submissions = submission_data.get(year, None)
            yearly_ratings = rating_data.get(year, None)

            if yearly_submissions or yearly_ratings:
                yearly = dict()
                for field in fields:
                    yearly[field] = 'Inactive'
                yearly['year'] = year

                if yearly_submissions:
                    yearly.update(**yearly_submissions)

                if yearly_ratings:
                    yearly.update(**yearly_ratings)

                report.append(yearly)

        return report
