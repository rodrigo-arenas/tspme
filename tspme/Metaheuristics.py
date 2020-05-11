class SimulatedAnnealing:

    def __init__(self, init_temp=0.05, alpha=0.995, stop_temp=0.5, n_cycles=100):
        self.init_temp = init_temp
        self.alpha = alpha
        self.stop_temp = stop_temp
        self.n_cycles = n_cycles
