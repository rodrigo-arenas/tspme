import numpy as np
import random
import functools
import operator
from sklearn.metrics.pairwise import euclidean_distances
from tspme.utils.CustomerProperties import LazyProperty


class SimulatedAnnealing:

    def __init__(self, init_temp=0.05, alpha=0.995, stop_temp=0.5, n_cycles=50):
        self.init_temp = init_temp
        self.alpha = alpha
        self.stop_temp = stop_temp
        self.n_cycles = n_cycles
        self.steps = None
        self.x = None
        self.y = None
        self.cost_matrix = None
        self.locations_generator = None
        self.solutions_size = None
        self.cost_hist = None
        self.solution = None
        self.callback = None

    def distance_matrix(self, locations_generator):
        self.locations_generator = locations_generator
        self.cost_matrix = euclidean_distances(self.locations_generator["locations"])
        return self.cost_matrix

    @LazyProperty
    def size(self):
        return len(self.locations_generator["x"])

    def tour_len(self, tour):
        return np.sum(self.cost_matrix[tour[i]][tour[i + 1]] for i in range(self.size - 1))

    def opt2(self, route):
        new_route = route.copy()
        crossover_points = random.sample(range(self.size), 2)
        _init_pos, _end_pos = min(crossover_points), max(crossover_points)
        new_route = [new_route[:_init_pos], new_route[_init_pos:_end_pos][::-1], new_route[_end_pos:]]
        return np.hstack(new_route).astype(int)

    def fit(self, return_cost_hist=False):
        current_solution = random.sample(range(self.size), self.size)
        current_len = self.tour_len(current_solution)
        t = 0.05 * self.tour_len(current_solution)
        self.n_cycles * int(np.log(self.init_temp / t) / np.log(self.alpha) + 1)
        n_iterations = self.solutions_size = int(np.log(self.init_temp / t) / np.log(self.alpha) + 2)
        self.cost_hist = [self.tour_len(current_solution)]

        k = 0
        while t > self.stop_temp:
            for i in enumerate(range(self.n_cycles)):
                acceptance_threshold = random.random()
                candidate = self.opt2(current_solution)
                candidate_len = self.tour_len(candidate)
                if candidate_len < current_len or acceptance_threshold < np.exp(-(candidate_len - current_len) / t):
                    current_solution = candidate
                    current_len = candidate_len
            k += 1
            if return_cost_hist:
                self.cost_hist.append(current_len)
            t *= self.alpha
        self.solution = current_solution
        self.callback = {"solution": self.solution,
                         "cost": current_len,
                         "n_iterations": n_iterations}
        if return_cost_hist:
            self.callback["cost_hist"] = self.cost_hist

        return self.callback
