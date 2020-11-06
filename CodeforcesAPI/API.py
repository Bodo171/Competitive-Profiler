import requests


class API:
    DOMAIN = 'https://codeforces.com/api/'

    @staticmethod
    def get_request(url,**arguments):
        response = requests.get(API.DOMAIN+url,params=arguments).json()
        if response['status']!='OK':
            raise Exception('Codeforces did not respond')
        return response['result']
