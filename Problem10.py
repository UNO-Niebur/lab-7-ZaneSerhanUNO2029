#Zane Serhan
#Date: 3/3/2026
#Assignment: Problem10.py
#Project Euler Problem #10
#SummationOfPrimes
#Approach: I started the total at 2, then went from 3 to 200,000 by 2s to skip the even numbers. 
# I used isPrime to check each number, and if it was prime, I added it to the total.
#RunTime: Takes around a minute to load. I tried 2,000,000 but took way too long.

from NumberTests import isPrime

def main():
    total = 2
    for n in range(3, 200000, 2):
        if isPrime(n):
            total += n

    print(f"The sum of all primes below 200,000 is {total}")

if __name__ == '__main__':
    main()