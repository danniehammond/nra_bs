# nra_bs
#python program that uses newton-raphson algorithm to calculate implied volatility 
#used to better the black-scholes method
Determination of Implied Volatility using the Newton-Raphson Algorithm.  
Approach
Nicolas Christou’s R code was taken and rewritten in python to achieve the desired output. The python code was tested using parameters from problems whose solutions have been previously obtained using the R code. The same results were obtained thus verifying the accuracy of the python code. 
Using the following parameters, 
s0= 34 # Current Stock Price (Yahoo)
E=34  #Exercise Price
r=0.001  #Risk Free Rate
t=1 #Time to expiry in years
c =2.7240   #Call Option Price according to Black-Scholes Model
sigma = 0.10 #Initial Volatility
The output obtained was:
#[0.1, 0.19983863364782378, 0.2000026167726357, 0.20000261744285897]

Giving an implied volatility (sigma) = 0.2

An implied volatility is noted as when f() = 0.
