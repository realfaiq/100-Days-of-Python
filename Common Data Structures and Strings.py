#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Lists (Mutable)
fruits = ['Oranges', 'Apples', 'Mangoes', 'Bananas', 'Grapes']
print(fruits)
fruits[0] = 'Peach' #Changing the element in the first index
print(fruits)


# In[8]:


#Tuples (Immutable)
courses = ('Maths', 'Science', 'History')
print(courses)
# course[0] = 'Geometry' Gives Error becuase tuples are immutable


# In[9]:


#Sets (Avoid Duplicates)
basket = {'apples', 'apples', 'oranges', 'mangoes'}
print(basket)


# In[11]:


#Dictionary (Key value pairs and they are immutable)
person_dict = {'Name' : 'John', 'Age' : 22, 'Country' : 'United States'}
print(person_dict)


# In[28]:


#Different Methods in List
flavors = ['Chocolate', 'Vanilla', 'Mango']
print(flavors)
print(flavors[0]) #1st index is the 0
print(flavors[-1]) #Negative Indexes -1 prints the last value
flavors.append('Strawberry') #Append adds it to the last of List
print(flavors)
flavors.insert(1, 'Mint Chocolate Chip') #Inserting at your specified location
print(flavors)
print(flavors[0:2]) #Slicing in list (First Index is included but not the last one)
flavors.remove('Mango') #Removing element from a List
print(flavors)
print(flavors.index('Mint Chocolate Chip')) #Finding the element by index
flavors.sort() #Sorting the List
print(flavors) 
flavors.sort(reverse=True) #Sorting in Reverse Order
print(flavors)
print(min(flavors)) #Finding the minimum value
print(max(flavors)) #Finding the maximum value
flavors_str = '-'.join(flavors) #Joining Values by -
print(flavors_str)


# In[31]:


#Strings in Python
course = 'Python Programming'
print(len(course)) #Length of Course
print(course[0]) #Accessing a character from string
print(course[0:2]) #Slicing in Strings


# In[37]:


#Cancatenation
first_name = 'John'
last_name = 'Doe'
print(first_name + last_name)


# In[38]:


#Formatter Strings
first_name = 'John'
last_name = 'Doe'
full = f"{first_name} {last_name}"
print(full)


# In[47]:


#String Methods
course_1 = ' Computer Science '
print(course_1.upper())
print(course_1.lower())
print(course_1.title())
print(course_1.strip())
print(course_1.find("Sc"))
print(course_1.replace("c", "p"))
print("Comp" in course_1)
print("Compu" not in course_1)


# In[ ]:




