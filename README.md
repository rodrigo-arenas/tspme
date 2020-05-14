# tspme
Python metaheuristics for Traveling Salesman Problem (TSP)

## Example

```python
import matplotlib.pyplot as plt
from tspme.utils.routes_generator import RandomRouteGenerator
from tspme.utils.plot_routes import plot_routes
from tspme.metaheuristics import SimulatedAnnealing


SIZE = 50
route_generator = RandomRouteGenerator(size=SIZE)
routes = route_generator.generate()

sa = SimulatedAnnealing()
sa.set_distance_matrix(routes)
solution = sa.fit(return_cost_hist=False)
print(solution)
plot_routes(cities=routes, solution=solution)
plt.show()

```

<img src="https://i.ibb.co/RgTPMLV/50-cities-solution.png" width="400"/>  <img src="https://i.ibb.co/KNSdrS8/100-cities-cost.png" width="400"/>



