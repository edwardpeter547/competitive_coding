from math import sqrt

# Prime numbers are numbers with only two factors. itself and 1

# find factors of a number 

def check_prime_number(n):
    
    if n == 0 or n == 1:
        return False
    
    divisor_count = 0 
    
    for i in range(1, n + 1): # O(N)
        if n % i == 0:
            divisor_count += 1
    print(f"Total Factors: {divisor_count}")
    if divisor_count > 2:
        return False
    else:
        return True
    

def check_prime_number_optimal(n):
    if n == 0 or n == 1:
        return False
    
    if n ==2 or n == 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(sqrt(n)) + 1):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        
    return True
    


def main():
    print(check_prime_number(2))
    print(check_prime_number_optimal(2))
    

if __name__ == "__main__":
    main()