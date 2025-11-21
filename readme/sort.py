def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # меняем местами
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
