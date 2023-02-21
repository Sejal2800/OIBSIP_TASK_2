#!/usr/bin/env python
# coding: utf-8

# # Unemployment Analysis using Python

# #### 1. Importing necessary modules 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# #### 2. Importing datasets 

# In[2]:


UA = pd.read_csv("Unemployment in India.csv")
UA = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
UA.head()


# #### 3. Analyzing dataset

# In[3]:


#Describing dataset
UA.describe()


# In[4]:


# checking null values
UA.isnull().sum()


# In[5]:


# renaming columns
UA.columns = ['State','Date','Frequency','Unemployment Rate','Employed','Labour Participation Rate','Region','Longitude','Latitude']


# #### 4. Data Visualization-Graphs 

# In[6]:


#histplot for employment data
sns.histplot(x='Employed',hue='Region',data=UA)
plt.show()


# In[7]:


# histplot for unemployed data
plt.figure(figsize=(7,5))
plt.title('Indian Unemployment')
sns.histplot(x='Unemployment Rate',hue='Region',data=UA)
plt.show()


# In[8]:


# sunburst chart for vizualization
up = UA[['State','Region','Unemployment Rate']]
figure= px.sunburst(up, path=['Region','State'], values='Unemployment Rate',width=700,height=700,color_continuous_scale='RdY1Gn',title='Unemployment Rate in India')
figure.show()


# #### 5. Corelation

# In[9]:


# checking the correlation of variables
UA.corr()


# In[10]:


#plotting correlation matrix
cor= UA.corr()
fig, ax=plt.subplots(figsize=(8,8))
sns.heatmap(cor,annot=True,ax=ax)


# 

# In[ ]:





# In[ ]:




