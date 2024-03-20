import timeit
import random

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return sequential_search(arr[:min(i, len(arr))], target)

def sequential_search(arr, target):
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
        print(f"Para n={n}: Tiempo tomado: {time_taken*1e9:.2f} nanosegundos")
