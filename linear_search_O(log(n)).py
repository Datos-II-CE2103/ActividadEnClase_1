import timeit
import random

def sequential_search_log_n(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, len(arr)))

def binary_search(arr, target, start, end):
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
        print(f"Para n={n}: Tiempo tomado: {time_taken*1e9:.2f} nanosegundos")
