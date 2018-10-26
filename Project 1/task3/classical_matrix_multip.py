import time
import random

def main():
    size = int(input("Enter the n size of a n x n matrix: "))
    arr1 = generate_nxn_array(size)
    arr2 = generate_nxn_array(size)
    arr3 = generate_empty_nxn_array(size)
    start_time = time.clock()
    classical_mult(arr1, arr2, arr3)
    end_time = time.clock()
    print("The matrix multiplication for n = {} took {} seconds".format(size, end_time - start_time))

# walk through the array and multiple the row by the column and place into correct space
def classical_mult(arr1, arr2, arr3):
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                arr3[i][j] += arr1[i][k] * arr2[k][j]

# Create random nxn array filled with values
def generate_nxn_array(size):
    x = []
    for i in range(size):
        j = []
        for i in range(size):
            j.append(random.randint(1, 11))
        x.append(j)
    return x

# Create nxn array with 0s
def generate_empty_nxn_array(size):
    x = []
    for i in range(size):
        j = []
        for i in range(size):
            j.append(0)
        x.append(j)
    return x

if __name__ == '__main__':
    main()

