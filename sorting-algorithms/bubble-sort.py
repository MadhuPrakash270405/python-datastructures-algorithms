

def bubble_sort(unsorted_list):
    """
    Bubble sort algorithm
    """
    for iternation in range(len(unsorted_list)):
        swapped=False
        print(f'\nITERATION:{iternation}')
        for i in range(len(unsorted_list)-iternation-1):
            print(f'COMPARING {unsorted_list[i]} {unsorted_list[i+1]}')
            if unsorted_list[i] > unsorted_list[i+1]:
                swapped=True
                unsorted_list[i],unsorted_list[i+1] =unsorted_list[i+1],unsorted_list[i]
        print(unsorted_list)
        print("****************************************************************")
        if not swapped:
            break;

if __name__ == '__main__':
    unsorted_list = [1,2,7,4,5,6,3,8,9,10]
    bubble_sort(unsorted_list)