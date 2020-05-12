import numpy as np


class RandomRouteGenerator:
    """
    Generates random cities and distances for the TSP
    """
    def __init__(self, size: int = None, x_min: int = 0, x_max: int = 100, y_min: int = 0, y_max: int = 100):
        self.size = size
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.routes = None

    def __repr__(self):
        return f'<Random Route Generator with {self.size} cities>'

    def generate(self):
        self.routes = dict({"x": np.random.randint(low=self.x_min, high=self.x_max, size=self.size),
                            "y": np.random.randint(low=self.x_min, high=self.x_max, size=self.size)})
        self.routes["locations"] = [[self.routes["x"][i], self.routes["y"][i]] for i in range(self.size)]
        return self.routes


