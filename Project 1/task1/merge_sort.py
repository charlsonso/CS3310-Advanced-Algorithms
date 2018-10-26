import random
import time

def main():
    # Get Size of array
    size = int(input("Enter the size of a merge sort: "))
    arr = []
    # Place random numbers into the array
    for i in range(size):
        arr.append(random.randint(1, 10000001))
    # Start Timer
    start_time = time.clock()
    # Merge Sort
    merge_sort(arr)
    # End timer
    end_time = time.clock()
    print("The merge sort for n = {} took {} seconds".format(size, end_time - start_time))

def merge_sort(arr):

    if len(arr)>1:
        # Split the arrays into subarray
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        # Recursively sort the left and right half
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0 
        # Sort and Merge
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1

if __name__ == '__main__':
    main()
