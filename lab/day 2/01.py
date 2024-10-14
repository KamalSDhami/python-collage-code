import numpy as np 

#check the version of numpy
print(np.__version__)

#create an np array 
arr = np.array([1,2,3,4])
print(type(arr))
print(f"Element of np array are : ",arr)

#check if array have an 0 inside it
print(np.all(arr))

#create an arry with element-wise for (nan (not a number ))and printit 
a = np.array([1,0,np.nan,np.inf])
print(np.isnan(a))


#check if number is complexx
a = np.array([1+5j,2j+2])
print(np.iscomplex(a))

#display the size of array
print("%d byites "%(x.size))

# create an array of intergers from 30 to 50
arr = np.arange(30,71)
print(arr)

x_2d = np.identity(3)
print(x_2d)

#create a numpy array 'm' containing integer from 10 to 21 and resape it to 3x4 matrix
m = np.arange(10,22).reshape((3,4))
print(m)

#create a 10 x 10 matrix filled with zeros using np.zeros
x =np.zeros((10,10))
print(x)
#create a 10 x 10 matrix filled with ones using np.ones
x =np.ones((10,10))
print(x)

#slice the array 
x[1:-1,1:-1]= 0
print(x)

#sum of all element 
print(np.sum(x))

#calculate the sum of column
print(np.sum(x,axis=0))

#calculate the sum of row
print(np.sum(x,axis=1))

#to check if the 2 array are equal 
nums1 = nums2 = np.arange(10,20)
print(np.equal(nums1,nums2))

#sorting the array by rows in in ascending order 
nums= np.random.randint(1,100,[2,3])
print(np.sort(nums))

#sorting the array by columns in ascending order
print(np.sort(nums,axis=0))

#print all the value grater then 5 
n =5 
print("Element gratere then 5 in array :",nums[nums >n])

#replace the number n with r in array 
n =8.32
r=18.32
print(np.where(nums ==n,r,nums))

#multiply 2 arrays
print(np.multiply(nums1,nums2))