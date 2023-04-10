#!/usr/bin/env python
# coding: utf-8

# ### Load Numpy
# 

# In[ ]:


import numpy as np


# ### Basics

# In[62]:


a = np.array([1,2,3], dtype = 'int16')
print(a)


# In[63]:


#2-D Array
b = np.array([[5.0,6.0,7.0], [3.0,2.0,8.0]])
print(b)


# In[64]:


#Get Dimension
a.ndim
b.ndim


# In[65]:


#Shape(Rows and Columns)
a.shape
b.shape


# In[66]:


#Get Type
a.dtype


# In[67]:


#Get Size
a.itemsize


# In[68]:


#Get Total Size
a.nbytes


# In[69]:


#2D Array
c = np.array([[1,2,3,4,5,6,7], [10,11,12,13,14,17,16]])
print(c)


# In[70]:


#Getting a specific element [r,c]
c[1,5]


# In[71]:


#Getting a specific row
c[0, :]


# In[72]:


#Getting a specific column
c[:, 3]


# In[73]:


#Little more fancy [startindex:endindex:steps]
c[0, 1:6:2]


# In[74]:


#Changing element
c[0, 2] = 4
print(c)


# In[75]:


#Changing element of column
c[:, 2] = [1,2]
print(c)


# In[76]:


#3D Array
d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(d)


# In[77]:


#Get Specific Element(Works outside in) (Set, Row/Column, Element)
d[1,1,:]


# In[78]:


#Replacing
d[1,:,:] = [[9,9], [8,8]]
print(d)


# In[79]:


#Initializing Different Types of Arrays
#All Zeros matrix
np.zeros((2,3))


# In[80]:


#All 1's matrix (Dimension, Rows, Columns)
np.ones((4,2,2), dtype = 'int16')


# In[81]:


#Any other number
np.full((2,2), 99)


# In[82]:


#Like any other array
np.full_like(a, 4)


# In[83]:


#Random decimal numbers
np.random.rand(4,2)


# In[84]:


#Rabdom Integer Value
np.random.randint(4,7, size=(3,3))


# In[85]:


#Identity Matrix
np.identity(3)


# In[86]:


#Repeat an Array
arr = [[1,2,3]]
r1 = np.repeat(arr, 3, axis = 0)
print(r1)


# In[87]:


output = np.ones((5,5))
print(output)
z = np.zeros((3,3))
print(z)
z[1,1] = 9
print(z)
output[1:4, 1:4] = z
print(output)


# In[89]:


#Copying Arrays
e = np.array([1,2,3])
f = e.copy()
print(e)
f[1] = 100
print(f)


# ### Mathematics

# In[90]:


e + 2


# In[91]:


e - 2


# In[92]:


e / 2


# In[93]:


e + f


# In[95]:


e ** 2


# In[96]:


#Take the Sin
np.sin(e)


# ### Linear Algebra

# In[99]:


#Multiplying Matrixes
g = np.ones((2,3))
print(g)
h = np.full((3,2), 2)
print(h)

np.matmul(g,h)


# In[100]:


#Determinant of a Matrix
i = np.identity(3)
np.linalg.det(i)


# ### Statistics

# In[102]:


stats = np.array([[1,2,3], [4,5,6]])
print(stats)


# In[103]:


np.min(stats)


# In[106]:


np.max(stats, axis = 0)


# ### Reorganizing Arrays

# In[110]:


before = np.array([[1,2,3,4], [5,6,7,8]])
print(before)

after = before.reshape((8,1))
print(after)


# In[113]:


#Vertically Stacking Matrix
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
np.vstack([v1,v2,v1,v1])


# In[116]:


#Horizontal Stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

np.hstack((h1,h2))


# ### Miscillineous
# Load Data from Files

# In[133]:


fileData = np.genfromtxt('C:/Users/Dell\Desktop/data.txt', delimiter = ',')
fileData = fileData.astype('int32')
print(fileData)


# ### Boolean Masking and Advanced Indexing

# In[125]:


#Gives true where value is greater than 50 and false otherwise
fileData > 50


# In[126]:


#For Value you'll have to use
fileData[fileData > 50]


# In[130]:


#You can index with a list in numPy
y = np.array([1,2,3,4,5])
y[[1,2,4]]


# In[142]:


np.any(fileData > 50, axis = 0)


# In[143]:


((fileData < 50) & (fileData < 100))


# In[ ]:




