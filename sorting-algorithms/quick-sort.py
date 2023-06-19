

def quick_sort(unsorted_list):
    print("\n********************************")
    print(f'PROCESSING:{unsorted_list}')
    if len(unsorted_list) <= 1:
        print(f'##RETURNING UNDER VALUED LIST:{unsorted_list}')
        return unsorted_list
    else:
        pivot = unsorted_list[0]
        left_list = [x for x in unsorted_list if x < pivot]
        right_list = [x for x in unsorted_list[1:] if x >= pivot]
        pivot_list = [pivot]
        print(
            f'PROCESSING left_list: {left_list},pivot:{pivot_list} right_list: {right_list}')
        left_quick = quick_sort(left_list)
        right_quick = quick_sort(right_list)

        print(
            f'OUTPUT FOR left_list: {left_list},pivot:{pivot_list} right_list: {right_list}')
        print(f'{left_quick+pivot_list+right_quick} ')
        print("********************************\n")
        return left_quick + pivot_list + right_quick


if __name__ == '__main__':
    unsorted_items = [9, 5, 1, 4, 3]
    print(quick_sort(unsorted_items))
