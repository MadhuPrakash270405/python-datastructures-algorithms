

def quick_sort(unsorted_list):
    print("\n********************************")
    print(f'PROCESSING:{unsorted_list}')
    if len(unsorted_list) <= 1:
        print(f'UNDER VALUED LIST:{unsorted_list}')
        return unsorted_list
    else:
        pivot = unsorted_list[0]
        left_list = [x for x in unsorted_list if x < pivot]
        right_list = [x for x in unsorted_list[1:] if x >= pivot]
        print(f'left_list: {left_list}, right_list: {right_list}')
        print("********************************\n")
        return quick_sort(left_list)+[pivot]+quick_sort(right_list)


if __name__ == '__main__':
    unsorted_items = [9, 5, 1, 4, 3]
    print(quick_sort(unsorted_items))
