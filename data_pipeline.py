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
        


# # BAROMETER

# In[24]:


"""
By calling this cell everytime you modify a column the variable barometer will be updated
and you can see which columns are left to be modified
"""

column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column)) 


# In[25]:


barometer


# In[26]:


for h in range(len(comp)):
    comp[h].dropna(axis=1,how='all',inplace=True)


# In[27]:


for df in range(len(comp)):
    if 'BAROMETER(mm)' in comp[df].columns:
        comp[df]['BAROMETER']= comp[df]['BAROMETER(mm)'].apply(lambda x: x/25.4)
        comp[df].drop('BAROMETER(mm)',axis=1, inplace=True)


# In[28]:


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


# In[29]:


for df in range(len(comp)):
    if 'BAROMETER (mm)' in comp[df].columns:
        comp[df]['BAROMETER']= comp[df]['BAROMETER (mm)'].apply(lambda x: x/25.4)
        comp[df].drop('BAROMETER (mm)',axis=1, inplace=True)


# In[30]:


comp[87].drop('BAROMETER (inches)',axis=1, inplace=True)


# In[31]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column)) 


# In[32]:


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
        
        


# In[33]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column)) 


# In[34]:


for df in range(len(comp)):
    if 'BAROMETER (INCHES) 9h' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER (INCHES) 9h': 'BAROMETER'}, inplace=True)
        comp[df].drop('BAROMETER (INCHES) 15h',axis=1, inplace=True)


# In[35]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column)) 


# In[36]:


for df in range(len(comp)):
    if 'BAROMETER 10 A.M.' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER 10 A.M.': 'BAROMETER'}, inplace=True)
        comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: x/25.4)
        comp[df].drop(' BAROMETER 4 P.M.',axis=1, inplace=True)


# In[37]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column))


# In[38]:


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


# In[39]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column))


# In[40]:


for df in range(len(comp)):
    if 'BAROMETER 9 A.M.' in comp[df].columns:
        comp[df].drop('BAROMETER 9 A.M.',axis=1, inplace=True)
        comp[df].drop('BAROMETER 3 P.M.',axis=1, inplace=True)
        


# In[41]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column))


# In[42]:


for df in range(len(comp)):
    if 'BAROMETER AT:' in comp[df].columns:
        comp[df].rename(columns={'BAROMETER AT:': 'BAROMETER'}, inplace=True)


# In[43]:


column=uniq_cols(comp)
column.sort()
r = re.compile("BAR*")
barometer = list(filter(r.match, column))


# In[44]:


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
    
    
    
    


# In[45]:


column=uniq_cols(comp)
column.sort()
r = re.compile("ANEROID*")
barometer = list(filter(r.match, column))


# In[46]:


for df in range(len(comp)):
    if 'ANEROID BAROMETER' in comp[df].columns:
        if df==26:
            comp[df].rename(columns={'ANEROID BAROMETER': 'BAROMETER'}, inplace=True)
            comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: None if x>200 else x)
        elif df==90:
            comp[df].rename(columns={'ANEROID BAROMETER': 'BAROMETER'}, inplace=True)
            comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: None if type(x)!=float else x)


# In[47]:


column=uniq_cols(comp)
column.sort()
r = re.compile("ANEROID*")
barometer = list(filter(r.match, column))


# In[48]:


for df in range(len(comp)):
    if 'ANEROID BAROMETER A' in comp[df].columns:
        comp[df].drop('SEA BAROMETER INCHES',axis=1, inplace=True)
        comp[df].drop('SEA BAROMETER MM',axis=1, inplace=True)
        comp[df].drop('SEA BAROMETER B',axis=1, inplace=True)
        comp[df].drop('SEMPIESOMETER INCHES',axis=1, inplace=True)
        comp[df].drop('SEMPIESOMETER MM',axis=1, inplace=True)
        comp[df].rename(columns={'ANEROID BAROMETER A': 'BAROMETER'}, inplace=True)
        comp[df]['BAROMETER']=comp[df]['BAROMETER'].apply(lambda x: x/25.4)


# In[49]:


column=uniq_cols(comp)
column.sort()
r = re.compile("ANEROID*")
barometer = list(filter(r.match, column))


# In[50]:


for df in range(len(comp)):
    if 'ANEROID BAROMETER I' in comp[df].columns:
        comp[df].drop('ANEROID BAROMETER I',axis=1, inplace=True)
        comp[df].drop('ANEROID BAROMETER II',axis=1, inplace=True)


# In[51]:


column=uniq_cols(comp)
column.sort()
r = re.compile("ANEROID*")
barometer = list(filter(r.match, column))


# In[52]:


for df in range(len(comp)):
    if "SHIP'S BAROMETER" in comp[df].columns:
        comp[df].drop("SHIP'S BAROMETER",axis=1, inplace=True)


# In[53]:


for df in range(len(comp)):
    if "MEAN BAROMETER" in comp[df].columns:
        comp[df].drop("MEAN BAROMETER",axis=1, inplace=True)
        


# In[54]:


for df in range(len(comp)):
    if "THERMOMETER of Barometer" in comp[df].columns:
        comp[df].drop("THERMOMETER of Barometer",axis=1, inplace=True)


# In[55]:


for df in range(len(comp)):
    if "MERCURIAL BAROMETER" in comp[df].columns:
        comp[df].rename(columns={'MERCURIAL BAROMETER': 'BAROMETER'}, inplace=True)


# In[56]:


for df in range(len(comp)):
    if "SEMPIESOMETER" in comp[df].columns:
        comp[df].rename(columns={'SEMPIESOMETER': 'BAROMETER'}, inplace=True)


# In[57]:


for df in range(len(comp)):
    if "SYMPESIOMETER" in comp[df].columns:
        comp[df].drop("SYMPESIOMETER",axis=1, inplace=True)
        


# In[58]:


for df in range(len(comp)):
    if "SYMPIESOMETER" in comp[df].columns:
        if df==15:
            comp[df].drop("SYMPIESOMETER",axis=1, inplace=True)
        else:
            comp[df].rename(columns={'SYMPIESOMETER': 'BAROMETER'}, inplace=True)


# In[59]:


for df in range(len(comp)):
    if "SYMPIESOMETER PRESSURE" in comp[df].columns:
        comp[df].drop("SYMPIESOMETER PRESSURE",axis=1, inplace=True)


# In[60]:


comp[35].rename(columns={'HOUR': 'BAROMETER'}, inplace=True)


# In[61]:


comp[14].rename(columns={'6 A.M.': 'BAROMETER'}, inplace=True)
comp[14].drop('12 P.M.',axis=1, inplace=True)
comp[14].drop('5 P.M.',axis=1, inplace=True)


# In[62]:


for df in range(len(comp)):
    if "BAROMETER"  not in comp[df].columns:
        comp[df]["BAROMETER"]=np.NaN


# In[63]:


# dropping any str formats in the barometer column
for i in range (len(comp)):
    comp[i]['BAROMETER']=comp[i]['BAROMETER'].apply(lambda x: np.NaN if type(x)==str else x)


# In[64]:


# checking every dataframe and if their barometers are in mm converting it to inches
for i in range (len(comp)):
    comp[i]['BAROMETER']=comp[i]['BAROMETER'].apply(lambda x: x/25.4 if np.mean(comp[i]['BAROMETER'].value_counts().index)>100 else x)


# # LATITUDE AND LONGITUDE

# In[65]:


column=uniq_cols(comp)
column.sort()


# In[66]:


long=[]
lat=[]

for df in range(len(comp)):
    if "LATITUDE" in comp[df].columns or "LATITUDE DR" in comp[df].columns :
        lat.append(df)
        
    if "LONGITUDE" in comp[df].columns or "LONGITUDE DR" in comp[df].columns :
        long.append(df)


# In[67]:


np.mean(long)


