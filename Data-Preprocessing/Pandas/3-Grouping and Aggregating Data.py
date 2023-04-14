#!/usr/bin/env python
# coding: utf-8

# In[161]:


import pandas as pd


# In[162]:


df = pd.read_csv('C:/Users/Dell/Desktop/data-set/survey_results_public.csv', index_col = 'Respondent')
df_schema = pd.read_csv('C:/Users/Dell/Desktop/data-set/survey_results_schema.csv', index_col = 'Column')


# In[163]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[74]:


#Aggregatin 
df['ConvertedComp'].head(15)


# In[75]:


df['ConvertedComp'].median()


# In[166]:


# df.median() Error
df['MainBranch'].unique() #Solve this way with loop
df['MainBranch'] = df['MainBranch'].replace('I am a student who is learning to code', 0, inplace = True)


# In[77]:


df.describe()


# In[78]:


df['ConvertedComp'].count()


# In[82]:


df['Hobbyist'].value_counts()


# In[84]:


df_schema.loc['SocialMedia']


# In[85]:


df['SocialMedia'].value_counts()


# In[87]:


#If we want by percentage
df['SocialMedia'].value_counts(normalize = True)


# In[88]:


#Grouping


# In[89]:


df['Country'].value_counts()


# In[91]:


#Grouping has three Operations
#1. Splitting
country_grp = df.groupby(['Country'])


# In[94]:


country_grp.get_group('Pakistan')


# In[98]:


filt = df['Country'] == 'United States'
df.loc[filt]['SocialMedia'].value_counts()


# In[104]:


country_grp['SocialMedia'].value_counts(normalize = True).loc['Pakistan']


# In[108]:


country_grp['ConvertedComp'].median().loc['United States']


# In[110]:


country_grp['ConvertedComp'].agg(['median', 'mean']).loc['Pakistan']


# In[118]:


filt = df['Country'] == 'United States'
df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()


# In[121]:


country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())


# In[124]:


country_respondents = df['Country'].value_counts()
country_respondents


# In[125]:


country_people_knows_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())


# In[132]:


python_df = pd.concat([country_respondents, country_people_knows_python], axis='columns', sort=False)


# In[133]:


python_df


# In[145]:


python_df.rename(columns = {'count': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace = True)


# In[146]:


python_df


# In[147]:


python_df['PctKnowsPython'] = (python_df['NumKnowsPython'] / python_df['NumRespondents']) * 100


# In[148]:


python_df


# In[152]:


python_df.sort_values(by = 'PctKnowsPython', ascending = False, inplace = True)


# In[153]:


python_df.head(50)


# In[154]:


python_df.loc['Japan']


# In[ ]:




