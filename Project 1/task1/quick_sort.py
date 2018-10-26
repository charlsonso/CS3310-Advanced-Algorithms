import time
import random

def main():
    size = int(input("Enter the size of a quick sort: "))
    arr = []
    for i in range(size):
        arr.append(random.randint(1, 10000001))
    start_time = time.clock()
    quick_sort(arr)
    end_time = time.clock()
    print("The quick sort for n = {} took {} seconds".format(size, end_time - start_time))

# start the quick sort
def quick_sort(arr):
   quick_sort_helper(arr,0,len(arr)-1)

# split array
def quick_sort_helper(arr,first,last):
   if first<last:

       split = partition(arr,first,last)

       quick_sort_helper(arr,first,split-1)
       quick_sort_helper(arr,split+1,last)

# Partition the array based on pivot
def partition(arr,first,last):
   pivot = arr[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and arr[leftmark] <= pivot:
           leftmark = leftmark + 1

       while arr[rightmark] >= pivot and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = arr[leftmark]
           arr[leftmark] = arr[rightmark]
           arr[rightmark] = temp

   temp = arr[first]
   arr[first] = arr[rightmark]
   arr[rightmark] = temp


   return rightmark

if __name__ == '__main__':
    main()
