#!/usr/bin/env python
# coding: utf-8

# # Assignment 3 Data Visualization using python with Airbnb Dataset

# I am using 2 different dataset HR Dataset and  Airbnd dataset to show 10 different visualization

# In[1]:


# first we have to import libraries 
# here first i am using Airbnb Dataset


# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


# In[60]:


df=pd.read_csv('D:\Airbnb.csv')


# In[61]:


df


# In[62]:


print(df.columns)


# In[ ]:


# using Bar chat i hsve created  the bar chart to visulazise the count of listing in each nieghborhood group . this provide s an overview of the distribution of listing .


# In[13]:


neighborhood_group_counts=df['neighbourhood_group'].value_counts()


# In[14]:


#create a bar plot
plt.figure(figsize=(8,6))
neighborhood_group_counts.plot(kind='bar')
plt.xlabel('neighborhood Group')
plt.ylabel('Count')
plt.title('Number of Listings in Each neighborhood Group')
plt.show()


# In[15]:


# in the above chart it shows that "MANHATTAN" has the hightest neighborhood  group .


# In[16]:


# using Bar chat i hsve created  the bar chart to visulazise the count of listing in each nieghborhood . this provide s an overview of the distribution of listing .


# In[17]:


neighborhood_counts=df['neighbourhood'].value_counts()


# In[18]:


# create the bar plot
plt.figure(figsize=(8,6))
neighborhood_counts.plot(kind='bar')
plt.xlabel('neighborhood ')
plt.ylabel('Count')
plt.title('Number of Listings in Each neighborhood ')
plt.show()


# In[19]:


# in the above chart it shows that "WILLIAMSBURG" has the hightest neighborhood.


# In[20]:


#we use the scatter plot to show the geographical distribution of listing using latitude and longitude coordinate.


# In[21]:


plt.figure(figsize=(10,8))
plt.scatter(df['longitude'],df['latitude'],alpha=0.5)
#set the lable
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographical Distribution of Listings')
plt.show()


# In[22]:


#the above scatterd plot show that most of the airbnb is situated in between Latitude (40.70,40.70) to Longitude (-74.00, 73.90)


# In[23]:


#we use Histogram to show the distribution of listing prices . 


# In[24]:


plt.hist(df['price'], bins=20, edgecolor='k')
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Distribution of Listing Prices')
plt.show()


# In[25]:


# we can see in the above histogram most of the airbnb price range in betwen 100 to 200.


# In[26]:


# we use box plot  that can be used to compare the distribution of prices across different room types .
# it also show the quartiles range for the price  within each  room type.


# In[37]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='room_type', y='price')
plt.xlabel('Room Type')
plt.ylabel('Price')
plt.title('Distribution of Listing Prices by Room Type')
plt.xticks(rotation=45)
plt.show()


# In[38]:


grouped_data = df.groupby('room_type')
quartiles = grouped_data['price'].quantile([0.25, 0.75]).unstack()
quartiles['IQR'] = quartiles[0.75] - quartiles[0.25]
print(quartiles)



# In[39]:


# we use box plot for examine the distribution of isting prices across different neighborhood .
# and also show the quartile range for the price with in each neighborhood group.


# In[41]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='neighbourhood_group', y='price')
plt.xlabel('Neighbourhood group')
plt.ylabel('Price')
plt.title('Distribution of Listing Prices by Neighbourhood group')
plt.xticks(rotation=45)
plt.show()


# In[42]:


grouped_data = df.groupby('neighbourhood_group')
quartiles = grouped_data['price'].quantile([0.25, 0.75]).unstack()
quartiles['IQR'] = quartiles[0.75] - quartiles[0.25]
print(quartiles)


# In[ ]:


#Heatmaps can be employed to show the concentration or density of listings across a geographic area using Longitude and Latitude.


# In[50]:


from scipy import ndimage
plt.figure(figsize=(10, 8))
bins = [50, 50]
heatmap, xedges, yedges = np.histogram2d(df['latitude'], df ['longitude'], bins=bins)
heatmap = ndimage.gaussian_filter(heatmap, sigma=2)
sns.heatmap(heatmap.T, cmap='viridis')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Density of Airbnb Listings')
plt.show()


# # Assignment 3 Data Visualization using HR dataset.

# In[4]:


Hr=pd.read_csv('D:\HR.csv')


# In[5]:


Hr


# In[6]:


# There are so many columns in HR dataset so we use print columns to get the columns name .
print(Hr.columns)


