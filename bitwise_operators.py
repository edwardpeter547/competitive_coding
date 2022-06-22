# bitwise operator and - &

def check_odd_number(n):
    # return true if a number is odd.
    return n & 1 == 1

def check_even_number(n):
    # return true if a number is even.
    return not n & 1 == 1



# Todo: To right-shift is to divide in the power of 2.
# m = 200 therefore m >> 3 = 200 // 2**3 or 200 // 2*2*2

def divide_powers_of_two(number, exponent):
    return number >> exponent


# Todo: To left-shift is to multiply in the power of 2.
# m = 400 therefore m << 4 = 400 * (2**4) = 400 * (2 * 2 * 2 *2)

def multiply_powers_of_two(number, exponent):
    return number << exponent



def main():
    
    # check for even and odd numbers
    print(check_even_number(3))
    print(check_odd_number(3))
    
    
    # multiplying a number by the exponent (powers of 2) using bitwise shift left
    print(multiply_powers_of_two(50, 2))
    
    
    # divide a number by the exponent (powers of 2) using bitwise shift right
    print(divide_powers_of_two(400, 2))
    
    
    
    
    
    







    

if __name__ == "__main__":
    main()