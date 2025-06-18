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


# abbcceer -> 1a2b2c2e1r
def encode(arr):
    result = ''
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            result += f'{count}{arr[i - 1]}'
            count = 1
    result += f'{count}{arr[-1]}'
    return result


def decode(arr):
    for i in range(1, len(arr)):
        if arr[1] == arr[i - 1]:
            return 'Это простой пример работы range(1, len(arr))'
        return None
    return None


print(suma([1, 2, 3, 4, 5]))
print(count([1, 2, 3, 4, 5]))
print(max([1, 2, 3, 4, 5]))
print(quick_sort([40, 30, 10, 20, 50]))
print(encode('aabbcceer'))
print(decode('aa'))
