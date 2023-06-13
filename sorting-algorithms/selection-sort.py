

def selection_sort(unsorted_list):
    """
    Selection sort algorithm
    """

    no_of_items_in_list = len(unsorted_list)
    for step in range(no_of_items_in_list):
        print(f'\n STEP:{step}')
        min_index = step
        for index in range(step+1, no_of_items_in_list):
            if unsorted_list[index] < unsorted_list[min_index]:
                print(
                    f'\nMIN ELE: {unsorted_list[min_index]} BUT MINIMUM INDEX CHANGED FROM:{min_index} TO {index} SO NEW MIN ELE: {unsorted_list[index]}')
                min_index = index
        print(
            f'\nSWAPPING {unsorted_list[step]} with {unsorted_list[min_index]}')
        unsorted_list[step], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[step]
        print(unsorted_list)
        print("****************************************************************")


if __name__ == '__main__':
    unsorted_list = [10, 5, 9, 2, 1, 0, 3, 4]
    selection_sort(unsorted_list)
