"""
    This is the coding implementation of the papers "C1_W1_Lab02_Model_Representation_Soln" and "C1_W1_Lab03_Cost_function_Soln"
"""
from main import LinearRegression

import numpy as np

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

model = LinearRegression(x_train, y_train, 100, 100)
model.compute_model_output()



