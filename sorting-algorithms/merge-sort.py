

def merge_sort(unsorted_list):
    """
    merge sort algorithm
    """
    if len(unsorted_list) > 1:
        half = len(unsorted_list)//2
        left = unsorted_list[:half]
        right = unsorted_list[half:]
        print(f'left_half:{left} right_half:{right}')
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_list[k] = left[i]
                i += 1
            else:
                unsorted_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            unsorted_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            unsorted_list[k] = right[j]
            j += 1
            k += 1

    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [6, 5, 12, 10, 9, 1]
    print(merge_sort(unsorted_list))
