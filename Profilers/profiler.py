from datetime import date
from settings import Settings
from abc import abstractmethod


class Profiler:
    @abstractmethod
    def _get_insights_for_filtered(self, criteria):
        """
        Criteria provides a filter condition for the list of entities
        Returns a dictionary which has values which describe certain attributes of the filtered
        set
        """
        pass

    def get_yearly_report(self):
        """
          Creates a report for profiled entities grouped by year, that contains
          the attributes provided by _get_insights_for_filtered
          The filtered entities must have a get_time attribute which returns a datetime or date object
        """
        ans = dict()

        for year in range(Settings.CF_OPENED_YEAR, date.today().year+1):
            current_year_stats = self._get_insights_for_filtered(lambda entity: entity.get_time().year == year)
            if current_year_stats:
                ans[year] = current_year_stats

        return ans
