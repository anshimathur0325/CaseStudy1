import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
#Create dataframes for each csv file
cab_df = pd.read_csv('Cab_data.csv')
city_df = pd.read_csv('City.csv')
customer_df = pd.read_csv('Customer_ID.csv')
transaction_df = pd.read_csv('Transaction_ID.csv')

#Add a column to get the total income per ride
total = cab_df['Price Charged']-cab_df['Cost of Trip']
cab_df['Total'] = total

#Change the date of travel column to a datetime format. 
cab_df["Date of Travel"] = pd.to_datetime(cab_df["Date of Travel"], format = "%m/%d/%Y")








#Count of Payment Modes
plt.figure(figsize=(9,6))
ax =sns.countplot(x='Payment_Mode', data=cab_df, hue='Company')
for i in ax.containers:
  ax.bar_label(i,)
plt.title('Count of Payment Modes')
plt.xlabel('Payment Mode')
plt.ylabel('Count')
plt.show()



#Users Per City
plt.figure(figsize=(9,6))
sns.barplot(x='City', y='Population', data=city_df, order=city_df.sort_values('Users').City, )
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.title('Users per City')
plt.show()

#Date of Travel vs Income Earned per Cab Company
plt.figure(figsize=(9,6))
sns.lineplot(x='Date of Travel', y='Total', data=cab_df, hue='Company')
plt.title('Date of Travel vs Income Earned per Cab Company')
plt.xlabel('Date of Travel')
plt.ylabel('Income Earned per Cab Company')
plt.show()


#Distance Traveled vs Income earned per cab company 
plt.figure(figsize=(9,6))
sns.lineplot(x='KM Travelled', y='Total', data=cab_df, hue='Company')
plt.title("Distance Traveled vs Income per Cab Ride")
plt.ylabel("Income per Car Ride")
plt.xlabel("Distance Traveled in KM")
plt.show()

#Total income per cab company
plt.figure(figsize=(9,6))
sns.histplot(x='Company', y='Total', data=cab_df)
plt.title("Company vs Income per Cab Ride")
plt.xlabel("Company")
plt.ylabel("Income per Car Ride")
plt.show()


#Count of Cabs per Company per City
plt.figure(figsize=(9, 6))
sns.countplot(x='Company', data=cab_df, hue=cab_df['City'])
plt.title('Count of Cabs per Company')
plt.ylabel('Count')
plt.xlabel('Company')
plt.show()

#Diagram of the companies and different totals per city. 
plt.figure(figsize=(9,6))
sns.histplot(x='Company',y='Total', data=cab_df, hue=cab_df["City"])
locs, labels = plt.xticks()
plt.setp(labels, rotation=45)
plt.title('Total vs Cabs')
plt.show()