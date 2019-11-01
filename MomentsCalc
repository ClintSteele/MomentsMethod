import numpy as nm
import derivatives as dd

def square(x):
    return x**2
def mean(func, vars):
    out = func(list(vars[0]))
    variance = list(map(square, vars[1]))
    diffs2 = dd.derivative_two(func, vars)
    second = nm.multiply(diffs2, variance)
    return out + 1 / 2 * sum(second)
    
def StdDev(func, vars):
    variance = list(map(square, vars[1]))
    diffs = dd.derivative_one(func, vars)
    diffs2 = dd.derivative_two(func, vars)
    second = nm.multiply(diffs2, variance)
    diffonesquared = list(map(square, diffs))
    diffonetwo = nm.multiply(diffs, diffs2)
    stdcubed = nm.multiply(variance, vars[1])
    skew = nm.multiply(vars[2], stdcubed)
    kurtosis = nm.multiply(vars[3], list(map(square, variance)))
    difftwosquared = list(map(square, diffs2))
    varianceout = nm.sum(nm.multiply(diffonesquared, variance)+nm.multiply(diffonetwo, skew)+.25*nm.multiply(difftwosquared,
               nm.subtract(kurtosis, list(map(square, variance)))))
    return varianceout**0.5
