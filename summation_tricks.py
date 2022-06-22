
# we are assuming if the input n = 5
# then our solution should look for 1+2+3+4+5 = 15
# n = 10
# n = 


def non_optimal_solution(n):
    # the time complexity for this algorithm is O(n)
    # because we have to traverse upto n.
    
    count = 0
    for i in range(n + 1):
        count = count + i
    return count    


def optimal_solution(n):
    return (n * (n + 1)) // 2


def main():
    
    print(optimal_solution(1000000000000))
    print(non_optimal_solution(1000000000000))
    


if __name__ == "__main__":
    main()