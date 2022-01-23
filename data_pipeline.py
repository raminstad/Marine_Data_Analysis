#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import warnings
from functools import partial, reduce
import regex as re
warnings.filterwarnings('ignore')
path='/Users/raminstad/Downloads/Tools1/Final/acre_marine_data/Marine data'


# In[2]:


files = [f for f in listdir(path) if isfile(join(path, f))]
files.remove('.DS_Store')
files.remove('~$ACEH, INDONESIA - NOVEMBER 1874 - JULY 1875.xlsx')
files.remove('MACAO HURRICANE(5-6 AUGUST 1835).xls')


# In[3]:


one=[]
two=[]
three=[]
four=[]
five=[]

for i in files:
    
    xlsx=pd.ExcelFile(f'{path}/{str(i)}')
    sheets=xlsx.sheet_names
    if len(sheets)==1:
        one.append(i)
    
    elif len(sheets)==2:
        two.append([i,sheets])
        
    elif len(sheets)==3:
        three.append([i,sheets])
    
    elif len(sheets)==4:
        four.append([i,sheets])

    elif len(sheets)==5:
        five.append([i,sheets])
        
    
dfOne=[]
for i in range(len(one)):    
    dfOne.append(pd.read_excel(f'{path}/{one[i]}'))


dfTwo=[]
for i in range(len(two)):    
    dfTwo.append(pd.read_excel(f'{path}/{two[i][0]}',sheet_name=two[i][1][0]))
    dfTwo.append(pd.read_excel(f'{path}/{two[i][0]}',sheet_name=two[i][1][1]))    


dfThree=[]
for i in range(len(three)):    
    dfThree.append(pd.read_excel(f'{path}/{three[i][0]}',sheet_name=three[i][1][0]))
    dfThree.append(pd.read_excel(f'{path}/{three[i][0]}',sheet_name=three[i][1][1]))
    dfThree.append(pd.read_excel(f'{path}/{three[i][0]}',sheet_name=three[i][1][2]))
    


dfFour=[]
for i in range(len(four)):    
    dfFour.append(pd.read_excel(f'{path}/{four[i][0]}',sheet_name=four[i][1][0]))
    dfFour.append(pd.read_excel(f'{path}/{four[i][0]}',sheet_name=four[i][1][1]))
    dfFour.append(pd.read_excel(f'{path}/{four[i][0]}',sheet_name=four[i][1][2]))
    dfFour.append(pd.read_excel(f'{path}/{four[i][0]}',sheet_name=four[i][1][3]))
    

dfFive=[]
for i in range(len(five)):    
    dfFive.append(pd.read_excel(f'{path}/{five[i][0]}',sheet_name=five[i][1][0]))
    dfFive.append(pd.read_excel(f'{path}/{five[i][0]}',sheet_name=five[i][1][1]))
    dfFive.append(pd.read_excel(f'{path}/{five[i][0]}',sheet_name=five[i][1][2]))
    dfFive.append(pd.read_excel(f'{path}/{five[i][0]}',sheet_name=five[i][1][3]))
    dfFive.append(pd.read_excel(f'{path}/{five[i][0]}',sheet_name=five[i][1][4]))
    


# In[4]:


len(dfOne)+len(dfTwo)+len(dfThree)+len(dfFour)+len(dfFive)


# In[5]:


def NoZero(lsts):
    lst=[]
    for i in lsts:
        if len(i)>0:
            lst.append(i)
    return lst     


# In[6]:


one=NoZero(dfOne)
two=NoZero(dfTwo)
three=NoZero(dfThree)
four=NoZero(dfFour)
five=NoZero(dfFive)


# In[7]:


len(one)+len(two)+len(three)+len(four)+len(five)


# In[8]:


for i in range(len(one)):
    one[i]=one[i].rename(columns=one[i].iloc[2]).drop(one[i].index[2])
    


# In[9]:


for i in range(len(two)):
    two[i]=two[i].rename(columns=two[i].iloc[2]).drop(two[i].index[2])
    


# In[10]:


for i in range(len(three)):
    three[i]=three[i].rename(columns=three[i].iloc[2]).drop(three[i].index[2])
    


# In[11]:


for i in range(len(four)):
    four[i]=four[i].rename(columns=four[i].iloc[2]).drop(four[i].index[2])


# In[12]:


for i in range(len(five)):
    five[i]=five[i].rename(columns=five[i].iloc[2]).drop(five[i].index[2])


# In[13]:


two[0].reset_index(drop=True)


# In[14]:


two[0],two[0].columns=two[0][4:],two[0].iloc[3]


# In[15]:


two[16].reset_index(drop=True)


# In[16]:


two[16],two[16].columns=two[16][3:],two[16].iloc[2]


