# Import the functions for calculate the mean and standard deviation
from moments_calc import mean
from moments_calc import std_dev

# Create a function to be analysed. Note the input is an array. This is essential for how the mean and
# standard deviation functions work. The function to be analyses should refer to parts of the input variable.
def pp(x):
    return 1*x[0]**3 + 50*x[1]**2 + 200 * x[2]


# Define the input variables. This done via an array (4 x n) where n is the number of input variables. The first row
# is the mean or nominal values for the inputs. The second row is the standard deviation, the third is the coefficient
# of skew and the fourth is the coefficient of kurtosis. Note the coefficients in the last two rows; not the respective
# moments in absolute terms. The functions are designed to take coefficients.
inputs = [
    [10, 9, 5],
    [.1, 1, 1],
    [1.14, 1.14, 1.14],
    [5.4, 5.4, 5.4]
]

# Below shows how the functions for the mean and standard deviation are called.
output_mean = mean(pp, inputs)
output_standard_deviation = std_dev(pp, inputs)

# Below prints the outputs
print(output_mean)
print(output_standard_deviation)

