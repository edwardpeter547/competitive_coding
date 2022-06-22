
# find the gcd of two numbers using euclidean divison algorithm 



def gcd_euclid_algorithm(a, b):
    # the time complexity for this algorithm is O(log(min(a, b)))
    if a == 0:
        return b
    
    return gcd_euclid_algorithm(b % a, a)
    


def lowest_common_multiple(a , b):
    hcf = gcd_euclid_algorithm(a,b)
    prod = a * b
    
    return prod // hcf


def main():
    
    # print(optimal_solution(1000000000000))
    print(gcd_euclid_algorithm(5,10))
    print(lowest_common_multiple(5,10))
    


if __name__ == "__main__":
    main()