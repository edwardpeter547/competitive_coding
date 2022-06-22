
# ispowerof2
# n  -> input
# returns True/False
# check if n is a power of 2
# n = 512 -> True 512 = 2**9
# n = 1024 -> True 1024 = 2 ** 10


def is_power_two(n):
    # T.C = O(1) Constant Time Operation.
    if n <= 0:
        return False
    x = n
    y =  not (n & (n - 1))
    return x and y
    
    
    
def main():
    
    print(is_power_two(4))
    

if __name__ == "__main__":
    main()