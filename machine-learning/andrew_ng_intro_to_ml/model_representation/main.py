# This model representation was inspired by the papers "C1_W1_Lab02_Model_Representation_Soln" and "C1_W1_Lab03_Cost_function_Soln"

import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    """
        Class representation of the functionality of linear regression
    """

    def __init__(self, x, y, w, b):
        """
        Args:
          x (ndarray (m,)): Data, m examples
          y (ndarray (m,)): target values
          w (scalar): model parameter, represents the slope of the line
          b (scalar): model parameter, represents the y-intercept of the line
        """
        self.x = x
        self.y = y
        self.w = w
        self.b = b

    def visualize_data(self):
        """
        Used to visualize data points without the line
        """
        # Plot the data points
        plt.scatter(self.x, self.y, marker='x', c='r')
        # Set the title
        plt.title("Housing Prices")
        # Set the y-axis label
        plt.ylabel('Price (in 1000s of dollars)')
        # Set the x-axis label
        plt.xlabel('Size (1000 sqft)')
        plt.show()

    def compute_model_output(self):
        """
                Computes the prediction of a linear model
                Args:
                 x (ndarray (m,)): Data, m examples
                 w,b (scalar) : model parameters
                Returns
                 f_wb (ndarray (m,)): model prediction
            """
        m = self.x.shape[0]
        f_wb = np.zeros(m)
        print(f"f_wb = {f_wb}", m)
        for i in range(m):
            f_wb[i] = self.w * self.x[i] + self.b

        self._visualize_model_output(f_wb)

    def _visualize_model_output(self, prediction):
        """
        Used to visualize the data with its computed line
        """
        # Plot our model prediction
        plt.plot(self.x, prediction, c='b', label='Our Prediction')
        # Plot the data points
        plt.scatter(self.x, self.y, marker='x', c='r', label='Actual Values')
        # Set the title
        plt.title("Housing Prices")
        # Set the y-axis label
        plt.ylabel('Price (in 1000s of dollars)')
        # Set the x-axis label
        plt.xlabel('Size (1000 sqft)')
        plt.legend()
        plt.show()

    def compute_cost(self):
        """
        Computes the cost function for linear regression.

        Args:
          x (ndarray (m,)): Data, m examples
          y (ndarray (m,)): target values
          w,b (scalar) : model parameters

        Returns
            total_cost (float): The cost of using w,b as the parameters for linear regression
        """

        # number of training examples
        m = self.x.shape[0]
        cost_sum = 0

        for i in range(m):
            f_wb = self.w * self.x[i] + self.b
            cost = (f_wb - self.y[i]) ** 2
            cost_sum = cost_sum + cost

        total_cost = (1 / (2 * m)) * cost_sum
        return total_cost
