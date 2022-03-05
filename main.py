import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/nasriAhmed/DataCleaningPorject/master/Data/data.csv"
data = pd.read_csv(url)
df = pd.DataFrame(data=data,columns=['Incident ID','Status','Affected CI','Primary Affected Service','Title','Assignment Group','Open Time','Area','Outage Start','Outage End','Assignee','Closure Code','Solution','Description','Department'])

df.drop(['Department','Description','Assignee','Status','Solution'],1,inplace=True)
print(df)

df.drop(df.loc[df['Closure Code']=='Incident Rejected'].index, inplace=True)
df.drop(df.loc[df['Area']=='Opération Programée'].index, inplace=True)
print(df)

#df= df[['Outage End']] - df[['Outage Start']]
df['Down Time'] = pd.to_datetime(df['Outage End']) - pd.to_datetime(df['Outage Start'])

print(df)
urll = "https://raw.githubusercontent.com/nasriAhmed/DataCleaningPorject/master/Data/data_2.csv"
data_2 = pd.read_csv(urll)
print(data_2)
#data_final= pd.merge(data,data_2,on='Affected CI')
#print(data_final)