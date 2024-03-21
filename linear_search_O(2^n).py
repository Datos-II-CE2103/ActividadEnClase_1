import timeit
import random

def exponential_search(arr, target):
    """
    Performs exponential search on the given sorted array to find the target element.
    
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
    return sequential_search(arr[:min(i, len(arr))], target)

def sequential_search(arr, target):
    """
    Performs linear search on the given array to find the target element.
    
    Parameters:
        arr (list): An array where the target element is to be searched.
        target (int): The element to be searched in the array.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        arr = list(range(n))
        target = n - 1  
        random.shuffle(arr)  
        arr.sort()  
        setup_code = f"from __main__ import exponential_search, arr, target"
        time_taken = timeit.timeit(stmt="exponential_search(arr, target)", setup=setup_code, number=1)
        print(f"For n={n}: Time taken: {time_taken*1e9:.2f} nanoseconds")
