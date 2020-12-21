from CodeforcesAPI.problemset import ProblemsetAPI
from Entities import Problem


class ProblemsetFetcher:
    @staticmethod
    def fetch_problems():
        problems_json = ProblemsetAPI.get_problems([])
        return [Problem(**problem_json) for problem_json in problems_json]

    # TO DO:check none to string
    @staticmethod
    def get_problems_to_csv(filename):
        file = open(filename,"w")
        problems = ProblemsetFetcher.fetch_problems()
        file.write('contest,problem,rating,tags\n')
        for problem in problems:
            file.write(problem.to_csv()+'\n')


