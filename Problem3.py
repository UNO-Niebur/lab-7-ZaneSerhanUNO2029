#Zane Serhan
#Date: 3/3/2026
#Assignment: Problem3.py
#Project Euler Problem #3
#LargestPrimeFactor
#Provided problem

from NumberTests import isPrime
from NumberTests import getFactors

def main():
  number = 13195
  factors = getFactors(number)
  print(factors)
  
  for f in factors:
    if isPrime(f):
      print(f)

if __name__ == '__main__':
  main()
