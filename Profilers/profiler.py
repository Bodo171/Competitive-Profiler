from datetime import date
from settings import Settings
from abc import abstractmethod


class Profiler:
    @abstractmethod
    def _get_insights_for_filtered(self, criteria):
        pass

    def get_yearly_report(self):
        ans = dict()

        for year in range(Settings.CF_OPENED_YEAR, date.today().year+1):
            current_year_stats = self._get_insights_for_filtered(lambda x: x.get_time().year == year)
            if current_year_stats:
                ans[year] = current_year_stats

        return ans
