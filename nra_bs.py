#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:48:13 2018

@author: danielhammond
@topic: newton-raphson-algorithm for calculating volatility
"""

import scipy.stats as ss
import math as m

s0= 34 # Current Stock Price (Yahoo)
E=34  #Exercise Price
r=0.001  #Risk Free Rate
t=1 #Time to expiry in years
c =2.7240   #Call Option Price according to Black-Scholes Model
sigma = 0.10 #Initial Volatility
def ivolatility(S0,E,r,t,c,sigma):
    """"
    "Determines implied volatility using the Newton-Raphson's algorithm
    Takes as arguments 
     - Current Stock Price(s0)
     - Exercise Price(E)
     - Risk Free Rate(r)
     - Time to expiry in years(t)
     - Call Option Price according to Black-Scholes Model(c)
     - Initial Volatility(sigma)
    as arguments and returns a list of volatilities.
    """
    vList = []    #Array to list of volatilities
    for i in range(0,11):
        vList.append(i)
    #print(sig)  #Initial list of volatilities
    vList[0]=sigma
    fList=[]
    #Newton-Raphson's Algorithm Implementation
    for i in range(1,101):
        d1 = (m.log(s0/E) + (r+sigma**2/2)*t)/(sigma*m.sqrt(t))
        d2 = d1-sigma*m.sqrt(t)
        #f(sigma)
        f = s0*ss.norm.cdf(d1)-E*m.exp(-(r*t))*ss.norm.cdf(d2)-c
        fList.append(f)
        #Derivative of d1 with respect to sigma
        d11 =(sigma **2 *t*m.sqrt(t)-(m.log(s0/E)+(r+sigma**2/2)*t))/(sigma**2 *t)
        #Derivative of d2 with respect to sigma
        d22 = d11-m.sqrt(t)
        #derivative of f_sigma
        f1 = s0*ss.norm.pdf(d1)*d11 - E * m.exp(-r*t)*ss.norm.pdf(d2)*d22
        #update sigma
        sigma = sigma - f/f1
        vList[i]= sigma
        if(abs(vList[i]-vList[i-1])<0.00000001):
            vList = vList[0:i+1] # Final list of volatilities
            break
    return vList
print(ivolatility(s0,E,r,t,c,sigma))
#output
#[0.1, 0.19983863364782378, 0.2000026167726357, 0.20000261744285897]
#The implied volatility (sigma) = 0.2
