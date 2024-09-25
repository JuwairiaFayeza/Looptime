def linear_time_example(n):
    # O(n) - Linear time complexity
    for i in range(n):
        print(i)

def quadratic_time_example(n):
    # O(n^2) - Quadratic time complexity
    for i in range(n):
        for j in range(n):
            print(i, j)

def constant_time_example():
    # O(1) - Constant time complexity
    print("This runs in constant time")

# Example usage
n = 5
linear_time_example(n)
quadratic_time_example(n)
constant_time_example()