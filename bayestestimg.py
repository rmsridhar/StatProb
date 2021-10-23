# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:25:56 2019

@author: ambra
"""

import math
def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
#e to test the calculateProbability() function
x = 71.5
mean = 73
stdev = 6.2
probability = calculateProbability(x, mean, stdev)
print('Probability of belonging to this class: {0}',probability)
