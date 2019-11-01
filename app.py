from MomentsCalc import mean
from MomentsCalc import StdDev

def pp(x):
    return 1*x[0]**3 + 1*50*x[1]**2 + 1*200 * x[2]

vars = [
    [10, 9, 5],
    [.1, 1, 1],
    [1.14, 1.14, 1.14],
    [5.4, 5.4, 5.4]
]

print(mean(pp, vars))
print(StdDev(pp, vars))

