import matplotlib.pyplot as plt
from tspme.utils.routes_generator import RandomRouteGenerator
from tspme.utils.plot_routes import plot_routes, plot_history
from tspme.metaheuristics import SimulatedAnnealing


SIZE = 100
route_generator = RandomRouteGenerator(size=SIZE)
routes = route_generator.generate()

sa = SimulatedAnnealing()
sa.set_distance_matrix(routes)
solution = sa.fit(return_cost_hist=True)
print(solution)
plot_routes(cities=routes, solution=solution)
plot_history(solution=solution)
plt.show()





