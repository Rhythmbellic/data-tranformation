#importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
#initiating
data=pd.read_csv("Raw_Housing_Prices3.csv")
data.info()
#applying data tranforming techniques to make required things in data
data['Zipcode']=data['Zipcode'].astype(object)
data['No of Times Visited'].unique()
data.info()
mapping={'None':0,
       'Once':1,
       'Twice':2,
       'Thrice':3,
       'Four':4}
data['No of Times Visited']=data['No of Times Visited'].map(mapping)
data['No of Times Visited']=data['No of Times Visited'].astype(int)
data.info()
data["Ever Renovated"]=np.where(data["Renovated Year"]==0,"No","Yes")
data["Ever Renovated"]
data['Purchase Year']=pd.DatetimeIndex(data['Date House was Sold']).year
data['Years Since Renovation']=np.where(data['Ever Renovated']=='Yes',abs(data['Purchase Year']-data['Renovated Year']),0)
data.drop(columns=['Purchase Year','Date House was Sold','Renovated Year'],inplace=True)
#now or data is tranformed so we will find corelation to know relation of variable with each other
data.drop(columns=['ID']).corr()
#we cannot find relation of catagorical value so we will use anova to find it in next respo
