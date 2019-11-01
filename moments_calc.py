import numpy as nm  # numpy will be needed for these functions to work
import derivatives as dd  # the derivatives need to be calculated and the respective functions are in another file


# Because squaring needs to be done a number of time, a dedicated function is made to do this
def square(x):
    return x**2


# A function to calculate the mean
def mean(func, varis):
    out = func(list(varis[0]))  # this is the nominal output value (also the first order approximation of the mean)
    variance = list(map(square, varis[1]))  # the standard deviations are squared to gain variance values
    diffs2 = dd.derivative_two(func, varis)  # find the derivatives of the function about the nominal for later
    second = nm.multiply(diffs2, variance)  # this is second order component - the variance be the second div
    return out + 1 / 2 * sum(second)  # this is the execution of the moment formula - first order plus second order/2


# A function to calculate the standard deviation
def std_dev(func, varis):
    variance = list(map(square, varis[1]))  # the standard deviations are squared to gain variance values
    diffs = dd.derivative_one(func, varis)  # find the first derivatives of the function about the nominal for later
    diffs2 = dd.derivative_two(func, varis)   # find the second derivatives of the function about the nominal for later
    diffonesquared = list(map(square, diffs))  # the square of the first derivative is needed later
    diffonetwo = nm.multiply(diffs, diffs2)  # the first derivative multiplied by the second derivative is needed later
    stdcubed = nm.multiply(variance, varis[1])  # this is to convert the coefficient of skew to the skew (std^3)
    skew = nm.multiply(varis[2], stdcubed)  # convert the coefficient of skew to skew by multiplying be std^3
    kurtosis = nm.multiply(varis[3], list(map(square, variance)))  # convert the coefficient of kurtosis to kurtosis
                                                                    # by multiplying be std^3
    difftwosquared = list(map(square, diffs2))  # the square of the second derivative is needed later
    varianceout = nm.sum(nm.multiply(diffonesquared, variance)+nm.multiply(diffonetwo, skew)+.25*nm.multiply(difftwosquared,
               nm.subtract(kurtosis, list(map(square, variance)))))  # this is the execution of the variance formula
    return varianceout**0.5  # standard deviation is the variance square rooted



