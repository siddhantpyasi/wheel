def isort(sortThis):
    sorted = False
    for i in range(len(sortThis)):
        item = sortThis[i]
        while i > 0 and sortThis[i-1] > sortThis[i]:
            temp = sortThis[i-1]
            sortThis[i-1] = sortThis[i]
            sortThis[i] = temp
            i -= 1

    return sortThis


if __name__ == "__main__":
    sortThis = [3, 44, 38, 5, 47, 15, 36, 26]
    sort2 = [56, 78, 99, 12, 3, 4, 98, 23, 21, 0, 86, 75, 68, 47, 999, 456, 15, 56, 47, 58, 94, 87, 7]
    print(sortThis)
    round1 = isort(sortThis)
    print(round1)

    print(sort2)
    round2 = isort(sort2)
    print(round2)