# In[68]:


np.mean(lat)


# In[69]:


for i in lat:
    if i not in long:
        print(i)


# In[70]:


# since the latitude for comp[23] is all nan we should add longitude to this dataframe 
#and set it to nan as well
comp[23]['LONGITUDE']=np.NaN
comp[23]['N/S']=np.NaN
comp[23]['E/W']=np.NAN


# In[71]:


nolat=[]
for df in range(len(comp)):
    if "LATITUDE" not in comp[df].columns:
        nolat.append(df)


# In[72]:


no_lat=[]
for df in nolat:
    no_lat.append(comp[df])


# In[73]:


for df in lat:
    if 'LATITUDE' in comp[df]:
        comp[df]['LATITUDE']=comp[df]['LATITUDE'].apply(lambda x: np.NaN if type(x)==str else x)
        comp[df]['LONGITUDE']=comp[df]['LONGITUDE'].apply(lambda x: np.NaN if type(x)==str else x)
    
    else:
        comp[df]['LATITUDE DR']=comp[df]['LATITUDE DR'].apply(lambda x: np.NaN if type(x)==str else x)
        comp[df]['LONGITUDE DR']=comp[df]['LONGITUDE DR'].apply(lambda x: np.NaN if type(x)==str else x)


# In[74]:


for df in lat:
    if 'LATITUDE' in comp[df]:
        comp[df]['LATITUDE']=comp[df].apply(lambda x:-x['LATITUDE'] if x['N/S']=='S' else x['LATITUDE'],axis=1)
        comp[df]['LONGITUDE']=comp[df].apply(lambda x:-x['LONGITUDE'] if x['E/W']=='W' else x['LONGITUDE'],axis=1)
    else:
        comp[df]['LATITUDE DR']=comp[df].apply(lambda x:-x['LATITUDE DR'] if x['N/S']=='S' else x['LATITUDE DR'],axis=1)
        comp[df]['LONGITUDE DR']=comp[df].apply(lambda x:-x['LONGITUDE DR'] if x['E/W']=='W' else x['LONGITUDE DR'],axis=1)
        


# In[75]:


for df in range (len (comp)):
    if 'LATITUDES' in comp[df].columns:
        comp[df].drop('LATITUDES',axis=1, inplace=True)


# In[76]:


comp[85].rename(columns={'LATITUDE DR': 'LATITUDE'}, inplace=True)
comp[85].rename(columns={'LONGITUDE DR': 'LONGITUDE'}, inplace=True)


# In[77]:


for df in range(len(comp)):
    if "LATITUDE"  not in comp[df].columns:
        comp[df]["LATITUDE"]=np.NaN
        comp[df]["LONGITUDE"]=np.NaN


# # Temperature adjustment

# In[78]:


# figuered out comp[3] and comp[8] are the same so I remove one of them at the end of cleaning


# In[79]:


def temp_uniq(comp):
    column=uniq_cols(comp)
    
    t = re.compile("THER*")
    ther_list = set(filter(t.search,column))
    ther_list

    te = re.compile("TEMP*")
    temp_list = set(filter(te.search,column))
    temp_list
    return set.union(temp_list,ther_list)


# In[80]:


for df in range (len(comp)):
    if 'AIR TEMP' in comp[df]:
        if df==2 or df==7:
            comp[df].drop('WATER TEMP',axis=1, inplace=True) 
            comp[df].rename(columns={'AIR TEMP': 'THERMOMETER'}, inplace=True)
        
        elif df==26:
            comp[df].rename(columns={'AIR TEMP': 'THERMOMETER'}, inplace=True)
            comp[df].drop('SEA',axis=1, inplace=True) 
    
        elif df==59:
            comp[df].drop('AIR TEMP',axis=1, inplace=True) 
            
        elif df==76:
            comp[df].rename(columns={'ATT.THERM': 'THERMOMETER'}, inplace=True)
            comp[df].drop('AIR TEMP',axis=1, inplace=True)
            comp[df].drop('SEA TEMP',axis=1, inplace=True)

        
        elif df==88:
            comp[df].rename(columns={'THERM.': 'THERMOMETER'}, inplace=True)
            comp[df].drop('ATT.THERM',axis=1, inplace=True)
            comp[df].drop('AIR TEMP',axis=1, inplace=True)
            comp[df].drop('SEA TEMP',axis=1, inplace=True)


