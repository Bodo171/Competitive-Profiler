from Entities import *


def test_problem():
    problem = Problem(contestId=1,name='Name',rating=10,tags=['DP','Data Structures'])

    assert len(problem.get_tags()) == 2
    assert problem.get_contest() == 1
    assert problem.get_name() == 'Name'
    assert problem.get_rating() == 10


def test_problem_no_rating():
    problem = Problem(contestId=1, name='Name', tags=['DP', 'Data Structures'])

    assert not problem.get_rating()
