import timeit
import random

def sequential_search_n_squared(arr, target):
    """
    Performs sequential search with quadratic complexity on the given array to find the target element.
    
    Parameters:
        arr (list): An array where the target element is to be searched.
        target (int): The element to be searched in the array.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] == target:
                return j
    return -1

if __name__ == "__main__":
    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        arr = list(range(n))
        target = n - 1  
        random.shuffle(arr) 
        setup_code = f"from __main__ import sequential_search_n_squared, arr, target"
        time_taken = timeit.timeit(stmt="sequential_search_n_squared(arr, target)", setup=setup_code, number=1)
        print(f"For n={n}: Time taken: {time_taken*1e9:.2f} nanoseconds")
