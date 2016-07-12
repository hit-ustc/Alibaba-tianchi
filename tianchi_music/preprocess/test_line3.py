__author__ = 'CC'

import math

import numpy

# def polyfit(x, y, degree):
#     results = {}
#     coeffs = numpy.polyfit(x, y, degree)
#     results['polynomial'] = coeffs.tolist()
#
#     # r-squared
#     p = numpy.poly1d(coeffs)
#     # fit values, and mean
#     yhat = p(x)                         # or [p(z) for z in x]
#     ybar = numpy.sum(y)/len(y)          # or sum(y)/len(y)
#     ssreg = numpy.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
#     sstot = numpy.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
#     results['determination'] = ssreg / sstot
#     return results
#
# x=[ 1 ,2  ,3 ,4 ,5 ,6]
# y=[ 2.5 ,3.51 ,4.45 ,5.52 ,6.47 ,7.2]
# z1 = polyfit(x, y, 2)
# print z1

def linefit(x , y):
    N = float(len(x))
    sx,sy,sxx,syy,sxy=0,0,0,0,0
    for i in range(0,int(N)):
        sx  += x[i]
        sy  += y[i]
        sxx += x[i]*x[i]
        syy += y[i]*y[i]
        sxy += x[i]*y[i]
    a = (sy*sx/N -sxy)/( sx*sx/N -sxx)
    b = (sy - a*sx)/N
    r = abs(sy*sx/N-sxy)/math.sqrt((sxx-sx*sx/N)*(syy-sy*sy/N))
    return a,b,r

if __name__ == '__main__':
    X = []
    for i in xrange(183):
        X.append(i+1)
    Y=[58,99,125,273,172,313,99,132,100,94,74,120,64,88,116,83,96,94,130,196,116,120,243,81,177,63,100,113,94,84,72,85,71,87,80,97,150,109,71,85,84,66,75,69,194,168,57,89,136,49,76,104,166,258,176,117,111,229,87,193,76,65,59,60,136,52,63,61,66,65,57,61,75,84,77,73,60,78,58,56,57,66,61,77,76,129,93,93,222,108,184,61,110,115,115,95,92,109,148,128,70,86,54,79,121,154,131,89,90,176,154,107,81,157,119,95,139,175,117,107,126,277,100,120,113,79,115,77,89,143,150,73,85,82,90,88,69,112,84,94,87,91,80,66,158,40,59,175,99,113,113,57,67,85,87,110,134,103,67,65,73,125,73,72,66,98,46,48,51,69,68,119,64,56,116,87,71,72,70,65,101,58,77]
    a,b,r=linefit(X,Y)
    print("X=",X)
    print("Y=",Y)
    print("y = %10.5f x + %10.5f , r=%10.5f" % (a,b,r) )
