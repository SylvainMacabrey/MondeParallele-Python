########################## classe BaseGraph ###########################

import matplotlib as mil
mil.use('TkAgg')
import matplotlib.pyplot as plt

class BaseGraph:
    
    def __init__(self):
        self.title = "Your graph title"
        self.x_label = "X-axis label"
        self.y_label = "X-axis label"
        self.show_grid = True

    def show(self, zones):
        # x_values = gather only x_values from our zones
        # y_values = gather only y_values from our zones
        x_values, y_values = self.xy_values(zones)
        plt.plot(x_values, y_values, '.')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()

    def xy_values(self, zones):
        raise NotImplementedError