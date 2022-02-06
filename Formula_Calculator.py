# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:09:48 2021

@author: Emre
"""
import math


p=0.3917;

a=(1-(2*p));

b=1- pow(2*p,6);

alpha= 2*a/((33*a)+32*p*b)
n = (math.log(1-p)/math.log(1-alpha))+1

print(" ",n);