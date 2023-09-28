#!/usr/bin/env python
# coding: utf-8

# ## 1. Printing, Data Types, and Input
# 

# In[4]:


name=input("Enter your name:")
print("Hello", name, "Nice to meet you")


# In[8]:


age=input("Enter your age:")


# In[11]:


print("Hello, I am", age, "years old")


# ## 2. String Manipulations and Input
# 

# In[13]:


hometown=input("Enter your hometown:")


# In[18]:


print(hometown[0:3])


# In[32]:


print(hometown[::-1])


# ## 3. Numeric Operations and Input
# 

# In[40]:


num=input("Enter a number:")


# In[52]:


num=25


# In[53]:


num*num


# In[67]:


import math


# In[69]:


math.sqrt(625)


# ## 4. Boolean Evaluations
# 

# In[70]:


x=10
y=5


# In[71]:


x>y


# In[73]:


x==y


# In[74]:


x=8
y=9


# In[75]:


x!=y


# ## 5.List Creation and Operations

# In[107]:


colors = ["red", "blue", "green"]


# In[108]:


colors


# In[110]:


colors[0]


# In[112]:


colors = ["red", "yellow", "green"]


# In[113]:


colors


# In[114]:


colors[-2]


# ## 6. Indexing and Slicing

# In[115]:


numbers = ["10", "20", "30", "40", "50"]


# In[116]:


numbers


# In[117]:


numbers[2]


# In[119]:


numbers[0:2]


# In[128]:


numbers[-3:]


# ## 7. Manipulating Elements

# In[166]:


animals = ["cat", "dog", "bird"]


# In[167]:


animals


# In[168]:


animals.append("fish")


# In[169]:


animals


# ## 8. Sorting

# In[170]:


numbers = ["42", "8", "15", "23", "16"]


# In[171]:


numbers


# In[195]:


numbers.sort()


# In[196]:


numbers


# In[200]:


numbers[1:3]

