#!/usr/bin/env python
# coding: utf-8

# ## NumPy 
# 
# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
# 
#   - a powerful N-dimensional array object
#   - sophisticated (broadcasting) functions
#   - tools for integrating C/C++ and Fortran code
#   - useful linear algebra, Fourier transform, and random number capabilities

# In[2]:


import numpy as np 


# # PART 1 - Intro to Arrays in NumPy
# 
# Numpy has a ton of built-in functions that are useful for Data Scientists & Python Programmers alike.
# 
# We shall cover some of the most important topics in Numpy: 
# 
#   - Arrays ( using Vectors & Matrices ) 
#   - Number Generation Concepts
# 
# # Numpy Arrays
# 
# NumPy arrays are the one of the most widely used data structuring techniques by Data Scientists. 
# 
# Numpy arrays are of two types: Vectors and Matrices. 
# 
# Vectors are 1-dimensional arrays and matrices are 2-dimensional arrays(A Matrix can still possess a single row or a column).
# 
# We shall begin our learning with how to create NumPy Arrays.
# 
# ## Creating simple NumPy Array Structures
# 
# We could create a simple Array by using a list of values or a list of "List of values".

# In[2]:


simple_list = [101,102,103,104,105,106,107,108,109,110]
simple_list


# In[3]:


np.array(simple_list)


# In[4]:


simple_list_of_lists = [[10,11,12],[20,21,22],[30,31,32]]
simple_list_of_lists


# In[5]:


np.array(simple_list_of_lists)


# **There are multiple built-in methods to generate Arrays**
# 
# ### arange
# 
# Return evenly spaced values within a given interval as input.

# In[7]:


np.arange(0,20)        
# Return values 0 to 19. Start value is 0 which is included, the stop value provided is 20 which is not included


# In[8]:


np.arange(0,20,4)       # Specify start, stop and step values as input


# ### 0's and 1's
# 
# Generate arrays of 0's or 1's

# In[9]:


np.zeros(10)            # Specify the count of 0's required in the array


# In[10]:


np.zeros((4,3))         # Specify the number of rows by columns - 4 rows and 3 cols in this example


# In[11]:


np.ones(10)            # Specify the count of 1's required in the array


# In[12]:


np.ones((4,5))         # Specify the number of rows by columns - 4 rows and 5 cols in this example


# ## eye
# 
# Return a 2-D array with ones on the diagonal and zeros elsewhere. Also called an identity matrix

# In[14]:


np.eye(10)


# In[3]:


np.eye(3)


# ## Random 
# 
# Numpy has lots of options to create random numbered arrays:
# 
# ### rand
# Create an array of the given shape and populate it with random variables derived from a uniform distribution between `[0, 1)`.

# In[15]:


np.random.rand(5)


# In[16]:


np.random.rand(3,2)


# ### randn
# 
# Return a variable (or a set of variables) from the "Standard Normal" distribution. Unlike rand which is from a uniform distribution: 
# 
# A standard Normal Distribution has mean 0 and SD of 1 as we know.

# In[17]:


np.random.randn(5)


# In[18]:


np.random.randn(3,2)


# ### randint
# Return random integers from `low` (inclusive) to `high` (exclusive).

# In[19]:


np.random.randint(5,20)       # Returns one rand integer between the values 5 & 19(20 is excluded)


# In[20]:


np.random.randint(20,50,5)  # Returns  5 rand integers between 20 & 49(50 is excluded)


# ## Array Attributes and Methods for an array
# 
# Let us look at some important attributes and methods for an array.

# In[4]:


sample_array = np.arange(30)
rand_array = np.random.randint(0,100,20)


# In[5]:


sample_array


# In[23]:


rand_array


# ## Reshape
# Returns an array containing the same data with a new shape.

# In[25]:


sample_array.reshape(5,6)


# ### max,min,argmax,argmin
# 
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax

# In[26]:


rand_array


# In[27]:


rand_array.max()


# In[28]:


rand_array.argmax()


# In[29]:


rand_array.min()


# In[30]:


rand_array.argmin()


# ## Shape
# 
# Shape is an attribute that arrays have. It is not a method.

# In[31]:


# Vector
sample_array.shape


# In[32]:


# Output has two sets of brackets - which indicates a matrix and not a vector
sample_array.reshape(1,30)


# In[33]:


sample_array.reshape(1,30).shape


# In[34]:


sample_array.reshape(30,1)


# In[35]:


sample_array.reshape(30,1).shape


# ### dtype
# 
# You could retrieve the data type of the object in an array using dtype.

# In[36]:


sample_array.dtype


# In[37]:


sample_array.T


# # Part 2 - NumPy Indexing & Selection
# 
# We will now learn how to select objects or groups of objects from an array

# In[6]:


sample_array


# In[8]:


sample_array[8]


# In[39]:


#Get values from a range selection
sample_array[0:3]


# In[7]:


#Get values from specific index positions
sample_array[[0,4,7]]


# ## Indexing a Matrix - 2 dimensional arrays
# 
# The general formats used are 
# 
# **sample_matrix[row][col]** 
# 
# or
# 
# **sample_matrix[row,col]**
# 
# We will use the second option as standard.

# In[10]:


sample_matrix = np.array(([50,200,5,10],[10,35,50,15],[25,100,145,120],[105,25,65,80]))

#Show output
sample_matrix


# In[42]:


#Indexing rows
sample_matrix[1]


# In[43]:


# Getting an individual element value from the matrix - Method 1
sample_matrix[1][2]


# In[44]:


# Slicing matrix

#Shape (3,3) from top right corner
sample_matrix[:3,1:]


# In[12]:


sample_matrix[1:3,1:]


# In[11]:


#Shape bottom row - Including column selection (Alternate to above)
sample_matrix[3,:]


# ## Selection
# 
# Using brackets for selection based on operators for comparison

# In[46]:


simple_array = np.arange(1,31)
simple_array


# In[47]:


simple_array <10


# In[49]:


boolean_array = simple_array<10
boolean_array


# In[50]:


simple_array[boolean_array]


# In[51]:


simple_array[simple_array>15]


# In[52]:


a = 11
simple_array[simple_array>a]


# In[ ]:




