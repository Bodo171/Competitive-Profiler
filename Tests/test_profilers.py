import pytest
from CodeforcesAPI import UserAPI
from Profilers import UserRatingProfiler
from datetime import datetime

@pytest.fixture
def standard_user():
    return 'user'


@pytest.fixture
def standard_contest(standard_user, new_rating=1500, contest_time=datetime(2020, 1, 1)):
    return dict(
            contestId=766,
            contestName='Codeforces Round #396 (Div. 2)',
            handle=standard_user,
            rank= 142,
            ratingUpdateTimeSeconds = contest_time.timestamp(),
            oldRating=1500,
            newRating=new_rating,
    )


@pytest.fixture
def mock_CodeforcesAPI(monkeypatch, standard_contest):
    def mock_get_contests(user):
        return [standard_contest]
    monkeypatch.setattr(UserAPI, 'get_contests', mock_get_contests)


def test_user_rating_profiler(mock_CodeforcesAPI, standard_user, standard_contest):
    profiler = UserRatingProfiler(username=standard_contest.get('user'))
    report = profiler.get_yearly_report()

    assert len(report) == 1
    assert report.get(2019).get('lastChange') == standard_contest.get('newRating')