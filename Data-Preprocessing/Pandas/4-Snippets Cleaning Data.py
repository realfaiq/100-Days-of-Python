#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}


# In[22]:


df = pd.DataFrame(people)

df.replace('NA', np.nan, inplace = True)
df.replace('Missing', np.nan, inplace = True)


# In[23]:


df


# In[24]:


#1-Simply Delete the Data having no values
#Delete Rows having missing values
df.dropna()


# In[25]:


#This is the default behaviour in pandas as df.dropna. axis = 'index' means drop rows if we want columns we will write 
#axis = 'columns' and how = 'any' any column or row with missing values drop it
df.dropna(axis = 'index', how = 'any')


# In[26]:


#All of the values need to be missing to drop in a row or column depends on index value.
df.dropna(axis = 'index', how = 'all')


# In[27]:


df.dropna(axis = 'columns', how = 'all')


# In[28]:


#Subset Argument
#It will only look in the email column
#Also inplace for permenancy
df.dropna(axis = 'index', how = 'all', subset = ['last','email'])


# In[29]:


#To see whether values were NA or not
df.isna()


# In[33]:


#Filling with MISSING all the NA values
# df.fillna('MISSING')
#Also inplace for making changes to permenant
df.fillna(0)


# In[35]:


df.dtypes


# In[39]:


df['age'] = df['age'].astype(float)


# In[41]:


df['age'].mean()


# In[ ]:




