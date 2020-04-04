#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os


# In[6]:


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        return 'Invalid Dir'
    
    path_list = os.listdir(path)
    output_list = []
    for item in path_list:
        item_path = os.path.join(path,item)
        if os.path.isdir(item_path):
            output_list += find_files(suffix,item_path)
        if os.path.isfile(item_path) and item_path.endswith(suffix):
            output_list.append(item_path)
    return output_list
   


# In[ ]:


# Default test
print("Test 1")
print(find_files('.c', './Problem 2/testdir'))


# In[ ]:


# Prints every file
print("Test 2")
print(find_files('', './Problem 2/testdir'))


# In[ ]:


# Non existent extension
print("Test 3")
print(find_files('.z', './Problem 2/testdir'))


# In[ ]:


# Non existent directory
print("Test 4")
print(find_files('.c', './asdf'))


# In[ ]:


# Empty Directory
print("Test 5")
print(find_files('.c', './Problem 2/emptydir'))