# In[81]:


for df in range (len(comp)):
    if 'AIR TEMPERATURE' in comp[df]:
        if df==38:
            comp[df].rename(columns={'AIR TEMPERATURE': 'THERMOMETER'}, inplace=True)
            comp[df].drop('WATER TEMPERATURE',axis=1, inplace=True)
            comp[df].drop('ATTACHED THERMOMETER',axis=1, inplace=True)
            
        elif df==67:
            comp[df].rename(columns={'AIR TEMPERATURE': 'THERMOMETER'}, inplace=True)
        
        elif df==15:
            comp[df].rename(columns={'AIR TEMPERATURE': 'THERMOMETER'}, inplace=True)
            comp[df].drop('SEA TEMP',axis=1, inplace=True)
        
        else:
            comp[df].rename(columns={'AIR TEMPERATURE': 'THERMOMETER'}, inplace=True)
            comp[df].drop('SEA TEMPERATURE',axis=1, inplace=True)


# In[82]:


for df in range (len(comp)):
    if 'AIR TEMPERATURE AT:' in comp[df]:
        comp[df].rename(columns={'AIR TEMPERATURE AT:': 'THERMOMETER'}, inplace=True)
        comp[df].drop('SEA TEMPERATURE AT:',axis=1, inplace=True)


# In[83]:


for df in range (len(comp)):
    if 'ATT THERM' in comp[df]:
        comp[df].rename(columns={'ATT THERM': 'THERMOMETER'}, inplace=True)


# In[84]:


for df in range (len(comp)):
    if 'ATT.THERM' in comp[df]:
        comp[df].rename(columns={'ATT.THERM': 'THERMOMETER'}, inplace=True)
        comp[df].drop('TEMP.CAP.',axis=1, inplace=True)
        comp[df].drop('TEMP.SEA',axis=1, inplace=True)
        comp[df].drop('TEMP.AIR',axis=1, inplace=True)
        comp[df].drop('TEMP.WHEEL',axis=1, inplace=True)


# In[85]:


for df in range (len(comp)):
    if 'DRY AND WET THERMOMETERS, ASPIRATED' in comp[df]:
        comp[df].rename(columns={np.nan:'YEAR'},inplace=True)
        comp[df].rename(columns={'DRY AND WET THERMOMETERS, ASPIRATED':'THERMOMETER'},inplace=True)
        comp[df].drop('DRY AND WET THERMOMETERS, FREE',axis=1, inplace=True)


# In[86]:


for df in range (len(comp)):
    if 'EXTERNAL THERMOMETERS' in comp[df]:
        comp[df].rename(columns={'EXTERNAL THERMOMETERS':'THERMOMETER'},inplace=True)
       


# In[87]:


for df in range (len(comp)):
    if 'MEAN TEMPERATURE' in comp[df]:
        comp[df].rename(columns={'MEAN TEMPERATURE':'THERMOMETER'},inplace=True)
        comp[df].drop('TEMPERATURE 1',axis=1, inplace=True)
        comp[df].drop('TEMPERATURE 2',axis=1, inplace=True)


# In[88]:


for df in range (len(comp)):
    if 'SEA TEMP(F)' in comp[df]:
        comp[df].rename(columns={'SEA TEMP(F)':'THERMOMETER'},inplace=True)


# In[89]:


for df in range (len(comp)):
    if 'SEA TEMP.' in comp[df]:
        comp[df].drop('THERMOMETER',axis=1, inplace=True)
        comp[df].rename(columns={'SEA TEMP.':'THERMOMETER'},inplace=True)


# In[90]:


for df in range (len(comp)):
    if 'SEA TEMPERATURE' in comp[df]:
        comp[df].rename(columns={'SEA TEMPERATURE':'THERMOMETER'},inplace=True)


# In[91]:


for df in range (len(comp)):
    if 'SYMPIESOMETER TEMPERATURE' in comp[df]:
        comp[df].rename(columns={'TEMPERATURE AIR':'THERMOMETER'},inplace=True)
        comp[df].drop('TEMPERATURE SEA',axis=1, inplace=True)
        comp[df].drop('SYMPIESOMETER TEMPERATURE',axis=1, inplace=True)


# In[92]:


for df in range (len(comp)):
    if 'TEMPERATURE (C)' in comp[df]:
        comp[df].rename(columns={'TEMPERATURE (C)':'THERMOMETER'},inplace=True)


# In[93]:


for df in range (len(comp)):
    if 'TEMPERATURE (F)' in comp[df]:
        comp[df].rename(columns={'TEMPERATURE ©':'THERMOMETER'},inplace=True)
        comp[df].drop('TEMPERATURE (F)',axis=1, inplace=True)


# In[94]:


for df in range (len(comp)):
    if 'TEMPERATURE AIR' in comp[df]:
        comp[df].rename(columns={'TEMPERATURE AIR':'THERMOMETER'},inplace=True)
        comp[df].drop('TEMPERATURE SEA',axis=1, inplace=True)
           


# In[95]:


for df in range (len(comp)):
    if 'TEMPERATURE IN SHADE 8h' in comp[df]:
        comp[df].rename(columns={'TEMPERATURE IN SHADE 8h':'THERMOMETER'},inplace=True)
        comp[df].drop('TEMPERATURE IN SHADE Sunset',axis=1, inplace=True)


# In[96]:


for df in range (len(comp)):
    if 'TEMPERATURE MAX' in comp[df]:
        comp[df]['THERMOMETER']=comp[df].apply(lambda x: (x['TEMPERATURE MAX']+x['TEMPERATURE MIN'])/2,axis=1)
        comp[df].drop('TEMPERATURE MAX',axis=1, inplace=True)
        comp[df].drop('TEMPERATURE MIN',axis=1, inplace=True)
        comp[df].drop('TEMPERATURE SEA',axis=1, inplace=True)


# In[97]:


for df in range (len(comp)):
    if 'TEMPERATURES' in comp[df]:
        comp[df].rename(columns={'TEMPERATURES':'THERMOMETER'},inplace=True)


# In[98]:


for df in range (len(comp)):
    if 'THERM' in comp[df]:
        comp[df].rename(columns={'THERM':'THERMOMETER'},inplace=True)

        


# In[99]:


for df in range (len(comp)):
    if 'THERMOMETER  (IN SHADE)' in comp[df]:
        comp[df].rename(columns={'THERMOMETER  (IN SHADE)':'THERMOMETER'},inplace=True)


# In[100]:


for df in range (len(comp)):
    if 'THERMOMETER ( C )' in comp[df]:
        comp[df].rename(columns={'THERMOMETER ( C )':'THERMOMETER'},inplace=True)


# In[101]:


for df in range (len(comp)):
    if 'THERMOMETER (C)' in comp[df]:
        comp[df].columns.values[12]='THERMOMETER'
        comp[df].rename(columns={'THERMOMETER (C)':'WASTE'},inplace=True)        


# In[102]:


comp[5]=comp[5][['YEAR','MONTH','DAY','BAROMETER','THERMOMETER','LATITUDE','LONGITUDE']]


# In[103]:


for df in range (len(comp)):
    if 'THERMOMETER (F)' in comp[df]:
        if df==85:
            comp[df].rename(columns={'THERMOMETER (F)':'THERMOMETER'},inplace=True)
            comp[df].drop('THERMOMETER ON DECK IN SHADE',axis=1, inplace=True)
            
        else:
            comp[df].rename(columns={'THERMOMETER (F)':'THERMOMETER'},inplace=True)


# In[104]:


for df in range (len(comp)):
    if 'THERMOMETER (F) MAX 15h' in comp[df]:
        comp[df]['THERMOMETER']=comp[df].apply(lambda x: (x['THERMOMETER (F) MAX 9h']+x['THERMOMETER (F) MAX 15h']+x['THERMOMETER (F) MIN 9h'])/3,axis=1)
        comp[df].drop('THERMOMETER (F) MAX 15h',axis=1, inplace=True)
        comp[df].drop('THERMOMETER (F) MAX 9h',axis=1, inplace=True)
        comp[df].drop('THERMOMETER (F) MIN 9h',axis=1, inplace=True)


# In[105]:


for df in range (len(comp)):
    if 'THERMOMETER (IN SHADE)' in comp[df]:
        comp[df].rename(columns={'THERMOMETER (IN SHADE)':'THERMOMETER'},inplace=True)


# In[106]:


for df in range (len(comp)):
    if 'THERMOMETER (UNDER COVER) ATTACHED ' in comp[df]:
        comp[df]['THERMOMETER']=comp[df].apply(lambda x: (x['THERMOMETER (UNDER COVER) ATTACHED ']+x['THERMOMETER (UNDER COVER) DETACHED'])/2,axis=1)
        comp[df].drop('THERMOMETER (UNDER COVER) ATTACHED ',axis=1, inplace=True)
        comp[df].drop('THERMOMETER (UNDER COVER) DETACHED',axis=1, inplace=True)


# In[107]:


for df in range (len(comp)):
    if 'THERMOMETER (in shade)' in comp[df]:
        comp[df].rename(columns={'THERMOMETER (in shade)':'THERMOMETER'},inplace=True)


# In[108]:


for df in range (len(comp)):
    if 'THERMOMETER 10h' in comp[df]:
        comp[df]['THERMOMETER']=comp[df].apply(lambda x: (x['THERMOMETER 10h']+x['THERMOMETER 22h'])/2,axis=1)
        comp[df].drop('THERMOMETER 10h',axis=1, inplace=True)
        comp[df].drop('THERMOMETER 22h',axis=1, inplace=True)
        


# In[109]:


for df in range (len(comp)):
    if 'THERMOMETER 2 P.M.' in comp[df]:
        comp[df].rename(columns={'THERMOMETER DECK':'THERMOMETER'},inplace=True)
        comp[df].drop('THERMOMETER 6 A.M.',axis=1, inplace=True)
        comp[df].drop('THERMOMETER 2 P.M.',axis=1, inplace=True)
        
            


# In[110]:


for df in range (len(comp)):
    if 'THERMOMETER 3 P.M.' in comp[df]:
        comp[df].rename(columns={'THERMOMETER DECK':'THERMOMETER'},inplace=True)
        comp[df].drop('THERMOMETER 9 A.M.',axis=1, inplace=True)
        comp[df].drop('THERMOMETER 3 P.M.',axis=1, inplace=True)


# In[111]:


for df in range (len(comp)):
    if 'THERMOMETER AIR' in comp[df]:
        if df==24:
            comp[df].rename(columns={'THERMOMETER AIR':'THERMOMETER'},inplace=True)
            comp[df].drop('THERMOMETER ATTACHED',axis=1, inplace=True)
            
        else:
            comp[df]['THERMOMETER']=comp[df].apply(lambda x: (x['THERMOMETER ATTACHED']+x['THERMOMETER AIR']+x['THERMOMETER WET'])/3,axis=1)
            comp[df].drop('THERMOMETER ATTACHED',axis=1, inplace=True)
            comp[df].drop('THERMOMETER AIR',axis=1, inplace=True)
            comp[df].drop('THERMOMETER WET',axis=1, inplace=True)

            


# In[112]:


for df in range (len(comp)):
    if 'THERMOMETER IN STERN GALLEY IN SHADE' in comp[df]:
        comp[df]['THERMOMETER']=comp[df].apply(lambda x: (x['THERMOMETER TIMEKEEPERS']+x['THERMOMETER IN STERN GALLEY IN SHADE'])/2,axis=1)
        comp[df].drop('THERMOMETER TIMEKEEPERS',axis=1, inplace=True)
        comp[df].drop('THERMOMETER IN STERN GALLEY IN SHADE',axis=1, inplace=True)


# In[113]:


for df in range (len(comp)):
    if 'THERMOMETER MAX' in comp[df]:
        comp[df]['THERMOMETER MAX']=comp[df]['THERMOMETER MAX'].apply(lambda x: np.NaN if type(x)==str else x)
        comp[df]['THERMOMETER MIN']=comp[df]['THERMOMETER MIN'].apply(lambda x: np.NaN if type(x)==str else x)
        comp[df]['THERMOMETER']=comp[df].apply(lambda x: (x['THERMOMETER MAX']+x['THERMOMETER MIN'])/2,axis=1)
        comp[df].drop('THERMOMETER MAX',axis=1, inplace=True)
        comp[df].drop('THERMOMETER MIN',axis=1, inplace=True)
        
        


# In[114]:


for df in range (len(comp)):
    if 'THERMOMETER( C)' in comp[df]:
        comp[df].rename(columns={'THERMOMETER( C)':'THERMOMETER'},inplace=True)
        comp[df].drop('THERMOMETER(F)',axis=1, inplace=True)


# In[115]:


for df in range (len(comp)):
    if 'THERMOMETER(F)' in comp[df]:
        comp[df].rename(columns={'THERMOMETER(F)':'THERMOMETER'},inplace=True)


# In[116]:


for df in range (len(comp)):
    if 'THERMOMETER©' in comp[df]:
        comp[df].rename(columns={'THERMOMETER©':'THERMOMETER'},inplace=True)


# In[117]:


for df in range (len(comp)):
    if 'WEATHER' in comp[df]:
        comp[df].rename(columns={'WEATHER':'THERMOMETER'},inplace=True)


# In[118]:


for df in range (len(comp)):
    if 'THERMOMETER' not in comp[df]:
        comp[df]['THERMOMETER']=np.NaN


# In[119]:


comp[17]=comp[17].loc[:,~comp[17].columns.duplicated()]


# In[120]:


comp[0]['THERMOMETER']=np.NaN


# In[121]:


for df in range (len(comp)):
    comp[df]['THERMOMETER']=comp[df]['THERMOMETER'].apply(lambda x: np.NaN if type(x)==str else x)
            


# In[122]:


for df in range (len(comp)):
    comp[df]['THERMOMETER']=comp[df]['THERMOMETER'].apply(lambda x: (x-32)*(5/9) if np.mean(comp[df]['THERMOMETER'].value_counts().index)>35 else x)
    


# In[123]:


for df in comp:
    df.drop([0,1,2], axis=0, inplace=True)


# In[124]:


for df in comp:
    df.reset_index(inplace=True)


# # YEAR , MONTH,DAY

# In[125]:


for df in range (len(comp)):
    if 'YEAR' not in comp[df]:
        comp[df]['YEAR']=np.NaN


# In[126]:


for df in range (len(comp)):
    if 'MONTH' not in comp[df]:
        comp[df]['MONTH']=np.NaN


# In[127]:


for df in range (len(comp)):
    if 'DAY' not in comp[df]:
        comp[df]['DAY']=np.NaN


# # MERGING

# In[128]:


for df in range (len(comp)):
    comp[df]=comp[df][['YEAR','MONTH','DAY','BAROMETER','THERMOMETER','LATITUDE','LONGITUDE']]


# In[129]:


final_df=pd.concat(comp,axis=0)


# In[130]:


final_df.reset_index(inplace=True)


# In[131]:


final_df.drop(columns=['index'],inplace=True)


# In[132]:


final_df.to_csv('final_df.csv')

