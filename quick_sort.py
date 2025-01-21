import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    remaining = arr[:-1]
    left = [x for x in remaining if x <= pivot]
    right = [x for x in remaining if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    arr = [random.randint(20, 10000000) for _ in range(100000)]
    print(quick_sort(arr))