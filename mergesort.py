def merge(left, right):
    # create an empty list to return
    returnThis = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            returnThis.append(left[0])
            left.remove(left[0])
        else:
            returnThis.append(right[0])
            right.remove(right[0])
    
    if left:
        returnThis.extend(left)
    if right:
        returnThis.extend(right)

    return returnThis


# Pretty standard  recursive algorithm
def mergeSort(sortThis):
    length = len(sortThis)
    if length == 1: return sortThis

    middle = length // 2
    firstHalf = sortThis[:middle]
    secondHalf = sortThis[middle:]

    left = mergeSort(firstHalf)
    right = mergeSort(secondHalf)

    return list(merge(left, right))


if __name__ == "__main__":
    sortThis = [56, 78, 99, 12, 3, 4, 98, 23, 21, 0, 86, 75, 68, 47, 999, 456, 15, 56, 47, 58, 94, 87, 70]
    sort2= [3,44,38,5,47,15,36,26]
    print(sort2)
    final =  mergeSort(sort2)
    print(final)

    print(sortThis)
    final = mergeSort(sortThis)
    print(final)
