import timeit
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
time_recursion = timeit.timeit('fact(100)', globals=globals(), number=10000)
print("Time taken for 10000 instances of fact(100) using recursion:", time_recursion)

def fact_for_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Time the execution of 1000 instances of fact(n) using a for loop
time_for_loop = timeit.timeit('fact_for_loop(100)', globals=globals(), number=1000)

print("Time taken for 1000 instances of fact(n) using a for loop:", time_for_loop)

# This function definition was generated using chat gpt
def fact_list_comprehension(n):
    return 1 if n == 0 else n * fact_list_comprehension(n-1)
time_list_comprehension = timeit.timeit('fact_list_comprehension(100)', globals=globals(), number=1000)
print("Time taken for 1000 instances of fact(n) using list comprehension:", time_list_comprehension)
