# This model representation was inspired by the papers "C1_W1_Lab02_Model_Representation_Soln" and "C1_W1_Lab03_Cost_function_Soln"

import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    """
        Class representation of the functionality of linear regression
    """

    def __init__(self, x, y):
        """
        Args:
          x (ndarray (m,)): Data, m examples
          y (ndarray (m,)): target values
          w (scalar): model parameter, represents the slope of the line
          b (scalar): model parameter, represents the y-intercept of the line
        """
        self.x = x
        self.y = y
        self.w = 0
        self.b = 0

    def visualize_data(self, title, x_label, y_label):
        """
        Used to visualize data points without the line
        """
        # Plot the data points
        plt.scatter(self.x, self.y, marker='x', c='r')
        # Set the title
        plt.title(title)
        # Set the y-axis label
        plt.ylabel(y_label)
        # Set the x-axis label
        plt.xlabel(x_label)
        plt.show()
        
    def fit_gradient_descent(self, alpha):
        w_gradient = 0
        b_gradient = 0
        
        for i in range(len(self.x)):
            w_gradient += -(2 / len(self.x)) * self.x[i] * (self.y[i] - (self.w * self.x[i] + self.b))
            b_gradient += -(2 / len(self.x)) * (self.y[i] - (self.w * self.x[i] + self.b))
        
        self.w = self.w - (alpha * w_gradient)
        self.b = self.b - (alpha * b_gradient)
        return self.w, self.b

    def fit_least_squares(self):
        """
        Finds the best fit line using the least squares method
        """
        # Find the centroids
        x_mean = np.mean(self.x)
        y_mean = np.mean(self.y)
        numerator = 0
        denaminator = 0
        
        for i in range(len(self.x)):
            x_part = self.x[i] - x_mean
            y_part = self.y[i] - y_mean
            numerator = numerator + (x_part * y_part)
            denaminator = denaminator + (x_part ** 2)
            print(numerator, denaminator)
        
        slope = numerator / denaminator
        intercept = y_mean - (slope * x_mean)
        
        self.w = slope
        self.b = intercept
        

        # Print the optimal parameters
        print("Optimal Parameters:")
        print("Slope (w):", self.w)
        print("Intercept (b):", self.b)

        # Compute and print the cost with the optimal parameters
        cost = self.compute_cost()
        print("Cost with Optimal Parameters:", cost)

        # Visualize the model output
        self.visualize_model_output()
        

    def predict_y(self, x):
        """
        Predicts the y value for a given x value
        """
        if self.w is None or self.b is None:
            print("Model not trained. Fit the model using fit_least_squares.")
            return None

        return self.w * x + self.b
    
    def predict_x(self, y):
        """
        Predicts the x value for a given y value
        """
        if self.w is None or self.b is None:
            print("Model not trained. Fit the model using fit_least_squares.")
            return None
        
        return (y - self.b) / self.w


    def visualize_model_output(self):
        """
        Used to visualize the data with its computed line
        """
        # Plot our model prediction
        plt.plot(self.x, self.w * self.x + self.b, c='b', label='Our Prediction')
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
