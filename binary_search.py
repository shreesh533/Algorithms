def binary_search(low, high, arr, key):
    while low < high:
        mid = int((low + high) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
    return -1


arr = [10, 12, 16, 19, 21, 32, 43, 74, 85, 91, 109, 123]
key = 123
start = 0
end = len(arr)
index = binary_search(start, end, arr, key)

if index == -1:
    print("Key not present")
else:
    print("Key present at index " + str(index))
