#!/usr/bin/env python
# coding: utf-8

# In[3]:


n=int(input("Enter the value of n "))


# In[4]:


ls=[None]*n
for i in range(n):
    val=int(input("enter the value"))
    ls[i]=val


# In[9]:


for i in range(n):
    for j in range(i,n-1):
        if(ls[j]>ls[j+1]):
            temp=ls[j]
            ls[j]=ls[j+1]
            ls[j+1]=temp
print(ls)


# In[12]:


sum=0
for i in range(n):
    sum+=ls[i]
mean=sum/n
print(mean)


# In[13]:


if(n%2==0):
    print((ls[n//2]+ls[(n//2)-1])//2)
if(n%2!=0):
    print(ls[n//2])


# In[16]:


a=[4,5,6,7,8]
n-len(a)
if(n%2==0):
    print((a[n//2]+a[(n//2)-1]/2))
else:
          print(a[n//2])


# In[36]:


sum=0
for i in range(n):
    sum+=(ls[i]-mean)**2
sd=math.sqrt(sum/n)
print(sd)


# In[38]:


variance=sd**2


# In[39]:


print(variance)


# In[ ]:




