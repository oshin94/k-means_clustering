#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as ma


# In[2]:


data = np.array([(-10,-5),(-6,1),(2,3),(7,8),(9,13),(21,25),(27,28),(29,35),(99,35),(45,11),(12,19),(50,60),(90,100),(99,150),(89,103),(77,107),(6,19),(9,33),(40,39),(30,41)])


# In[48]:


df = pd.read_csv("cars.csv", usecols=[2,3])


# In[51]:


df


# In[52]:


df.iloc[:,0].replace(' ', np.nan, inplace=True)


# In[53]:


df.iloc[:,1].replace(' ', np.nan, inplace=True)


# In[54]:


df.dropna(inplace=True)
df.dropna(inplace=True)


# In[57]:


dfx=df.iloc[:,0].values
dfy=df.iloc[:,1].values


# In[58]:


dfx


# In[84]:


dfx = dfx.astype(int)
dfx


# In[85]:


dfy


# In[86]:


df = pd.DataFrame({'x':dfx, 'y':dfy})


# # view data

# In[87]:


df


# # #visualize data

# In[88]:


df.plot('x','y', kind='scatter')


# In[89]:


df.loc[1:1].values


# # Enter cluster numbers

# In[71]:


k = int(input("Enter the numberof clusters to form: "))


# #set initial centroids

# In[90]:


a = {}
div = round(len(df)/k)
m={}
print(div)
print(len(df))


# In[91]:


for i in range(1,k+1):
    a[i] = []
    m[i] = df.loc[div*i-2:div*i-2].values
print(a)
print(m)


# # functions to find distance and centroid

# In[92]:


def dist(med, point):
    #print(med)
    #print(point)
    dist = ma.sqrt((med[0][0]-point[0][0])**2+(med[0][1]-point[0][1])**2)
    return dist


# In[93]:


def centroid(p, key):
    x = 0
    y=0
    for i in p:
        #print (i)
        x += i[0][0]/len(p)
        y += i[0][1]/len(p)
    #print(x)
    #print(y)
    m[key] = np.array([[x,y]])


# # training

# In[76]:


for _ in range(0,10):
    for key in a:
        a[key] = []
    for i in range(0,len(df)):
        low = None
        for ke in m:
            if low is None:
                low= dist(m[ke], df.loc[i:i].values)
                temp = ke
            elif (dist(m[ke], df.loc[i:i].values) < low):
                low = dist(m[ke], df.loc[i:i].values)
                temp = ke
        a[temp].append(df.loc[i:i].values)
    a_vis={}
    for key in a:
        a_vis[key] = np.concatenate(a[key])
    for i in range (1,k+1):
        plt.plot(a_vis[i][:,0],a_vis[i][:,1])
        plt.scatter(m[i][:,0],m[i][:,1])
    # plt.plot(range(5))
    # plt.xlim(0, 500)
    # plt.ylim(0, 500)
    # plt.gca().set_aspect('equal')
    
    plt.show()
    for key in a:
        centroid(a[key], key)


# In[77]:


m


# In[78]:


m[1][:,1]


# In[79]:


a


# In[80]:


for key in a:
    a[key] = np.concatenate(a[key])


# In[81]:


a


# In[82]:


a[1][:,0]


# 
# df1x = a[1][:,0]
# df1y = a[1][:,1]
# df2x = a[2][:,0]
# df2y = a[2][:,1]
# df3x = a[3][:,0]
# df3y = a[3][:,1]

# In[83]:


for i in range (1,k+1):
    plt.plot(a[i][:,0],a[i][:,1])
    plt.scatter(m[i][:,0],m[i][:,1])
    #plt.scatter(m[i][:,0],m[i][:,1], 'o')


# In[ ]:





# In[ ]:




