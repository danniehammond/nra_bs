#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 17:28:25 2018

@author: niioto
"""

import scipy.stats as ss
import math as m
s0 =  2.36
E =2.36
r=0.01
t=1
c = 0.1875
sigma = 0.10
d1 = (m.log(s0/E) + (r+sigma**2/2)*t)/(sigma*m.sqrt(t))
d2 = d1-sigma*m.sqrt(t)
print(d1)
print(d2)