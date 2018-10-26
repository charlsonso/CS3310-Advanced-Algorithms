import time
import random

def main():
    size = int(input("Enter the n size of a n x n matrix: "))
    arr1 = generate_nxn_array(size)
    arr2 = generate_nxn_array(size)
    start_time = time.clock()
    arr3 = strassen_mult(arr1, arr2)
    end_time = time.clock()
    print("The matrix multiplication for n = {} took {} seconds".format(size, end_time - start_time))

# Generate nxn array with random numbers
def generate_nxn_array(size):
    x = []
    for i in range(size):
        j = []
        for i in range(size):
            j.append(random.randint(1, 11))
        x.append(j)
    return x

# Split the matrix into quarters
def split_matrix(m):
    row_len = len(m[0][:])
    col_len = len(m[:][0])
    half_row_len = row_len // 2
    half_col_len = col_len // 2
    if row_len == col_len and row_len % 2 == 0:
        a = [[0 for i in range(half_row_len)] for j in range(half_col_len)]
        b = [[0 for i in range(half_row_len)] for j in range(half_col_len)]
        c = [[0 for i in range(half_row_len)] for j in range(half_col_len)]
        d = [[0 for i in range(half_row_len)] for j in range(half_col_len)]
        for i in range(half_row_len):
            for j in range(half_col_len):
                a[i][j] = m[i][j]
                b[i][j] = m[i][j+half_col_len]
                c[i][j] = m[i+half_row_len][j]
                d[i][j] = m[i+half_row_len][j+half_col_len]
    return a,b,c,d

# Add the matrix together
def matrix_add(a,b):
    row_len_a = len(a[0][:])
    col_len_a = len(a[:][0])
    row_len_b = len(b[0][:])
    col_len_b = len(b[:][0])
    if row_len_a == row_len_b and col_len_a == col_len_b:
        c = [[0 for i in range(col_len_a)] for j in range(row_len_a)]
        for i in range(row_len_a):
            for j in range(col_len_a):
                c[i][j] = a[i][j] + b[i][j]
    return c

# Subtract the matrix
def matrix_subtract(a,b):
    row_len_a = len(a[0][:])
    col_len_a = len(a[:][0])
    row_len_b = len(b[0][:])
    col_len_b = len(b[:][0])
    if row_len_a == row_len_b and col_len_a == col_len_b:
        c = [[0 for i in range(col_len_a)] for j in range(row_len_a)]
        for i in range(row_len_a):
            for j in range(col_len_a):
                c[i][j] = a[i][j] - b[i][j]
    return c

# Merge the invidiaul matrices into a larger matrix
def matrix_merge(a,b,c,d):

    row_len_a = len(a[0][:])
    col_len_a = len(a[:][0])
    row_len_b = len(b[0][:])
    col_len_b = len(b[:][0])
    row_len_c = len(c[0][:])
    col_len_c = len(c[:][0])
    row_len_d = len(d[0][:])
    col_len_d = len(d[:][0])

    result = [[0 for i in range(row_len_a + row_len_c)] for t in range(col_len_a + col_len_b)]

    if row_len_a == row_len_b and col_len_a == col_len_c and col_len_b == col_len_d and row_len_c == row_len_d:

        for i in range(row_len_a):
            for j in range(col_len_a):
                result[i][j] = a[i][j]

        for i in range(row_len_b):
            for j in range(col_len_b):
                result[i][j+col_len_a] = b[i][j]

        for i in range(row_len_c):
            for j in range(col_len_c):
                result[i+row_len_a][j] = c[i][j]

        for i in range(row_len_d):
            for j in range(col_len_d):
                result[i+row_len_a][j+col_len_a] = d[i][j]
    return result

# Do strassen multiplication
# split the arrays into sub arrays, and do matrix addition and subtraction
def strassen_mult(a,b):
    row_len_a = len(a[0][:])
    col_len_a = len(a[:][0])
    row_len_b = len(b[0][:])
    col_len_b = len(b[:][0])

    a11,a12,a21,a22 = split_matrix(a)
    b11,b12,b21,b22 = split_matrix(b)
    s1 = matrix_subtract(b12,b22)
    s2 = matrix_add(a11,a12)
    s3 = matrix_add(a21,a22)
    s4 = matrix_subtract(b21,b11)
    s5 = matrix_add(a11,a22)
    s6 = matrix_add(b11,b22)
    s7 = matrix_subtract(a12,a22)
    s8 = matrix_add(b21,b22)
    s9 = matrix_subtract(a11,a21)
    s10 = matrix_add(b11,b12)
    p1 = [[]]
    p2 = [[]]
    p3 = [[]]
    p4 = [[]]
    p5 = [[]]
    p6 = [[]]
    p7 = [[]]

    if row_len_a > 2 and col_len_a > 2 and row_len_b > 2 and col_len_b >2:
        p1 = strassen_mult(a11,s1)
        p2 = strassen_mult(s2,b22)
        p3 = strassen_mult(s3,b11)
        p4 = strassen_mult(a22,s4)
        p5 = strassen_mult(s5,s6)
        p6 = strassen_mult(s7,s8)
        p7 = strassen_mult(s9,s10)
    else:
        p1[0].append(a11[0][0]*s1[0][0])
        p2[0].append(s2[0][0]*b22[0][0])
        p3[0].append(s3[0][0]*b11[0][0])
        p4[0].append(a22[0][0]*s4[0][0])
        p5[0].append(s5[0][0]*s6[0][0])
        p6[0].append(s7[0][0]*s8[0][0])
        p7[0].append(s9[0][0]*s10[0][0])

    c11 = matrix_add(matrix_add(p5,p6),matrix_subtract(p4,p2))
    c12 = matrix_add(p1,p2)
    c21 = matrix_add(p3,p4)
    c22 = matrix_subtract(matrix_add(p5,p1),matrix_add(p3,p7))


    return matrix_merge(c11,c12,c21,c22)

if __name__ == '__main__':
    main()

