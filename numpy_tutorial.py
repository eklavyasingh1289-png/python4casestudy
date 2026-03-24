import numpy as np
arr = np.array([1,2,3,4])
print(arr)
print(type(arr))

#0D array 
ar1 = np.array(11)
print(ar1)

#1D array
ar2 = np.array([1,2,3,4,5,5,7])
print(ar2)

#2D array
ar3 = np.array([[2,3,4],[1,5,5]])
print(ar3)

#3D array
ar4 = np.array([[[4,6],[2,3]],[[4,2],[4,5]]])
print(ar4)

print(ar2.ndim)
print(ar4.ndim)

#higher dimensions
ar5 = np.array([1,2,3,4,45],ndmin=5)
print(ar5)
print(ar5.ndim)

#indexing(same as python)
print(arr[0]+ar2[0])
print(ar3[0,1])
#/*indexing is done with a comma*/
print(ar4[0,1,0])
print(arr[-2])
#/*negative indexing starts from the back*/


#slicing 2D arrays
print(ar3[0,0:2])







#     DATATYPES IN NUMPY

ar6 = np.array([1,4,312],dtype='S')
print(ar6.dtype)
ar7 = np.array([1,3,4],dtype="i4")
print(ar7)
print(ar7.dtype)
#Integer after datatype specifies how much memory you wanna allocate to each element

newar = ar7.astype("S")
print(newar)
#astype copies and changes datatype as per the parameter


#     VIEW AND COPY
newar1 = ar7.view()
newar1[1]=2
print(ar7)
print(newar1)

newar2 = ar7.copy()
newar2[1] = 8
print(newar2)
print(ar7)

#View just views the original array and all changes made are reflected in the original array meanwhile copy is a whole different array

print(newar1.base)
#base function is used to identify a view array and returns the base array if the give array is a view otherwise returns none





print(ar3.shape)
#The example above returns (3,3) as ar3 has 2 dimensions with 3 elements each

 