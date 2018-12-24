#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as ma


# In[2]:


data = np.array([(6,1),(99,12),(87,22),(1,19),(2,3),(7,8),(21,25),(1,1),(1,55),(5,99),(57,93),(50,13),(27,28),(29,35),(99,35),(45,11),(12,19),(50,60),(90,100),(99,150),(89,103),(-10,-5),(77,107),(6,19),(9,33),(40,39),(30,41),(9,13)])


# # view data

# In[3]:


data


# In[4]:


df = pd.DataFrame(data=data)


# In[5]:


df


# In[6]:


df.loc[6:6]


# In[7]:


dfx = df[0]
dfy = df[1]


# # #visualize data

# In[8]:


plt.scatter(dfx, dfy)
plt.show()

# In[9]:


k = int(input("Enter the numberof clusters to form: "))


# In[10]:


a = {}
div = round(len(df)/k)
m={}
print(div)
print(len(df))


# In[11]:


for i in range(1,k+1):
    a[i] = []
    m[i] = df.loc[div*i-3:div*i-3].values
print(a)
print(m)


# # functions to find distance and centroid

# In[12]:


def dist(med, point):
    #print(med)
    #print(point)
    dist = ma.sqrt((med[0][0]-point[0][0])**2+(med[0][1]-point[0][1])**2)
    return dist


# In[13]:


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

# In[ ]:


for _ in range(0,20):
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
    plt.plot(range(5))
    plt.xlim(0, 150)
    plt.ylim(0, 150)
    plt.gca().set_aspect('equal')
    
    plt.show()
    for key in a:
        centroid(a[key], key)


# In[ ]:


m


# In[ ]:


m[1][:,1]


# In[ ]:


a


# In[ ]:


for key in a:
    a[key] = np.concatenate(a[key])


# In[ ]:


a


# In[ ]:


a[1][:,0]


# 
# df1x = a[1][:,0]
# df1y = a[1][:,1]
# df2x = a[2][:,0]
# df2y = a[2][:,1]
# df3x = a[3][:,0]
# df3y = a[3][:,1]

# In[ ]:


for i in range (1,k+1):
    plt.plot(a[i][:,0],a[i][:,1])
    plt.scatter(m[i][:,0],m[i][:,1])
	
plt.plot(range(5))
plt.xlim(0, 150)
plt.ylim(0, 150)
plt.gca().set_aspect('equal')
   
plt.show()
    #plt.scatter(m[i][:,0],m[i][:,1], 'o')


# In[ ]:




