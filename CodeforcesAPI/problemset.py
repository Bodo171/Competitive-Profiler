from CodeforcesAPI.API import API


class ProblemsetAPI:
    @staticmethod
    def get_problems(tags: list):
        return API.get_request('problemset.problems', tags=';'.join(tags))