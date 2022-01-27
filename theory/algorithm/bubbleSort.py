def bubbleSort(array):
    arrayLength = len(array)
    for i in range(arrayLength -1, 0, -1):
        swapped = False
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array

array = [3, 2, 1, 4, 5]
print(bubbleSort(array))

