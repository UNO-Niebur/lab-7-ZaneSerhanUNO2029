#Zane Serhan
#Date: 3/3/2026
#Assignment: Problem7.py
#Project Euler Problem #7
# Find10001stPrime
#Approach:I just counted primes starting at 2 and checked each number with isPrime(). 
# Every time I found a prime, I added to a counter until I got to the 10001st prime, then printed it.

from NumberTests import isPrime

def main():
    prime_count = 0
    num = 2

    while True:
        if isPrime(num):
            prime_count += 1
            if prime_count == 10001:
                print(f"The 10001st prime number is {num}")
                break
        num += 1

if __name__ == '__main__':
    main()