#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math
rdx=6.2
rdy=3.2
blux=6.5
bluy=3.0
grnx=6.6
grny=3.7
rdxc=0
rdyc=0
countrd=0
grnxc=0
grnyc=0
countgrn=0
bluxc=0
bluyc=0
countblu=0

for i in range(10):
    
    x=float(input("enter x co-ordinate of datapoints "))
    y=float(input("enter y co-ordinate f datapoints "))
    rd=math.sqrt(((rdx-x)*(rdx-x))+((rdy-y)*(rdy-y)))
    blu=math.sqrt(((blux-x)*(blux-x))+((bluy-y)*(bluy-y)))
    grn=math.sqrt(((grnx-x)*(grnx-x))+((grny-y)*(grny-y)))
    if(rd<=grn and rd<=blu):
        print("this datpoints belongs to red cluster")
        rdxc=rdxc+x
        rdyc=rdyc+y
        countrd=countrd+1
    elif(grn<=rd and grn<=blu):
        print("this datpoints belongs to green cluster")
        grnxc=grnxc+x   
        grnyc=grnyc+y
        countgrn=countgrn+1
    else:
        print("this datpoints belongs to blue cluster")
        bluxc=bluxc+x   
        bluyc=bluyc+y
        countblu=countblu+1
        
  


# In[9]:


print("new red centroid is (",rdxc/countrd,",",rdyc/countrd,")")
print("new green centroid is (",grnxc/countgrn,",",grnyc/countgrn,")")
print("new blue centroid is (",bluxc/countblu,",",bluyc/countblu,")")


# In[ ]:




