# brute force approach to counting the number of 1's in the binary representation of a number

def bruteforce_count_bits(n):
    # T.C = O(N) since we have to use the count function.
    
    s = str(bin(n))[2:]
    print(s.count('1'))
    

def optimal_count_bits(n):
    count = 0
    
    while n:
        count +=1
        n = n & (n - 1)
    return count


# Take an Integer N and convert it into binary

def integer_to_binary(number):
    return str(bin(number))[2:]


def convert_binary_decimal(binary):
    return int(binary, 2)

# check an array for the one and only number that occurs only once.
def find_single_occurence(data):
    result = data[0]
    for i in range(1, len(data)):
        result = result ^ data[i]
        
    return result


# Check if a particular bit is set in a binary representation of a number:
# example in 7 with binary of 111 n=7 k=1 should return True

def check_bit_status(number, bit_position):
    if number & (1 << (bit_position - 1)):
        return True
    else:
        return False
    
    
def main():
    
    bruteforce_count_bits(7)
    print(optimal_count_bits(7))
    
    
    # convert an integer to binary representation
    number = 7
    binary = integer_to_binary(number)
    print(f"Binary representation of {number} is {binary}")
    
    # convert a binary to decimal or integer representation
    decimal = convert_binary_decimal(binary)
    print(f"decimal representation of the binary of {binary} is {decimal}")
    
    # check for any number that occurs only once in the array
    data = [2,3,2,5,3,4,5,6,6,10]
    print(find_single_occurence(data))
    
    # Check if a particular bit is set in a binary representation of a number:
    print(check_bit_status(6,3))
    
    
    
    
    

if __name__ == "__main__":
    main()