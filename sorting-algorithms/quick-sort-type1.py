

def partition(unsorted_list, low_index, high_index):
    print("\n********************************")
    print("* Partition Function Called *")
    print(f'PROCESSING {unsorted_list[low_index:high_index]}')
    pivot = unsorted_list[high_index]
    swap_pointer = low_index-1
    for current_index in range(low_index, high_index):
        if unsorted_list[current_index] <= pivot:
            swap_pointer += 1
            unsorted_list[swap_pointer], unsorted_list[current_index] = unsorted_list[current_index], unsorted_list[swap_pointer]
    unsorted_list[swap_pointer +
                  1], unsorted_list[high_index] = unsorted_list[high_index], unsorted_list[swap_pointer+1]

    print(
        f'PIVOT ELEMENT:{pivot} SWAP POINTER VALUE :{swap_pointer}')
    return swap_pointer+1


def quick_sort(unordered_list, low, high):
    if low < high:
        pi = partition(unordered_list, low, high)
        quick_sort(unordered_list, low, pi-1)
        quick_sort(unordered_list, pi+1, high)


if __name__ == '__main__':
    unsorted_list = [8, 7, 6, 1, 0, 9, 2]
    quick_sort(unsorted_list, 0, len(unsorted_list)-1)
    print('-------------------------FINAL SORTED---------------------------------------')
    print(unsorted_list)
