

def insertion_sort(unsorted_list):
    """
    insertion sort algorithm
    """
    for step in range(1, len(unsorted_list)): # step= 3
        back_step=step-1
        key=unsorted_list[step]
        print("\n************************************")
        print(f"KEY:{key} UNSORTED_LIST:{unsorted_list}")
        while back_step>=0 and key < unsorted_list[back_step]:
            print(f'ITERATION:{step} BACKSTEP:{back_step} ELE:{unsorted_list[back_step]} ')
            unsorted_list[back_step+1]=unsorted_list[back_step]
            back_step = back_step - 1
            print(unsorted_list)
        unsorted_list[back_step+1]=key
        print(f'AFTER ITERATION:{step} UNSORTED LIST:{unsorted_list}')
        print("\n************************************")
    print(f'FINAL :{unsorted_list}')




if __name__ == '__main__':
    unsorted_list = [1, 5, 9, 4, 3]
    insertion_sort(unsorted_list)
