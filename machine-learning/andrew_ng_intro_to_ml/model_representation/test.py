"""
    This is the coding implementation of the papers "C1_W1_Lab02_Model_Representation_Soln" and "C1_W1_Lab03_Cost_function_Soln"
"""
from main import LinearRegression

import numpy as np

x_train = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
y_train = np.array([110.0, 120.0, 200.0, 220.0, 310.0, 370.0])

model = LinearRegression(x_train, y_train)


epochs = 1000
L = 0.0001

for i in range(epochs):
    w, b = model.fit_gradient_descent(L)
    print(f'Epoch {i}: w={w}, b={b}')
    
print(f'Final model: w={w}, b={b}')
model.visualize_model_output()