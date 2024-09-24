import numpy as np
from scipy.optimize import minimize


def objective_function(x):
    return x ** 2 + 3 * x + 2


result = minimize(objective_function, x0 = 0)
print(result.x)


print("-------------------------------------------")

from scipy.integrate import quad


def integrand(x):
    print(x)
    return x ** 2


result, error = quad(integrand,0,1)
print(result)

print("-------------------------------------------")

from scipy.linalg import inv, det

matrix = np.array([[1,2],[3,4]])

matrix_det = det(matrix)
print(matrix_det)

print("-------------------------------------------")


from scipy.interpolate import interp1d

#known data points
x = np.array([0,1,2,3])
y = np.array([0,1,4,9])

#create a interpolation function
f = interp1d(x,y,kind = 'linear')

#interpolate a new value
new_x = 2.5
interpolated_value= f(new_x)
print(interpolated_value)