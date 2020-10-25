from CodeforcesAPI.API import API


class UserAPI:
    @staticmethod
    def get_contests(user: str):
        return API.get_request('user.rating', handle=user)

    @staticmethod
    def get_submissions(user: str):
        return API.get_request('user.status', handle=user)

