#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


na_vals = ['NA', 'Missing']
df = pd.read_csv('C:/Users/Dell/Desktop/data-set/survey_results_public.csv', index_col = 'Respondent', na_values = na_vals)
df_schema = pd.read_csv('C:/Users/Dell/Desktop/data-set/survey_results_schema.csv', index_col = 'Column')


# In[5]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[8]:


df['YearsCode'].head(10)


# In[10]:


df['YearsCode'].unique()


# In[11]:


df['YearsCode'].replace('Less than 1 year', 0, inplace = True)
df['YearsCode'].replace('More than 50 years', 51, inplace = True)


# In[13]:


df['YearsCode'].unique()


# In[14]:


df['YearsCode'] = df['YearsCode'].astype(float)


# In[15]:


df['YearsCode'].mean()


# In[16]:


df['YearsCode'].median()


# In[ ]:




