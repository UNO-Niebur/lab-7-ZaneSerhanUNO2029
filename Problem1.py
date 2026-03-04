#Zane Serhan
#Date: 3/3/2026
#Assignment: Problem1.py
#Project Euler Problem #1
#MultiplesOf3and5
#Provided problem

import NumberTests

def main():
  total = 0
  for i in range(1000):
    if NumberTests.isThreeOrFive(i):
      total += i

  print(total)


if __name__ == '__main__':
  main()
