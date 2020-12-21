from sklearn.neighbors import KNeighborsClassifier
from pandas import Dataset, read_csv

from Recommender.recommender_settings import RecommenderSettings

class Recommender:
    def __init__(self):
        self._engine = KNeighborsClassifier(algorithm='brute')

    def train(self):
        problem_dataset = read_csv(RecommenderSettings.PROBLEM_DATASET_PATH)
        #self._engine.fit(problem_dataset,y)

    def get_recommended(self):
        pass
