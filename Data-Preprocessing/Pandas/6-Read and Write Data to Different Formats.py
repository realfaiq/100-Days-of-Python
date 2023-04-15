#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


#CSV
df = pd.read_csv('C:/Users/Dell/Desktop/data-set/survey_results_public.csv')


# In[4]:


df


# In[8]:


filt = df['Country'] == 'India'
india_df = df.loc[filt]


# In[10]:


india_df.head()


# In[15]:


india_df.to_csv('C:/Users/Dell/Desktop/data-set/modified.csv')


# In[16]:


#Tab separator files
india_df.to_csv('C:/Users/Dell/Desktop/data-set/modified.tsv', sep = '\t')


# In[17]:


#Write to Excel File
india_df.to_csv('C:/Users/Dell/Desktop/data-set/modified.xlsx')


# In[29]:


# test = pd.read_excel('C:/Users/Dell/Desktop/data-set/modified.xlsx')


# In[32]:


#JSON
#For more List like pass arguments orient = records and lines = True so every record is on different line
india_df.to_json('C:/Users/Dell/Desktop/data-set/modified.json', orient = 'records', lines = True)


# In[33]:


#Reading JSON
test = pd.read_json('C:/Users/Dell/Desktop/data-set/modified.json', orient = 'records', lines = True)


# In[34]:


test


# In[35]:


#SQL Database
# from sqlalchemy import create_engine
# engine = create_engine('postgresql://dbuser:dbpass@localhost5432/sample_db')
# india_df.to_sql('sa,ple_table', engine, if_exists = 'replace')
# sql_df = pd.read_sql('sample_table', engine, index_col = 'Respondent')
# sql_df.head()


# In[36]:


#Read a Sql Query
# sql_df = pd.read_sql('SELECT * FROM sample_table', engine, index_col = 'Respondent')


# In[ ]:


#From URL
#Same as Read but you must know the extension of data correctly.

