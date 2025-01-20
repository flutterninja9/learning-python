def find_sum(arr, max):
    if max < 0:
        return 0
    return arr[max] + find_sum(arr, max - 1)

print(find_sum([], -1)) # 0
print(find_sum([1], 0)) # 1
print(find_sum([1, 2], 1)) # 3
print(find_sum([1, 2, 3], 2)) # 6
print(find_sum([1, 2, 3, 4], 3)) # 10
print(find_sum([i for i in range(10)], 9)) # 45