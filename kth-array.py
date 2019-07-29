# kth smallest element
#
# https://www.geeksforgeeks.org/kth-smallest-element-in-a-subarray/

'''
Given an array arr of size N. The task is to find the kth smallest element in the subarray(l to r, both inclusive).

Note :

Query are of type query(l, r, k)
1 <= k <= r-l+1
There can be mutiple queries.

This is the 'naive' implementation - it does not use segment trees.
'''



# query(left, right, k)
def query(l, r, k):
    # Note: assumes arrays start from 1, not 0
    if l < 1 or r > len(array):
        print("Invalid l,r inputs")
        exit(1)
    if not (1 <= k and k <= r-l+1):
        print("Invalid k")
        exit(1)
    slice = sorted(array[l-1:r])
    return slice[k-1]


my_l = 2
my_r = 6
my_k = 3
array = [3, 2, 5, 4, 7, 1, 9]

print("Array = ",array)
print("Query (%d, %d, %d) = %d" % (my_l, my_r, my_k, query(my_l, my_r, my_k)))

my_l = 1
my_r = 5
my_k = 2
array = [2, 3, 4, 1, 6, 5, 8]

print("Array = ",array)
print("Query (%d, %d, %d) = %d" % (my_l, my_r, my_k, query(my_l, my_r, my_k)))