# In[17]:


def lstshrink(lsts):
    lst=[]
    for i in lsts:
        if len(i)>26:
            lst.append(i)
    return lst


# In[18]:


one=lstshrink(one)
two=lstshrink(two)
three=lstshrink(three)
four=lstshrink(four)
five=lstshrink(five)


# In[19]:


comp=one+two+three+four+five


# In[20]:


for i in range(len(comp)):
    comp[i].reset_index(inplace=True, drop=True)


# In[21]:


def remove_dup_col(frame):
    names = set()
    icols = list()
    for icol, name in enumerate(frame.columns):
        if name not in names:
            names.add(name)
            icols.append(icol)
    frame=frame.iloc[:, icols]
    return frame


# In[22]:


for i in range(len(comp)):
    comp[i]=remove_dup_col(comp[i])


# In[23]:


def uniq_cols(frame):
    t=[]
    for i in range(len(frame)):
        t.append(frame[i].columns)
    r=set()   
    for j in t:
        for k in j:
            r.add(k)

    l=[]
    cols=[]
    for g in r:
        l.append(g)

    for h in l:
        if type(h)==str:
            cols.append(h)
    return cols
        


# In[25]:


"""
By calling this cell everytime you modify a column the variable barometer will be updated
and you can see which columns are left to be modified
"""

column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column)) 


# In[26]:


for h in range(len(comp)):
    comp[h].dropna(axis=1,how='all',inplace=True)


# In[31]:


for df in range(len(comp)):
    if 'BAROMETER(mm)' in comp[df].columns:
        comp[df]['BAROMETER']= comp[df]['BAROMETER(mm)'].apply(lambda x: x/25.4)
        comp[df].drop('BAROMETER(mm)',axis=1, inplace=True)


# In[32]:


b=['BAROMETER','BAROMETER(INCHES)']
for df in range(len(comp)):
    if 'BAROMETER(MM)' and 'BAROMETER(INCHES)' in comp[df].columns:
        comp[df]['BAROMETER']= comp[df]['BAROMETER(MM)'].apply(lambda x: x/25.4)
        comp[df].drop('BAROMETER(MM)',axis=1, inplace=True)
        comp[df]['BAROMETER'] = comp[df][b].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
        comp[df]['BAROMETER'] = comp[df]['BAROMETER'].apply(lambda x:x.split('nan'))
        comp[df]['BAROMETER'] = comp[df]['BAROMETER'].apply(lambda x:x[0] if len (x[0])>0 else x[-1])
        comp[df]['BAROMETER'] = comp[df]['BAROMETER'].apply(lambda x:x.strip(','))
        comp[df].drop('BAROMETER(INCHES)',axis=1, inplace=True)


# In[33]:


for df in range(len(comp)):
    if 'BAROMETER (mm)' in comp[df].columns:
        comp[df]['BAROMETER']= comp[df]['BAROMETER (mm)'].apply(lambda x: x/25.4)
        comp[df].drop('BAROMETER (mm)',axis=1, inplace=True)


# In[34]:


comp[87].drop('BAROMETER (inches)',axis=1, inplace=True)


# In[35]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column)) 


# In[36]:


for df in range(len(comp)):
    if 'BAR' in comp[df].columns:
        comp[df].rename(columns={'BAR': 'BAROMETER'}, inplace=True)
        
    elif 'BAR.' in comp[df].columns:
        comp[df].rename(columns={'BAR.': 'BAROMETER'}, inplace=True)
        
        
    elif 'BAR. (PARIS LINES)' in comp[df].columns:
        comp[df].rename(columns={'BAR. (PARIS LINES)': 'BAROMETER'}, inplace=True)
        
        
    elif 'BAROMETER ' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER ': 'BAROMETER'}, inplace=True)
        
        
    elif 'BAROMETER (INCHES)' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER (INCHES)': 'BAROMETER'}, inplace=True)
        
    
    elif 'BAROMETER (UNCORRECTED)' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER (UNCORRECTED)': 'BAROMETER'}, inplace=True)
        
        


# In[37]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column)) 


# In[38]:


for df in range(len(comp)):
    if 'BAROMETER (INCHES) 9h' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER (INCHES) 9h': 'BAROMETER'}, inplace=True)
        comp[df].drop('BAROMETER (INCHES) 15h',axis=1, inplace=True)


# In[39]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column)) 


# In[40]:


for df in range(len(comp)):
    if 'BAROMETER 10 A.M.' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER 10 A.M.': 'BAROMETER'}, inplace=True)
        comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: x/25.4)
        comp[df].drop(' BAROMETER 4 P.M.',axis=1, inplace=True)


# In[41]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column))


# In[42]:


for df in range(len(comp)):
    if 'BAROMETER 10h' and 'BAROMETER 22h' in comp[df].columns:
        if 'BAROMETER 16h' not in comp[df].columns:
            comp[df]['BAROMETER']=comp[df][['BAROMETER 10h','BAROMETER 22h']].mean(axis=1)
            comp[df].drop('BAROMETER 10h',axis=1, inplace=True)
            comp[df].drop('BAROMETER 22h',axis=1, inplace=True)
        else:
            comp[df]['BAROMETER']=comp[df][['BAROMETER 10h','BAROMETER 22h','BAROMETER 16h']].mean(axis=1)
            comp[df].drop('BAROMETER 10h',axis=1, inplace=True)
            comp[df].drop('BAROMETER 22h',axis=1, inplace=True)
            comp[df].drop('BAROMETER 16h',axis=1, inplace=True)


# In[43]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column))


# In[45]:


for df in range(len(comp)):
    if 'BAROMETER 9 A.M.' in comp[df].columns:
        comp[df].drop('BAROMETER 9 A.M.',axis=1, inplace=True)
        comp[df].drop('BAROMETER 3 P.M.',axis=1, inplace=True)
        


# In[46]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column))


# In[47]:


for df in range(len(comp)):
    if 'BAROMETER AT:' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER AT:': 'BAROMETER'}, inplace=True)


# In[48]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column))


# In[49]:


for df in range(len(comp)):
    if 'BAROMETER CORR.' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER CORR.': 'BAROMETER'}, inplace=True)
    
    elif 'BAROMETER RED. 0° C' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER RED. 0° C': 'BAROMETER'}, inplace=True)
        comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: x/25.4)
    
    elif 'BAROMETER RED. TO 0°C' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER RED. TO 0°C': 'BAROMETER'}, inplace=True)
        comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: None if type(x)!= float else x)
        comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: x/25.4)
    
    elif 'BAROMETER REDUCED' in comp[df].columns:
        if 'BAROMETER(UNCORRECTED)' not in comp[df].columns:
            comp[df].drop('BAROMETER REDUCED',axis=1, inplace=True)
        
        elif 'BAROMETER(UNCORRECTED)' in comp[df].columns:
            comp[df].rename(columns={'BAROMETER(UNCORRECTED)': 'BAROMETER'}, inplace=True)
            comp[df].drop('BAROMETER REDUCED',axis=1, inplace=True)
    
    
    
    


# In[55]:


column=uniq_cols(comp)
column.sort()
r = re.compile("ANEROID*")
barometer = list(filter(r.match, column))


# In[62]:


for df in range(len(comp)):
    if 'ANEROID BAROMETER' in comp[df].columns:
        if df==26:
            comp[df].rename(columns={'ANEROID BAROMETER': 'BAROMETER'}, inplace=True)
            comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: None if x>200 else x)
        elif df==90:
            comp[df].rename(columns={'ANEROID BAROMETER': 'BAROMETER'}, inplace=True)
            comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: None if type(x)!=float else x)


# In[65]:


column=uniq_cols(comp)
column.sort()
r = re.compile("ANEROID*")
barometer = list(filter(r.match, column))


# In[68]:


for df in range(len(comp)):
    if 'ANEROID BAROMETER A' in comp[df].columns:
        comp[df].drop('SEA BAROMETER INCHES',axis=1, inplace=True)
        comp[df].drop('SEA BAROMETER MM',axis=1, inplace=True)
        comp[df].drop('SEA BAROMETER B',axis=1, inplace=True)
        comp[df].drop('SEMPIESOMETER INCHES',axis=1, inplace=True)
        comp[df].drop('SEMPIESOMETER MM',axis=1, inplace=True)
        comp[df].rename(columns={'ANEROID BAROMETER A': 'BAROMETER'}, inplace=True)
        comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: x/25.4)


# In[70]:


column=uniq_cols(comp)
column.sort()
r = re.compile("ANEROID*")
barometer = list(filter(r.match, column))


# In[75]:


for df in range(len(comp)):
    if 'ANEROID BAROMETER I' in comp[df].columns:
        comp[df].drop('ANEROID BAROMETER I',axis=1, inplace=True)
        comp[df].drop('ANEROID BAROMETER II',axis=1, inplace=True)


# In[76]:


column=uniq_cols(comp)
column.sort()
r = re.compile("ANEROID*")
barometer = list(filter(r.match, column))


# In[80]:


for df in range(len(comp)):
    if "SHIP'S BAROMETER" in comp[df].columns:
        comp[df].drop("SHIP'S BAROMETER",axis=1, inplace=True)


# In[81]:


for df in range(len(comp)):
    if "BAROMETER"  not in comp[df].columns:
        comp[df]["BAROMETER"]=None




