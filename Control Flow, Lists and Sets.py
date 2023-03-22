#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Control Flow
temprature = 14
raining = False
if(temprature <= 14 and not raining):
    print('You can go for outing')
else:
    print('You can not go for outing')


# In[7]:


#Ternary Opertor
a = 10
b = 10
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")


# In[9]:


#if Elif
marks = 64
if(marks > 90):
    print("A")
elif(marks > 80 and marks < 90):
    print("B")
elif(marks > 70 and marks < 80):
    print("C+")
elif(marks > 60 and marks < 70):
    print("C")
else:
    print("F")


# In[10]:


#Lists
courses = ['Maths', 'Science', 'English']
print(courses)


# In[11]:


#Slicing in Lists
print(courses[0:2])


# In[12]:


#Appending and Inserting
courses.append('Islamiyat')
courses.insert(0, 'Computer')
print(courses)


# In[13]:


#Extending the List
new_courses = ['newsubject']
courses.extend(new_courses)
print(courses)


# In[14]:


#Removing from List
courses.remove('Maths')
print(courses)


# In[17]:


#Sorting and Revresing a List
num = [1,8,7,9,10,65]
# num.sort()
num.sort(reverse=True)
print(num)


# In[18]:


#Min, Max and Sum
print(min(num))
print(max(num))
print(sum(num))


# In[21]:


#Finding the index of values
print(courses.index('English'))


# In[22]:


#Checking for the availability of item in the List
print('English' in courses)


# In[23]:


#Looping through Lists
for item in courses:
    print(item)


# In[25]:


#Converting the List through Join method
courses_str = '-'.join(courses)
print(courses_str)


# In[26]:


#Sets
courses_1 = {'History', 'English', 'Maths'}
print(courses_1)


# In[30]:


#Intersection and difference in Sets
courses_2 = {'History, English', 'Science'}
print(courses_1.intersection(courses_2))
print(courses_1.difference(courses_2))
print(courses_1.union(courses_2))


# In[33]:


#Nested Conditionals
temprature = 14
rain = True
if temprature < 20:
    if not rain:
        print('You can go for outing!')
    else:
        print('It is raining!, You can\'t go')
else:
    print('Temprature is too hot!, You can\'t go')


# In[ ]:




