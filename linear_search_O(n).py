import timeit
import random

def jump_search(arr, target):
    """
    Performs jump search on the given sorted array to find the target element.
    
    Parameters:
        arr (list): A sorted list where the target element is to be searched.
        target (int): The element to be searched in the array.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    n = len(arr)
    step = int(n**0.5) 
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

if __name__ == "__main__":
    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        arr = list(range(n))
        target = n - 1  
        random.shuffle(arr)
        arr.sort()
        setup_code = f"from __main__ import jump_search, arr, target"
        time_taken = timeit.timeit(stmt="jump_search(arr, target)", setup=setup_code, number=1)
        print(f"For n={n}: Time taken: {time_taken*1e9:.2f} nanoseconds")
