import matplotlib.pyplot as plt
from tspme.utils.RoutesGenerator import RandomRouteGenerator
from tspme.utils.PlotRoutes import plot_routes
from tspme.Metaheuristics import SimulatedAnnealing


SIZE = 50
route_generator = RandomRouteGenerator(size=SIZE)
routes = route_generator.generate()

sa = SimulatedAnnealing()
sa.set_distance_matrix(routes)
solution = sa.fit(return_cost_hist=False)
print(solution)
plot_routes(cities=routes, solution=solution)
plt.show()





