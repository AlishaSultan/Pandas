#!/usr/bin/env python
# coding: utf-8

# # Pandas is a library of python used for data analysis , fast , flexible , build on the top of python programming lanuage. like hamaray pass data hai us ko analyze krna hai us ko smjhna hai tu pandas jaisa tool use hoo ga . It is used for manipulation

# # pandas contain the different objects. Famous objects are dataframe and Series
Pandas Series:

    Pandas Series is like a column in the table.It is 1d array holding  data of any type.
    
 
 salary       experience       age
 -----         
 -----
 -----
 -----  -------------> column is called Series
 -----
 -----
 -----
 
# In[2]:


import numpy as np
import pandas as pd


# # how to make series::::::::::::::::::::::::
# 
# 
# Series from list:

# In[37]:


country = ['Pakistan' , 'India' , 'London' , 'Australia' , 'UK' , 'Germany']

final=pd.Series(country)    #---------->Series ak class hai pandas mei us ka object bnai gy

final


#It contain the values and indexes 

#pandas strings ko object  smjhta hai .........


# In[41]:


country = ['Pakistan' , 'India' , 'London' , 'Australia' , 'UK' , 'Germany']

final=pd.Series(country , name = 'Countries_name')    #---------->Series ak class hai pandas mei us ka object bnai gy

final


# In[54]:


runs = [12 , 13 , 14 , 15 , 16 , 17 , 18]

pd.Series(runs)


# In[55]:


runs = [12 , 13 , 14 , 15 , 16 , 17 , 18]

pd.Series(runs , dtype = np.int32)


# In[43]:


subjects = ['English' , 'Urdu' , 'Maths' , 'programming' , 'Isl']
marks = [98 , 100 , 100 , 50 , 100]

pd.Series( marks , index = subjects)


# In[45]:


subjects = ['English' , 'Urdu' , 'Maths' , 'programming' , 'Isl']
marks = [98 , 100 , 100 , 50 , 100]

marks = pd.Series( marks , index = subjects , name = "Alisha's score")

marks


# # Series in dictionary

# In[17]:


marks = {
    'english': 100,
    'Urdu': 98,
    'Isl':76,
    'programming':67
}

dic_series = pd.Series(marks , name = "Alisha's marks")
dic_series


# # Attributes of pandas

# # Size:
# 
# Ak Series ky andar  kitne items hai 
# Actually it tells the number of items
# 
# We can only see the size of dictionaries

# In[18]:


dic_series.size


# In[39]:


final.size


# # dtype:
# 
# it tells the datatype like int , float ,,,,,,,,,
# 
# 

# In[22]:


dic_series.dtype


# In[40]:


final.dtype


# # name

# In[24]:


dic_series.name


# # is_unique

# In[25]:


dic_series.is_unique


# In[26]:


pd.Series([1 ,1 , 2 , 4, 5 , 2 , 1]).is_unique


# # index
# 
# it return the index object

# In[28]:


dic_series.index


# In[35]:


scores = [12 , 16 , 18 , 90 , 56 , 23]

result=pd.Series(scores)
result


# In[33]:


result.index


# In[34]:


type(result.index)


# # values

# In[36]:


dic_series.values


# In[38]:


final.values


# # Series using real world data set
# 
# By default data converted into dataframe not Series.... So by using squeeze it converted into series explicitly
# 
# read_csv ------------> data ko read kr ky default dataframe mei store krta hai

# In[8]:


bolly_wood = pd.read_csv("D:/Data_science/data_sets/datasets-session-16/bollywood.csv" , index_col = 'movie').squeeze()




# In[9]:


bolly_wood


# In[10]:


subs = pd.read_csv("D:/Data_science/data_sets/datasets-session-16/subs.csv").squeeze()



# In[11]:


subs


# In[47]:


type(subs)


# In[12]:


kohli_ipl = pd.read_csv("D:/Data_science/data_sets/datasets-session-16/kohli_ipl.csv", index_col='match_no').squeeze()

print(kohli_ipl)


# # Pandas Method:

# # Head():
#     
#     shows the first 5 columns

# In[6]:


subs.head()


# In[7]:


subs.head(3)


# # tail():
# 
#        Last 5 columns

# In[8]:


subs.tail()


# In[9]:


subs.tail(20)


# # sample()
#     
#     randomly one row dekhate hai koi be ak 

# In[14]:


bolly_wood.sample()


# In[15]:


bolly_wood.sample(3)


# # value_counts:
#     
#     har item ka frequency batata hai wo value data mei kitne bar hai
#     
#     

# In[17]:


bolly_wood.value_counts()


#Given in dexcending order ky har actor ny kitne kitne movies ke hai us ka count bta dein ga


# # sort_values():
#     
#     Ascending order mei sort hoo jai ga

# In[19]:


kohli_ipl.sort_values()


# ################################################Also in decsending: ##########################################################

# In[20]:


kohli_ipl.sort_values(ascending = False)


# ########################################################fetch the top row################################################

# In[21]:


kohli_ipl.sort_values(ascending = False).head(1)


# In[22]:


kohli_ipl.sort_values(ascending = False).head(1).values


# In[25]:


kohli_ipl.sort_values(ascending = False).head(1).values[0]  #---------------------------> method chaining


# # Series Maths Method:

# # count() :
#     
#     number of items ko count krta hai in series bt don't count the missing values in case of size....It also counts the missing values

# In[7]:


kohli_ipl.count()      #it returns the number of rows


# # sum():

# In[8]:


subs.sum()


# # product():

# In[9]:


subs.product()


# In[10]:


subs


# # mean()
# 

# In[12]:


subs.mean()


# # mode()

# In[13]:


bolly_wood.mode()


# # median()

# In[14]:


kohli_ipl.median()


# # var()

# In[16]:


subs.var()


# # std()

# In[17]:


subs.std()


# # min():

# In[18]:


subs.min()


# # max():

# In[19]:


subs.max()


# # describe():

# In[22]:


kohli_ipl.describe()


# saray mathematical functions describe kr ky dy dy ga

#25%
#50%      it is percentile       means 25% inings mei 9 yeh 9 sy km score banaya hai
#75%


# # Series Indexing:

# # positive indexing:

# In[24]:


x = pd.Series([12 , 13 , 14 , 15 , 16 , 3 , 4 , 8 ,9])
x


# # negative indexing:
# 
# in case of index (integer) it is not working in negative indexing but in case of string(object) index it is working in negative indexing

# In[26]:


bolly_wood


# # Also fetch the data by integer and string index

# In[27]:


bolly_wood[0]


# In[32]:


bolly_wood['Hum Tumhare Hain Sanam']


# In[33]:


bolly_wood['Awara Paagal Deewana']


# # Slicing

# In[34]:


kohli_ipl[11 : 15]


# # Negative slicing

# In[35]:


kohli_ipl[-5 :]


# In[36]:


bolly_wood[-5:]


# In[37]:


bolly_wood[::2]


# # fancy indexing:

# In[38]:


bolly_wood[[1 , 3 , 4 , 5]]


# In[39]:


kohli_ipl[[1 , 6 , 7 , 3]]


# # indexing with labels------->

# In[40]:


bolly_wood


# In[42]:


bolly_wood[['Evening Shadows' , 'Hum Tumhare Hain Sanam' , 'Awara Paagal Deewana']]


# # Editing series:

# # using indexing:

# In[46]:


marks


# In[48]:


marks[3]=100
marks


# # Create new row in data

# In[50]:


marks['Science']=100
marks


# marks['Socialogy']----------------> it gives the error because firstly it is not present and cann't read it but in write it does

# # slicing

# In[57]:


marks


# In[59]:


marks[1:3]=[90 , 80]
marks


# # fancy indexing:

# In[61]:


marks[[1 , 3 , 5]]=[100 , 80 , 98]
marks


# # using index label:

# In[62]:


bolly_wood


# In[63]:


bolly_wood['Company (film)'] = 'Alia Butt'


# In[64]:


bolly_wood


# # Series with python functionalities

# # len

# In[65]:


len(subs)


# # type

# In[66]:


type(subs)


# # dir

# In[67]:


#It tells the attributes and methods

dir(subs)


# # sorted

# In[72]:


sorted(subs)     #stores output in the list


# # max

# In[70]:


max(subs)


# # min

# In[71]:


min(subs)


# # type conversion

# In[73]:


list(subs)


# In[74]:


dict(subs)


# # Membership operators:
# 
#     in
#     not in
#     etc

# In[77]:


bolly_wood


# In[78]:


'Battalion 609' in bolly_wood


# In[79]:


'Heer ranjha' in bolly_wood


# In[80]:


'Heer ranjha' not in bolly_wood


# # It only works in index if u want to work in values then use values

# In[81]:


bolly_wood


# In[82]:


'Alia Butt' in bolly_wood


# In[83]:


'Alia Butt' in bolly_wood.values


# # looping
# 
# It works on values...... if u want to work in index then use index

# In[84]:


for x in bolly_wood:    #-----------------------------> give the values
    print(x)


# In[85]:


for x in bolly_wood.index:
    print(x)


# # Arithmetic operators:

# In[86]:


marks


# In[87]:


#if u wanna check 100 mei sy kitny or nmb anay chahiya thy ky pora 100 bn jata


# In[89]:


100 - marks    #---------(best example of broadcasting ak scalar diya sb py apply hoo gya)


# In[90]:


100 + marks


# In[91]:


100 - marks


# In[92]:


100 * marks


# # Relational operator

# In[93]:


subs


# In[94]:


subs <=200


# # boolean indexing on Series:

# In[95]:


subs[subs <=200]


# In[96]:


subs == 0


# In[97]:


subs[subs == 0]


# In[98]:


kohli_ipl == 0


# In[100]:


kohli_ipl[kohli_ipl == 0].size


# In[101]:


subs >= 200


# In[102]:


subs[subs >= 200]


# In[103]:


subs[subs >= 200].size


# In[107]:


num_series = bolly_wood.value_counts()
num_series


# In[108]:


num_series >= 20


# In[112]:


num_series[num_series >= 20]


# In[113]:


num_series[num_series >= 20].index


# # Plots:

# In[114]:


import matplotlib.pyplot as plt


# In[117]:


plt.plot(marks)


# In[118]:


subs.plot()


# In[5]:


graph =bolly_wood.value_counts().head(20)


# In[6]:


graph.plot(kind = 'bar')


# In[7]:


graph.plot(kind = 'pie')


# # important functions

# # astype()

# In[13]:


kohli_ipl


# In[14]:


import sys

sys.getsizeof(kohli_ipl)


# In[18]:


km_size=kohli_ipl.astype('int16')


# In[19]:


sys.getsizeof(km_size)


# In[23]:


km_size1=kohli_ipl.astype('float16')
km_size1


# In[24]:


sys.getsizeof(km_size1)


# # between()

# In[29]:


kohli_ipl.between(14 , 100)          # 14 or 100 ky between score dekha dein ga


# In[30]:


kohli_ipl[kohli_ipl.between(14 , 100)]       #both are inclusive


# In[31]:


kohli_ipl[kohli_ipl.between(14 , 100)].size


# # Clip
# 
# 
# jo 100 sy km hai us ko 100 bna dein ga or jo 200 sy zyada hai us ko 200

# In[32]:


subs


# In[33]:


subs.clip(100 , 200)


# # drop_duplicates

# In[35]:


duplication_series = pd.Series([1 , 2 , 4 ,5 , 4 , 3 , 3 , 7 , 7 , 8 , 2 , 3 , 4 , 3])

duplication_series


# In[36]:


duplication_series.drop_duplicates()


# In[37]:


duplication_series = pd.Series([1 , 1, 1, 2 , 4 ,5 , 4 , 3 , 3 , 7 , 7 , 8 , 2 , 3 , 4 , 3])

duplication_series


# In[38]:


duplication_series.drop_duplicates(keep = 'last')


# In[39]:


duplication_series.drop_duplicates(keep = 'first')


# In[41]:


bolly_wood


# In[44]:


bolly_wood.drop_duplicates()


# # duplicated()
# 
# to check duplicated or not

# In[46]:


duplication_series.duplicated()


# In[47]:


duplication_series[duplication_series.duplicated()]


# In[48]:


duplication_series[duplication_series.duplicated()].size


# In[50]:


duplication_series.duplicated().sum()


# # isnull

# In[52]:


temp = pd.Series([12 , 16 , 19 , np.nan , 56 , np.nan , 78 , 12 , 12 , np.nan])
temp


# In[53]:


temp.size  #-----------------count all data


# In[56]:


temp.count()  #-----------------count only data which is not missed


# In[57]:


kohli_ipl


# In[62]:


kohli_ipl.isnull().sum()


# In[63]:


temp.isnull().sum()


# # dropna    ---------> drop missing values

# In[64]:


temp.dropna()


# # fillna ------------> fill missing values

# In[66]:


temp.fillna(1)


# In[68]:


temp.fillna(temp.mean()).astype('int16')


# # isin

# In[70]:


(kohli_ipl == 49) | (kohli_ipl == 90)


# In[71]:


kohli_ipl[(kohli_ipl == 49) | (kohli_ipl == 90)]


# but when we find more values then we use isin

# In[73]:


kohli_ipl.isin([49 , 90 , 100 , 120])


# In[74]:


kohli_ipl[kohli_ipl.isin([49 , 90 , 100 , 120])]


# # apply()  -----------> we can make our own function

# In[75]:


bolly_wood


# In[76]:


bolly_wood.apply(lambda x : x.split())


# In[77]:


bolly_wood.apply(lambda x : x.split()[0])


# In[78]:


bolly_wood.apply(lambda x : x.split()[0].upper())


# In[79]:


subs


# In[85]:


average=subs.mean()


# In[89]:


subs.apply(lambda x : 'good day' if x > average else 'bad day')
     


# # Copy

# In[90]:


kohli_ipl


# In[94]:


new = kohli_ipl.head(5)


# In[95]:


new[5] = 0


# In[96]:


new


# # but we load the original data it also changes which is wrong

# In[97]:


kohli_ipl


# # head yeh tail krty hai tu data ka preview milta hai us ke copy ni milte agr tail yeh head mei changes karein gy tu reflect back kr jai ga original data mei

# # soo use copy.................

# In[98]:


new = kohli_ipl.head().copy()


# In[99]:


new


# In[100]:


new[3] = 98


# In[101]:


new


# In[103]:


kohli_ipl                    #not changed


# In[ ]:




