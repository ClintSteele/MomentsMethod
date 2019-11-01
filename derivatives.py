# the first derivative
def derivative_one(function, var):
    x = [list(var[0]), list(var[0]), list(var[0])]  # create an array for inputs to use later
    deriv = []  # a list to store the derivatives
    for i in range(0, len(var[0])):  # a partial derivative is needed for each input
        x[0][i] = var[0][i] - var[1][i]/10  # the respective input is decreased slightly and recorded
        x[2][i] = var[0][i] + var[1][i]/10  # the respective input is increased slightly and recorded
        y = list(map(function, x))  # the output is found for each setting (high, low and nominal)
        deriv.append((y[2] - y[0]) / (2 * var[1][i]/10))  # the numerical approximation for the first derivative
        x[0][i] = var[0][i]  # set the decreased input set back to nominal for the next cycle
        x[2][i] = var[0][i]  # set the increased input set back to nominal for the next cycle
    return deriv  # return the the first derivative


# the second derivative
def derivative_two(function, var):
    x = [list(var[0]), list(var[0]), list(var[0])]  # create an array for inputs to use later
    deriv = []  # a list to store the derivatives
    for i in range(0, len(var[0])):  # a partial derivative is needed for each input
        x[0][i] = var[0][i] - var[1][i]/10  # the respective input is decreased slightly and recorded
        x[2][i] = var[0][i] + var[1][i]/10  # the respective input is increased slightly and recorded
        y = list(map(function, x))  # the output is found for each setting (high, low and nominal)
        deriv.append((y[2]-2*y[1]+y[0])/((var[1][i]/10)**2))  # the numerical approximation for the second derivative
        x[0][i] = var[0][i]  # set the decreased input set back to nominal for the next cycle
        x[2][i] = var[0][i]  # set the increased input set back to nominal for the next cycle
    return deriv  # return the the first derivative

