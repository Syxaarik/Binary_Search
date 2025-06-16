# recursive function sum
def suma(arr):
    if not arr:
        return 0
    return arr[0] + suma(arr[1:])


# recursive function count
def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])


# recursive function max
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sum_max = max(list[1:])
    return list[0] if list[0] > sum_max else sum_max


# quick sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(suma([1, 2, 3, 4, 5]))
print(count([1, 2, 3, 4, 5]))
print(max([1, 2, 3, 4, 5]))
print(quick_sort([5, 2, 4, 3, 1]))
