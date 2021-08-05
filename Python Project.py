#!/usr/bin/env python
# coding: utf-8

# In[12]:


#File project Jawaher Alrabiah - 
# data processing,
# Importing required libraries
import pandas as pd 
import numpy as np
#import libraries for visualisation
import seaborn as sns 
import matplotlib.pyplot as plt 
sns.set(color_codes=True)
# Read Data File open file with open() and when finish must close the file with close()
f =open("Copy of CrystalPools.csv","r")
# print file name 
print(f.name)
f.close()

# using with means to open file and allow us to work with file in this block,no need to close() file 
with open('Copy of CrystalPools.csv', 'r') as f:
    f_cont = f.readline()
    print(f_cont, end='')
    
    f_cont = f.read(100)
    print(f_cont, end='')
    
    size_to_read = 10 
    f_cont = f.read(size_to_read)
    print(f.tell())


# In[2]:


#Loading the data into the data frame
d = pd.read_csv("Copy of CrystalPools.csv")
# To display the top 5 rows of data file
d.head(5)


# In[4]:


# To display the botton 5 rows
d.tail(5)


# In[5]:


#checking types of data 
d.dtypes


# In[ ]:





# In[6]:


# Dropping irrelevant columns
#d = d.drop(['Transaction Number', 'Profit', 'Commision 10%'], axis=1)
d = d.drop(['Transaction Number','Profit','Commision 10%'], axis=1)
d.head(5)


# In[ ]:


d.head()


# In[3]:


# shape in python is the  number of elements in each dimension
# Total number of rows and columns
d.shape


# In[8]:


#  Renaming the columns 
# Rows containing duplicate data
duplicate_rows_d = d[d.duplicated()]
print("number of duplicate rows:", duplicate_rows_d.shape)


# In[9]:


# Finding the null values.
print(d.isnull().sum())


# In[13]:


#Detecting Outliers
sns.boxplot(x=d['Sale Price'])


# In[20]:


# Plotting a Histogram
#visualisation
import matplotlib.pyplot as plt 
# An "interface" to matplotlib.axes.Axes.hist() method
#d, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
#d.Product Description.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
#plt.title("Number of Product through Months")
#plt.ylabel("Month")
#plt.xlabel("Product Description");


# In[22]:


# Finding the relations between the variables.
plt.figure(figsize=(20,10))
c= d.corr()
sns.heatmap(c,cmap='BrBG',annot=True)
c


# In[44]:


#### Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime
# matplotlib histogram
#plt.hist(['Product Descriptiony'], color = 'blue', edgecolor = 'black',
 #        bins = int(12))

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Month')
plt.ylabel('Product Descriptiony')
plt.title('My Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = d.max()


df2 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])

fig, ax = plt.subplots()
bins = np.arange(1,14)
ax.hist(months, bins = bins, edgecolor="k", align='left')
ax.set_xticks(bins[:-1])
ax.set_xticklabels([datetime.date(1900,i,1).strftime('%b') for i in bins[:-1]] )

plt.show()


# In[ ]:




