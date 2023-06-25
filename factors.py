#!/usr/bin/python3
import sys
def factorize(number):
    numbers = []
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            numbers.append(i)
            number //= i
    if number > 1:
        numbers.append(number)
    return numbers

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return
    filen = sys.argv[1]
    with open(filen, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            print(f"{number}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    main()

