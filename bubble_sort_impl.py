def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    
    return arr


if __name__ == '__main__':
    arr = [4, 3, 1, 5, 2]
    print(bubble_sort(arr))