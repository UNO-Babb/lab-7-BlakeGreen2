#Project Euler Problem 3

import NumberTests

def main():
  number = 600851475143
  largest = 0

  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0 and NumberTests.isPrime(i):
      largest = i

  print("The largest prime factor is:", largest)


if __name__ == '__main__':
  main()