# In[7]:


missing_values=Hr.isnull().sum()
print(missing_values)


# In[8]:


# As we see in managerid we have 8 missing values either we have to fill that value with most common manager id or just Drop the row .
# here we see missing id are only 8 and it will not impact the result so we can choose to drop the row .


# In[9]:


Hr.dropna(subset=['ManagerID'],inplace=True)


# In[10]:


Hr.to_csv('updated_HR.csv',index=False)


# In[11]:


Hr


# In[12]:


missing_values=Hr.isnull().sum()
print(missing_values)


# In[20]:


# Now are dataset is clean we can perform Data Visualization 


# In[ ]:


# we use BAR PLOT for REcruitmentSource to show through wich sources people get hired.


# In[36]:


column_to_plot='RecruitmentSource'
source_counts=Hr[column_to_plot].value_counts()
plt.figure(figsize=(12,6))
sns.barplot(x=source_counts.index, y=source_counts.values)
plt.title('Recruitment Source Distribution')
plt.xlabel('Recruitment Source')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')


plt.tight_layout()
plt.show()


# In[ ]:


#seeing the upper chart we can say that most of the people get hired through Indeed and Linkedin.


# In[ ]:


# And aslo we can see the performance chart using BAR PLOT using PerformanceScore column.


# In[60]:


column_to_plot='PerformanceScore'
source_counts=Hr[column_to_plot].value_counts()
total_count =source_counts.sum()
Performance_percentages = (source_counts / total_count) * 100

plt.figure(figsize=(5,6))
pt = Performance_percentages.plot(kind='bar')

pt.set_title('Performance Score of Employee')
pt.set_xlabel('Performance Score')
pt.set_ylabel('count')
plt.xticks(rotation=45, ha='right')
#Display the percentage values on top of each bar.
for p in pt.patches:
    pt.annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')
    
plt.tight_layout()
plt.show()


# In[ ]:


# we can clearly see that 77.89% of the employee fully meet the target. and by using this chart we can see on which side we have to focus.


# In[ ]:


#we use BOX PLOT to show salary of employee in each department.


# In[13]:


column_to_plot='Salary'
category_column='Department'
plt.figure(figsize=(10,6))
sns.boxplot(x=category_column,y=column_to_plot,data=Hr)
plt.title('Salary Distribution by Department')
plt.xlabel(category_column)
plt.ylabel(column_to_plot)
plt.tight_layout()
plt.show()


# In[ ]:


# we use pie chart to show the percentage of male and female employee.


# In[18]:


gender_counts = Hr['Sex'].value_counts()

plt.figure(figsize=(6, 6))  
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Male and Female Workers')

plt.show()


# In[ ]:


# we use pie chart to show the Marital Status of the employee.


# In[20]:


gender_counts = Hr['MaritalDesc'].value_counts()

plt.figure(figsize=(6, 6))  
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Marital Status of the employee')

plt.show()


# In[ ]:


# use bar plot to show Number of employee to work in each department.


# In[21]:


department_column = 'Department'
department_counts = Hr[department_column].value_counts()
plt.figure(figsize=(10, 6))
sns.countplot(x=department_column, data=Hr)
plt.title('Number of Employees in Each Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()


# In[ ]:


# use pie chart to show Race Description .


# In[23]:


gender_counts = Hr['RaceDesc'].value_counts()
plt.figure(figsize=(6, 6))  
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Race Description of employee')
plt.show()


# In[25]:


# use histogram Chart to represent the employee  Satisfaction .


# In[24]:


satisfaction_column = 'EmpSatisfaction'
plt.figure(figsize=(8, 6)) 
plt.hist(Hr[satisfaction_column], bins=10, edgecolor='black')
plt.title('Employee Satisfaction Distribution')
plt.xlabel('Satisfaction Level')
plt.ylabel('Frequency')
plt.show()


# In[ ]:


#use count chart to show the count termination reasone


# In[27]:


termination_column = 'TermReason'
termination_counts = Hr[termination_column].value_counts()
plt.figure(figsize=(15, 9)) 
sns.countplot(x=termination_column, data=Hr)
plt.title('Termination Reasons')
plt.xlabel('Termination Reason')
plt.ylabel('Count')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()


# In[ ]:


# use pie chart to show the percentage of employment status.


# In[28]:


gender_counts = Hr['EmploymentStatus'].value_counts()
plt.figure(figsize=(6, 6))  
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Employment Status of employee')
plt.show()


# In[ ]:




