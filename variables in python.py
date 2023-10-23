#!/usr/bin/env python
# coding: utf-8

# # Variables in python

# in memory spacevariable acts a container to store data

# 2.variable are pointer towards object in python

# 2.variable acts as container to store data in memory space

# 3.variable can start with letter or underscore. 

# 4.you can not include special character while create variable

#  important points to remember while creating a variable 

# 1.pyhton is case sensitive

# 2.if variable name involves more than two words then,join those words with underscore 

# 3.give meaningful name to variables

# In[2]:


# variable 
10


# In[4]:


a= 10
a


# In[5]:


id(a)      #inbuilt function appear in green


# In[6]:


2name = python


# In[9]:


name = 'python'
name


# In[12]:


name2 =  'python'
name2


# In[16]:


@name= 'python' # u can not use special symbol while creating variable


# In[17]:


# single line comment 


# In[19]:


age = 60 # age variable contain 60 value
age


# In[20]:


# this is ingle line comment
#this is second comment


# In[21]:


# multiline comment
'''this is firdt line comment. this is second line comment
this is third line comment 
this is fourth line comment'''           # for multile comment use'''  '''  .


# # Data types in python

#  1.integer

# 2.float

# 3.string

# 4.boolean

# In[25]:


#Integer
pin_code =456478
pin_code


# In[43]:


type(pin_code)


# In[45]:


temp=2.5
type(temp)


# In[47]:


logical = True
logical


# In[48]:


type(logical)


# In[49]:


#string creation


# In[52]:


a =50
a=100
a


# In[56]:


s ='we are learning python'
s1 = 'we are learning python'
s2 = 'we are learning python'


# In[54]:


s==s1


# In[57]:


s==s2


# In[59]:


st = 'it's a laptop'    # when we use string inside single string string is incomplete
st ="it's a laptop "


# In[61]:


st = "it's a laptop "
st


# In[63]:


st1 = 'it"a laptop'
st1


# # Typecasting

# type casting is used to change data type

# In[66]:


age   # age = 60 previously
type(age)


# In[ ]:





# In[68]:


x = str(age)  # 'str' string 


# In[69]:


type(x)


# In[70]:


int(x)


# In[72]:


y= int(age)
type(y)


# In[73]:


int(y)


# In[75]:


int(y) == int(x)


# In[76]:


float(age)


# In[77]:


age


# In[79]:


int(age)
int(x) == int (age)


# In[81]:


bool(-5)


# In[83]:


zero = 0
bool(zero)


# In[84]:


# We can create any type of value to bool type and the output for all the value will be true only for '0' it will be false 


# # String type

# In[85]:


# create a string
 s


# In[86]:


# capitalize function 


# In[89]:


s1 = 'we are learning python'
s.capitalize()


# In[90]:


s.capitalize()


# In[91]:


# count 


# In[93]:


s.count('a')


# In[94]:


s.count(' ')


# In[95]:


# startswith and endswith function 


# In[96]:


s


# In[100]:


s.startswith('we')  # tell us 's' starts with we


# In[101]:


s.endswith('n')    # tells up  's' end with n


# In[102]:


s.endswith('N')     # since it doesn't end up with N then its false 


# In[103]:


#find 


# In[105]:


s


# In[106]:


s.find('learning')  # find function show the position of learning


# In[107]:


s.find('we')


# In[108]:


# replace


# In[109]:


s


# In[119]:


s.replace('we','they')


# In[111]:


s


# In[113]:


s = s.replace('we','they')
s


# In[114]:


# Basic function


# In[116]:


s.upper()


# In[117]:


s.lower()


# In[118]:


s


# # Data structure

# 1.list

# 2.tuple

# 3.dictionary

# 4.sets

# # lists

# list are built in data structure in python

# list are heterogeneous data strucutre

# list are mutable structure

# In[121]:


# list are mutable


# In[124]:


lst = []
type(lst)


# In[128]:


lst = [10,10.2 ,True,'python']
lst


# In[130]:


#append


# In[133]:


lst.append('R')     # append means add R in lst


# In[132]:


lst


# In[134]:


#count


# In[135]:


lst.count('R')


# In[136]:


lst.count('python')


# In[138]:


#INDEX
lst.index('R')


# In[139]:


lst.index('python')


# In[140]:


#INSERT


# In[141]:


lst


# In[142]:


lst.insert(0,1000)      # put 1000 at the '0' place


# In[143]:


lst


# In[144]:


lst.insert(3,'analyst')  #put analyst at the 3rd position in lst 


# In[145]:


lst


# In[146]:


#pop


# In[ ]:





# In[ ]:




