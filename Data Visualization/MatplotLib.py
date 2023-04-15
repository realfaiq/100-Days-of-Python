#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[25]:


#Basic Graph
x = [0,1,2,3,4]
y = [0,2,4,6,8]
plt.plot(x,y, 'b^--', label = '2x')
#Short Hand
plt.plot(x,y, label = '2x', color = 'red', linewidth = 1, markersize = 12, markeredgecolor = 'blue')
plt.title('Our First Graph', fontdict = {'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10])
plt.legend()
plt.show()


# In[ ]:




