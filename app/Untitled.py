
# coding: utf-8

# In[5]:

import os
rootdir = '/Users/ziv/GDrive/papers'
papers = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
    	f = os.path.join(subdir, file)
    	if f.split('/')[-1][0] != "." and f.split('/')[5] != "app":
    		papers.append(f)


# In[6]:

papers[0]


# In[7]:

tree = {"name" : "papers", "children" : []}


# In[13]:

route = papers[0].split('/')[5:]


# In[14]:

route


# In[ ]:



