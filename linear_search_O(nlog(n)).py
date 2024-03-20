import timeit
import random

def sequential_search_n_log_n(arr, target):
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
        print(f"Para n={n}: Tiempo tomado: {time_taken*1e9:.2f} nanosegundos")
