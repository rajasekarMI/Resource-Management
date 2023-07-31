#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


x1=pd.read_csv("D:\Data Science\Mini Project\State1.csv",encoding='cp1252')
x1


# In[8]:


x2=pd.read_csv("D:\Data Science\Mini Project\State2.csv",encoding='cp1252')
x2


# In[9]:


x3=pd.read_csv("D:\Data Science\Mini Project\State3.csv",encoding='cp1252')
x3


# In[10]:


x4=pd.read_csv("D:\Data Science\Mini Project\State4.csv",encoding='cp1252')
x4


# In[11]:


x5=pd.read_csv("D:\Data Science\Mini Project\State5.csv",encoding='cp1252')
x5


# In[12]:


x6=pd.read_csv("D:\Data Science\Mini Project\State6.csv",encoding='cp1252')
x6


# In[13]:


x7=pd.read_csv("D:\Data Science\Mini Project\State7.csv",encoding='cp1252')
x7


# In[14]:


x8=pd.read_csv("D:\Data Science\Mini Project\State8.csv",encoding='cp1252')
x8


# In[15]:


x9=pd.read_csv("D:\Data Science\Mini Project\State9.csv",encoding='cp1252')
x9


# In[16]:


x10=pd.read_csv("D:\Data Science\Mini Project\State10.csv",encoding='cp1252')
x10


# In[17]:


x11=pd.read_csv("D:\Data Science\Mini Project\State11.csv",encoding='cp1252')
x11


# In[18]:


x12=pd.read_csv("D:\Data Science\Mini Project\State12.csv",encoding='cp1252')
x12


# In[19]:


x13=pd.read_csv("D:\Data Science\Mini Project\State13.csv",encoding='cp1252')
x13


# In[20]:


x14=pd.read_csv("D:\Data Science\Mini Project\State14.csv",encoding='cp1252')
x14


# In[21]:


x15=pd.read_csv("D:\Data Science\Mini Project\State15.csv",encoding='cp1252')
x15


# In[22]:


x16=pd.read_csv("D:\Data Science\Mini Project\State16.csv",encoding='cp1252')
x16


# In[23]:


x17=pd.read_csv("D:\Data Science\Mini Project\State17.csv",encoding='cp1252')
x17


# In[24]:


x18=pd.read_csv("D:\Data Science\Mini Project\State18.csv",encoding='cp1252')
x18


# In[25]:


x19=pd.read_csv("D:\Data Science\Mini Project\State19.csv",encoding='cp1252')
x19


# In[26]:


x20=pd.read_csv("D:\Data Science\Mini Project\State20.csv",encoding='cp1252')
x20


# In[27]:


x21=pd.read_csv("D:\Data Science\Mini Project\State21.csv",encoding='cp1252')
x21


# In[28]:


x22=pd.read_csv("D:\Data Science\Mini Project\State22.csv",encoding='cp1252')
x22


# In[29]:


x23=pd.read_csv("D:\Data Science\Mini Project\State23.csv",encoding='cp1252')
x23


# In[30]:


df=pd.concat([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23],ignore_index=True)
df


# In[31]:


df1=df.dropna()
df1


# In[69]:


df1.dropna(inplace=True)
df1


# In[70]:


print(df1.duplicated())


# In[71]:


df1.drop_duplicates(inplace=True)


# In[72]:


# Commented out IPython magic to ensure Python compatibility.
import seaborn as sn
import matplotlib.pyplot as plt
# %matplotlib inline
import scipy.stats as st


# In[73]:


df1['Main Workers - Total -  Persons']


# In[74]:


#Main Workers - Total - Males,Main Workers - Total - Females
df1["Main Workers - Total - Males"],["Main Workers - Total - Females"]
sn.boxplot(x='Main Workers - Total - Males',y="Main Workers - Total - Females",data=df1)
plt.show()
st.f_oneway(df1["Main Workers - Total - Males"],df1["Main Workers - Total - Females"])


# In[75]:


#Main Workers - Rural - Females,Main Workers - Rural - Males
df1["Main Workers - Rural - Females"],["Main Workers - Rural - Males"]
sn.boxplot(x='Main Workers - Rural - Females',y="Main Workers - Rural - Males",data=df1)
plt.show()
st.f_oneway(df1["Main Workers - Rural - Females"],df1["Main Workers - Rural - Males"])


# In[76]:


df1["Main Workers - Urban - Males"],["Main Workers - Urban - Females"]
sn.boxplot(x='Main Workers - Urban - Males',y="Main Workers - Urban - Females",data=df1)
plt.show()
st.f_oneway(df1["Main Workers - Urban - Males"],df1["Main Workers - Urban - Females"])


# In[77]:


#Marginal workers-Total-Persons,Marginal workers-Total-Male
df1["Marginal Workers - Total -  Persons"],["Marginal Workers - Total - Males"]
sn.boxplot(x='Marginal Workers - Total -  Persons',y="Marginal Workers - Total - Males",data=df1)
plt.show()
st.f_oneway(df1["Marginal Workers - Total -  Persons"],df1["Marginal Workers - Total - Males"])


# In[78]:


#Marginal workers-Rural-Persons,Marginal workers-Rural-Female
df1["Marginal Workers - Rural -  Persons"],["Main Workers - Rural - Females"]
sn.boxplot(x='Main Workers - Rural -  Persons',y="Main Workers - Rural - Females",data=df1)
plt.show()
st.f_oneway(df1["Main Workers - Rural -  Persons"],df1["Main Workers - Rural - Females"])


# In[79]:


#Marginal workers-Rural-Male,Marginal workers-Rural-Female
df1["Marginal Workers - Rural - Males"],["Marginal Workers - Rural - Females"]
sn.boxplot(x='Marginal Workers - Rural - Males',y="Marginal Workers - Rural - Females",data=df1)
plt.show()
st.f_oneway(df1["Marginal Workers - Rural - Males"],df1["Marginal Workers - Rural - Females"])


# In[80]:


#entire full data
sn.boxplot(data=df1,palette='Blues',orient='h')


# In[81]:


#states
df["India/States"].hist(bins=25)


# In[82]:


print(df.head)


# In[83]:


print(df.columns)


# In[84]:


print(df.info())


# In[85]:


state_counts = df.groupby(['State Code', 'NIC Name']).size().reset_index(name='Counts')


# In[86]:


pip install seaborn     


# In[87]:


import seaborn as sns


# In[88]:


plt.figure(figsize=(12, 6))
sns.barplot(x='State Code', y='Counts', hue='NIC Name', data=state_counts)
plt.xticks(rotation=90)
plt.xlabel('State Code')
plt.ylabel('Counts')
plt.title('State-wise Counts of Industrial Classification')
plt.show()


# In[92]:


df[df['NIC Name'].str.contains('plastic')]


# In[93]:


df[df['NIC Name'].str.contains('rubber')]


# In[94]:


df[df['NIC Name'].str.contains('chemical')]


# In[95]:


df[df['NIC Name'].str.contains('furniture')]


# In[99]:


df[df['NIC Name'].str.contains('building')]


# In[100]:


df[df['NIC Name'].str.contains('retail')]


# In[ ]:




