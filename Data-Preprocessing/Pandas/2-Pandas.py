#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv('C:/Users/Dell/Desktop/data-set/survey_results_public.csv', index_col = 'Respondent')
df_schema = pd.read_csv('C:/Users/Dell/Desktop/data-set/survey_results_schema.csv', index_col = 'Column')


# In[5]:


df


# In[7]:


df_schema


# In[14]:


df.sort_values(by = ['Country', 'ConvertedComp'], ascending = [True, False], inplace = True)


# In[15]:


df[['Country', 'ConvertedComp']].head(50)


# In[17]:


#10 Largest from Series(Column)
df['ConvertedComp'].nlargest(10)


# In[19]:


df.nlargest(10, 'ConvertedComp')


# In[20]:


df.nsmallest(10, 'ConvertedComp')


# In[ ]:




