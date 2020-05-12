import numpy as np
import random
from sklearn.metrics.pairwise import euclidean_distances
from tspme.utils.CustomerProperties import LazyProperty


class SimulatedAnnealing:

    def __init__(self, init_temp=0.05, alpha=0.995, stop_temp=0.5, n_cycles=100):
        self.init_temp = init_temp
        self.alpha = alpha
        self.stop_temp = stop_temp
        self.n_cycles = n_cycles
        self.x = None
        self.y = None
        self.cost_matrix = None
        self.locations_generator = None

    def distance_matrix(self, locations_generator):
        self.locations_generator = locations_generator
        self.cost_matrix = euclidean_distances(self.locations_generator["locations"])
        return self.cost_matrix

    @LazyProperty
    def size(self):
        return len(self.locations_generator["x"])

    def tour_len(self, tour):
        return np.sum(self.cost_matrix[tour[i]][tour[i+1]] for i in range(self.size-1))







