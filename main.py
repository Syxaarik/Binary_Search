def  findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findsmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr


print(selectionsort([10, 5, 2, 6,7, 3,2, 8,9, 7 ,1]))
