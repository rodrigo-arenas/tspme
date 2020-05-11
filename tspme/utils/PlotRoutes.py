import matplotlib.pyplot as plt


class TSPlot:
    """
    Plotting class for TSP solutions and cities selection
    """
    def __init__(self):
        pass

    @staticmethod
    def plot_cities(cities: dict = None, figsize=(8, 6), **kwargs):
        fig = plt.figure(figsize=figsize)
        plt.scatter(cities['x'], cities['y'], c='black', alpha=0.5, **kwargs)
        return fig

