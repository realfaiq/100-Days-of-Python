#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd


# In[37]:


# d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
#Because Already Parsed
# df = pd.read_csv('C:/Users/Dell/Desktop/data-set/ETH_1h.csv', parse_dates = ['Date'], date_parser = d_parser)
df = pd.read_csv('C:/Users/Dell/Desktop/data-set/ETH_1h.csv')


# In[38]:


df.head()


# In[39]:


df.loc[0, 'Date']


# In[40]:


df['Date'] = pd.to_datetime(df['Date'])


# In[41]:


df['Date']


# In[42]:


df.loc[0, 'Date'].day_name()


# In[43]:


df['Date'].dt.day_name()


# In[44]:


df['DayOfWeek'] = df['Date'].dt.day_name()


# In[45]:


df


# In[46]:


df['Date'].min()


# In[47]:


df['Date'].max()


# In[48]:


df['Date'].max() - df['Date'].min()


# In[49]:


filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))


# In[50]:


df.loc[filt]


# In[51]:


df.set_index('Date', inplace = True)


# In[65]:


# df['2020']


# In[66]:


df


# In[67]:


df['2020-01': '2020-05']


# In[69]:


df['2020-01': '2020-05']['Close'].mean()


# In[70]:


df['2020-01': '2020-05'].head(24)


# In[74]:


# df['2020-01-01']['High'].max()


# In[76]:


highs = df['High'].resample('D').max()
highs['2020-01-01']


# In[77]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[78]:


highs.plot()


# In[80]:


# df.resample('W').mean()


# In[82]:


df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})


# In[ ]:




