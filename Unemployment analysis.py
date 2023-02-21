#!/usr/bin/env python
# coding: utf-8

# # Unemployment Analysis using Python

# #### 1. Importing necessary modules 




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


#  2. Importing datasets 



UA = pd.read_csv("Unemployment in India.csv")
UA = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
UA.head()


# 3. Analyzing dataset



#Describing dataset
UA.describe()




# checking null values
UA.isnull().sum()




# renaming columns
UA.columns = ['State','Date','Frequency','Unemployment Rate','Employed','Labour Participation Rate','Region','Longitude','Latitude']


# 4. Data Visualization-Graphs 




#histplot for employment data
sns.histplot(x='Employed',hue='Region',data=UA)
plt.show()





# histplot for unemployed data
plt.figure(figsize=(7,5))
plt.title('Indian Unemployment')
sns.histplot(x='Unemployment Rate',hue='Region',data=UA)
plt.show()




# sunburst chart for vizualization
up = UA[['State','Region','Unemployment Rate']]
figure= px.sunburst(up, path=['Region','State'], values='Unemployment Rate',width=700,height=700,color_continuous_scale='RdY1Gn',title='Unemployment Rate in India')
figure.show()


#  5. Corelation



# checking the correlation of variables
UA.corr()




#plotting correlation matrix
cor= UA.corr()
fig, ax=plt.subplots(figsize=(8,8))
sns.heatmap(cor,annot=True,ax=ax)
