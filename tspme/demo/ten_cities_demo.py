import random
import numpy as np
from tspme.utils.RoutesGenerator import RandomRouteGenerator
from tspme.Metaheuristics import SimulatedAnnealing

SIZE = 10
route_generator = RandomRouteGenerator(size=SIZE)
routes = route_generator.generate()

sa = SimulatedAnnealing()
sa.distance_matrix(routes)
solution = sa.fit()
print(solution)


