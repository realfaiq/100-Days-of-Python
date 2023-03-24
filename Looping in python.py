#!/usr/bin/env python
# coding: utf-8

# In[1]:


#For Loop
fruits = ['Oranges', 'Banana', 'Apple', 'Mango']
for fruit in fruits:
    print(fruit)


# In[23]:


#For Loop
marks = []
total = 0
for i in range(0, 5):
    print('Enter the marks of Subject', i)
    marks.append(input())
    total += int(marks[i])
print('The total marks are:', total)


# In[26]:


#For Loop
for i in range(6):
    for j in range(i):
        print('*', end = '')
    print(' ')


# In[34]:


#While loop
i = 1
while i < 6:
    print(i)
    if(i == 3):
        break
    i += 1


# In[40]:


#While loop
marks = []
i = 0
total = 0
while i < 5:
    print('Enter the marks of Subject', i)
    marks.append(input())
    total += int(marks[i])
    i += 1
print('The total marks are:', total)


# In[ ]:




