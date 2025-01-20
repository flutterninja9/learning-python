def binary_search(low, high, arr, key):
    mid = (low + high) // 2

    if low > high:
        return None
    if arr[mid] == key:
        return mid
    if key > arr[mid]:
        return binary_search(mid + 1, high, arr, key)
    if key < arr[mid]:
        return binary_search(low, mid-1, arr, key)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60]
    key = 30
    print(binary_search(0, len(arr) - 1, arr, key))