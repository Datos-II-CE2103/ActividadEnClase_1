import timeit
import random

def sequential_search_n_log_n(arr, target):
    """
    Performs sequential search with n log n complexity on the given sorted array to find the target element.
    
    Parameters:
        arr (list): A sorted list where the target element is to be searched.
        target (int): The element to be searched in the array.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binary_sequential_search(arr, target):
    """
    Performs binary sequential search on the given array to find the target element.
    
    Parameters:
        arr (list): An array where the target element is to be searched.
        target (int): The element to be searched in the array.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for i in range(0, len(arr), len(arr) // 2):
        result = sequential_search_n_log_n(arr[i:i+len(arr) // 2], target)
        if result != -1:
            return result + i
    return -1

if __name__ == "__main__":
    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        arr = list(range(n))
        target = n - 1  
        random.shuffle(arr)  
        setup_code = f"from __main__ import binary_sequential_search, arr, target"
        time_taken = timeit.timeit(stmt="binary_sequential_search(arr, target)", setup=setup_code, number=1)
        print(f"For n={n}: Time taken: {time_taken*1e9:.2f} nanoseconds")
