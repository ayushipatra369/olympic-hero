# ====================================
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

# Code starts here
# Load data and renamed one column
data = pd.read_csv(path)
data = data.rename(columns={'Total':'Total_Medals'})
data.head(10)

# # Summer or Winter? Which is the better event 
summer_winter = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', summer_winter)
better_event = data['Better_Event'].value_counts().index[0]
print(f'{better_event} has been a better event with respect to all the performing countries') 

# ===========================================================================================================================

# # Finding out the best performing countries across all events

# Created a new DataFrame subset with four columns as needed
top_countries = data.loc[:,['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]

# Dropped the last row from the DataFrame top_countries as it contains sum of the medals
top_countries = top_countries[:-1]

# Created a function that returns top ten country's list

def top_ten(dataframe, columns):
    country_list = []
    df = dataframe.nlargest(10, columns) 
    country_list = df.iloc[:, 0:1]
    country_list = list(country_list['Country_Name'])  
    return country_list 

# Calling top_ten() function for different columns in dataframe top_countries 

top_10_summer = top_ten(top_countries, 'Total_Summer') 
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

# Created a new list 'common' which stores common elements between 3 list defined above
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10)) 

# ===========================================================================================================================

# # Plotted the medal count of the top 10 countries for better visualisation
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.sort_values('Total_Summer', ascending=True).plot.bar(x='Country_Name', y='Total_Summer', color='c') 
winter_df.sort_values('Total_Winter', ascending=True).plot.bar(x='Country_Name', y='Total_Winter', color='c')
top_df.sort_values('Total_Medals', ascending=True).plot.bar(x='Country_Name', y='Total_Medals', color='c') 

# ===========================================================================================================================

# # Found out which country has had the best performance with respect to the ratio between gold medals won and total medals won.
# Summer Golden Ratio
summer_df['Golden_Ratio'] = data['Gold_Summer'] / data['Total_Summer']

# Summer Max Golden Ratio
summer_max_ratio = summer_df['Golden_Ratio'].max()

# Summer Country per Max Golden Ratio
scg = summer_df.groupby('Country_Name')['Golden_Ratio'].agg('max').sort_values(ascending=False).to_frame().reset_index() 
summer_country_gold = scg['Country_Name'].loc[0] 

# Winter Golden Ratio
winter_df['Golden_Ratio'] = data['Gold_Winter'] / data['Total_Winter']

# Winter Max Golden Ratio
winter_max_ratio = winter_df['Golden_Ratio'].max()

# Winetr Country per Max Golden Ratio
wcg = winter_df.groupby('Country_Name')['Golden_Ratio'].agg('max').sort_values(ascending=False).to_frame().reset_index() 
winter_country_gold = wcg['Country_Name'].loc[0] 

# Top Golden Ratio
top_df['Golden_Ratio'] = data['Gold_Total'] / data['Total_Medals']

# Top Max Golden Ratio
top_max_ratio = top_df['Golden_Ratio'].max()

# Top Country per Max Golden Ratio
tcg = top_df.groupby('Country_Name')['Golden_Ratio'].agg('max').sort_values(ascending=False).to_frame().reset_index() 
top_country_gold = tcg['Country_Name'].loc[0] 

# ===========================================================================================================================

# # Found out the best overall perfomer who won most gold
# Maximum points scored
data_1 = data[:-1]
data_1['Total_Points'] = data['Gold_Total']*3 + data['Silver_Total']*2 + data['Bronze_Total']*1 
most_points = data_1['Total_Points'].max()

# Best Country in winning most Gold
country_grouped = data_1.groupby('Country_Name')['Total_Points'].agg('max').sort_values(ascending=False).to_frame().reset_index() 
best_country = country_grouped['Country_Name'].loc[0] 

# # Plotted the medal count of the Best performer to visualise their success better.
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()

plt.xlabel('United States')
plt.ylabel('Medals Tally')

plt.xticks(rotation=45)


