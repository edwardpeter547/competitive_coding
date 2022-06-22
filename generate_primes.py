from math import sqrt

# generate prime numbers using Sieve of Eratosthenes

def generate_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for p in range(2, int(sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p, n + 1, p):
                primes[i] = False
    
    for i in range(0, len(primes)):
        if primes[i] == True:
            print(i, end=" ")
    


def main():
    generate_primes(10)



if __name__ == "__main__":
    main()