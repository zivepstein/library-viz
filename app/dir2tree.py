
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


# In[26]:

import os
import json

def path_to_dict(path):
    name = os.path.basename(path)
    d = {'name': name}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path) if x[0] != '.' and name != 'app']
    else:
        d['type'] = "file"
        d['size'] = 3812
    return d

data = json.dumps(path_to_dict('/Users/ziv/GDrive/papers'))


# In[27]:

data


# In[ ]:



