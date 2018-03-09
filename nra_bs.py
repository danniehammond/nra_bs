#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:48:13 2018

@author: danielhammond
@topic: newton-raphson-algorithm for calculating volatility
"""

import scipy.stats as ss
import math as m
"""
s0 =  21
E = 20
r=0.1
t=0.25
c = 1.875
"""
s0= 2.36
E=2.36
r=0.01
t=1
c =0.1875
sigma = 0.10
sig = []
for i in range(0,11):
    sig.append(i)
print(sig)
sig[0]=sigma
for i in range(1,101):
    d1 = (m.log(s0/E) + (r+sigma**2/2)*t)/(sigma*m.sqrt(t))
    d2 = d1-sigma*m.sqrt(t)
    f = s0*ss.norm.cdf(d1)-E*m.exp(-(r*t))*ss.norm.cdf(d2)-c
    #Derivative of d1 with respect to sigma
    d11 =(sigma **2 *t*m.sqrt(t)-(m.log(s0/E)+(r+sigma**2/2)*t))/(sigma**2 *t)
    #Derivative of d2 with respect to sigma
    d22 = d11-m.sqrt(t)
    #derivative of f_sigma
    f1 = s0*ss.norm.pdf(d1)*d11 - E * m.exp(-r*t)*ss.norm.pdf(d2)*d22
    #update sigma
    sigma = sigma - f/f1
    sig[i]= sigma
    if(abs(sig[i]-sig[i-1])<0.00000001):
        sig = sig[0:i]
        break
print(sig)

