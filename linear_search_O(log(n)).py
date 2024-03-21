import timeit
import random

def sequential_search_log_n(arr, target):
    """
    Performs sequential search with logarithmic complexity on the given sorted array to find the target element.
    
    Parameters:
        arr (list): A sorted list where the target element is to be searched.
        target (int): The element to be searched in the array.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, len(arr)))

def binary_search(arr, target, start, end):
    """
    Performs binary search on the given sorted array within the specified range to find the target element.
    
    Parameters:
        arr (list): A sorted list where the target element is to be searched.
        target (int): The element to be searched in the array.
        start (int): The starting index of the search range.
        end (int): The ending index of the search range.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == "__main__":
    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        arr = list(range(n))  
        target = n - 1  
        random.shuffle(arr)  
        arr.sort()  
        setup_code = f"from __main__ import sequential_search_log_n, arr, target"
        time_taken = timeit.timeit(stmt="sequential_search_log_n(arr, target)", setup=setup_code, number=1)
        print(f"For n={n}: Time taken: {time_taken*1e9:.2f} nanoseconds")
