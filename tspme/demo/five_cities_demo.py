import random
import numpy as np
from tspme.utils.RoutesGenerator import RandomRouteGenerator
from tspme.Metaheuristics import SimulatedAnnealing

SIZE = 5
route_generator = RandomRouteGenerator(size=SIZE)
routes = route_generator.generate()

sa = SimulatedAnnealing()
sa.distance_matrix(routes)
print(routes)
initial_solution = random.sample(range(SIZE), SIZE)
print(sa.size)
print(initial_solution)

