
import random

class MaybeCls:

    def __init__(self):
        self.__truthiness = 0.5
        self.__basket = [True, False]

    def __bool__(self):
        return random.choice(self.__basket)

    def __call__(self):
        return random.choice(self.__basket)

    def __eq__(self, other):
        return random.choice(self.__basket) == other

    def __str__(self):
        return str(random.choice(self.__basket))

    def __repr__(self):
        return str(random.choice(self.__basket))

    @property
    def truthiness(self):
        return self.__truthiness

    @truthiness.setter
    def truthiness(self, value):
        if value <= 0 or value >= 1:
            raise ValueError("Truthiness cannot be negative and should be between [0;1]")
        self.__truthiness = value
        self.__basket = MaybeCls.prepare_basket(self.__truthiness)

    @staticmethod
    def prepare_basket(truthiness_factor: float) -> list[int]:
        basket = []
        num_of_true_objects = int(truthiness_factor * 100)
        num_of_false_objects = 100 - num_of_true_objects

        for _ in range(0, num_of_true_objects):
            basket.append(True)

        for _ in range(0, num_of_false_objects):
            basket.append(False)

        return basket



Maybe = MaybeCls()
