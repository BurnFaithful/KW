def bubbleSort(target_list):
    list_len = len(target_list)
    for i in range(list_len - 1):
        flag = True
        for j in range(list_len - 1 - i):
            if target_list[j] > target_list[j + 1]:
                target_list[j], target_list[j + 1] = target_list[j + 1], target_list[j]
                flag = False

        if flag:
            break
    return target_list

def insertionSort(target_list):
    list_len = len(target_list)
    for i in range(1, list_len):
        temp = target_list[i]
        j = i - 1
        while j >= 0 and target_list[j] > temp:
            target_list[j + 1] = target_list[j]
            j -= 1
        target_list[j + 1] = temp

    return target_list


def selectionSort(target_list):
    list_len = len(target_list)
    for i in range(list_len - 1):
        min_index = i
        for j in range(i + 1, list_len):
            if target_list[j] < target_list[min_index]:
                min_index = j

        if i != min_index:
            target_list[i], target_list[min_index] = target_list[min_index], target_list[i]

    return target_list

def mergeSort(target_list):
    pass

def quickSort(target_list, start, end):
    if start >= end:
        return

    pivot = partition(target_list, start, end)
    quickSort(target_list, start, pivot - 1)
    quickSort(target_list, pivot + 1, end)


def partition(target_list, start, end):
    pivot = start
    left = pivot + 1
    right = end

    while left <= right:
        while left < right and target_list[pivot] > target_list[left]:
            left += 1
        while left < right and target_list[pivot] < target_list[right]:
            right -= 1
        target_list[left], target_list[right] = target_list[right], target_list[left]
        left += 1
        right -= 1

    target_list[pivot], target_list[right] = target_list[right], target_list[pivot]
    return right



if __name__ == "__main__":
    test_list = [38, 6, 22, 3, 19, 72, 65, 34, 26, 51]
    print(test_list)
    # bubbleSort(test_list)
    insertionSort(test_list)
    # selectionSort(test_list)
    # quickSort(test_list, 0, len(test_list) - 1)
    print(test_list)