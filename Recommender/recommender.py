from sklearn.neighbors import KNeighborsClassifier

class Recommender:
    def __init___(self):
        self._engine = KNeighborsClassifier(algorithm='brute')

    #def train(self):
    #    self._engine.fit()