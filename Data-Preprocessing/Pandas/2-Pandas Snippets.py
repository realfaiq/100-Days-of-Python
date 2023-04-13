#!/usr/bin/env python
# coding: utf-8

# In[89]:


people = {
    'first': ['Faiq', 'Khan', 'Corey'],
    'last' : ['Khan', 'Khalil', 'Schaffer'],
    'email': ['faiq@gmail.com', 'khan@gmail.com', 'corey@gmail.com']
}


# In[90]:


people


# In[91]:


import pandas as pd


# In[92]:


df = pd.DataFrame(people)


# In[93]:


df


# In[94]:


#Add Columns
df['full_name'] = df['first']+ ' ' + df['last']


# In[95]:


df


# In[96]:


#Removing Columns
remove = df.drop(columns = ['first', 'last'], inplace = True)
df


# In[97]:


#Reverting the process
#expand = True to show it in rows and columns
df['full_name'].str.split(' ', expand = True)


# In[98]:


df[['first', 'last']] = df['full_name'].str.split(' ',expand = True)


# In[99]:


df


# In[100]:


#Adding a single row
df = pd.concat([df, pd.DataFrame.from_records([{ 'first': 'Tony'}])])


# In[101]:


df


# In[102]:


people = {
    'first': ['Shehzad', 'Khan'],
    'last' : ['Tony', 'Stark'],
    'email': ['shehzad@gmail.com', 'tony@gmail.com']
}


# In[103]:


df2 = pd.DataFrame(people)


# In[104]:


df2


# In[105]:


df = pd.concat([df, pd.DataFrame.from_records(df2)])


# In[106]:


df


# In[112]:


df.drop(index=0)


# In[118]:


filt = df['last'] == 'Stark'
df.drop(index = df[filt].index)


# ### Sorting

# In[121]:


df.sort_values(by = ['last','first'], ascending = False)


# In[123]:


df.sort_values(by = ['last','first'], ascending = [False, True], inplace = True)


# In[124]:


df.sort_index()


# In[125]:


df['last'].sort_values()


# In[ ]:




