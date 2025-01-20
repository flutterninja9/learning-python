def find_sum(arr, max):
    if max < 0:
        return 0
    if isinstance(arr[max], list):
        return find_sum(arr[max], len(arr[max]) - 1) + find_sum(arr, max-1)
    if isinstance(arr[max], int):
        return arr[max] + find_sum(arr, max - 1)
    
    return 0

print(find_sum([], -1)) # 0
print(find_sum([1, 2, [3,4], [5,6]], 3)) # 21
print(find_sum([[3,4]], 0)) # 7