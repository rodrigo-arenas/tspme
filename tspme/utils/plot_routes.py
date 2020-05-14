import matplotlib.pyplot as plt


def plot_cities(cities: dict = None, figsize=(8, 6), **kwargs):
    fig = plt.figure(figsize=figsize)
    plt.scatter(cities['x'], cities['y'], c='black', alpha=0.5, **kwargs)
    return fig


def plot_routes(cities: dict = None, solution: dict = None, figsize=(8, 6), **kwargs):
    fig = plt.figure(figsize=figsize)
    index = solution['route']
    x = cities['x'][index]
    y = cities['y'][index]
    plt.plot(x, y, '-o', c='black', alpha=0.5, **kwargs)
    plt.title('Final Solution Route')
    return fig


def plot_history(solution: dict = None, figsize=(8, 6)):
    fig = plt.figure(figsize=figsize)
    hist = solution['cost_hist']
    plt.plot(hist, '-', c='black', alpha=0.5)
    plt.xlabel('Iteration')
    plt.ylabel('Cost')
    plt.title('Cost evolution')
    return fig


