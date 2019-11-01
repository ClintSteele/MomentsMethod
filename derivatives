def derivative_one(function, var):
    x = [list(var[0]), list(var[0]), list(var[0])]
    deriv = []
    for i in range(0, len(var[0])):
        x[0][i] = var[0][i] - var[1][i]/10
        x[2][i] = var[0][i] + var[1][i]/10
        y = list(map(function, x))
        deriv.append((y[2] - y[0]) / (2 * var[1][i]/10))
        x[0][i] = var[0][i]
        x[2][i] = var[0][i]
    return deriv

def derivative_two(function, var):
    x = [list(var[0]), list(var[0]), list(var[0])]
    deriv = []
    for i in range(0, len(var[0])):
        x[0][i] = var[0][i] - var[1][i]/10
        x[2][i] = var[0][i] + var[1][i]/10
        y = list(map(function, x))
        deriv.append((y[2]-2*y[1]+y[0])/((var[1][i]/10)**2))
        x[0][i] = var[0][i]
        x[2][i] = var[0][i]
    return deriv
