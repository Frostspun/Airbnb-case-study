#!/usr/bin/env python
# coding: utf-8

# <center><h1 style="color: pink"> Welcome to the Airbnb Mini Practice Project </h1>
# 

# <img src = "airbnb_header.jpeg" width="800" height="600">

# As you've worked through Python Sub Unit you would have realised there are a number of powerful functions you can use.
# 
# You would have covered the following libraries:
# 
# <li> Matplotlib </li>
# <li> Pandas </li> 
#     
# These are all powerful libraries to help augment your data analysis capabilities.
# In these set of exercises below, we've crafted a few extra challenges to reinforce your understanding of how these libraries work. 
# 
# Please note there is a particular emphasis on the Pandas Library as this is the most critical library you will be using throughout your career as a data analyst. You'll see the similarities that hold with respect to Pandas and Pivot Tables!
#     
# <b><u>`The most important thing to build confidence with Python is to practice all the time. This way you will build muscle memory. Don't simply copy the code you've written previously but write it again and again so you build the muscle memory associated with these coding libraries.`</u>
# 
# <H3>  Let's get started! </H3>

# We've provided a file called `airbnb_2.csv` that you'll need to import.
# 
# Let's do this first before we start our analysis.
# 
# <b> Don't forget to import the libraries you need to read .csv files! </b> 
# 
# 

# ### Step 1: <span style="color:pink">Import Libraries</span> 
# 
# Import the pandas library below. 
# 
# <b> Put your code in the box below </b>
# 

# In[3]:


import pandas as pd


# ### Step 2: <span style="color:pink">Ingest the Airbnb CSV file into your Jupyter Notebook</span> 

# Now that you have the Pandas Libraries imported, it's time to import the airbnb dataset.
# 
# <b> i) Please ingest the airbnb dataset using the `.read_csv()` syntax.
# 
# ii) Upon completion of this, use .info() to better understand the variables inside your dataset.
# <p>    
# 
# <b> Put your code in the box below </b>

# In[4]:


airbnb_data = pd.read_csv("airbnb_2.csv")

airbnb_data.info()
# ### Step 3: <span style="color:pink">Exploring your data with Pandas</span> 
# 
# The rest of these questions will have you focus on using the following Pandas Skills:
# 
# <li> Subsetting a Pandas dataframe using [] and boolean operators </li>
# <li> Summing up Records with value_counts()</li>
# <li> Creating calculated fields </li>
# <li> Group By in Pandas </li> 
# <li> Creating Bar Plots with Matplotlib</li> 
# 
# 

# <b> i)  Please count how many airbnb listings are in each of the 5 Neighbourhood Groups (Manhattan, Brooklyn, Queens, Bronx, Staten Island) and identify which Neighbourhood Groups has the largest number of Airbnb Listings </b>
# 
# Hint: Think about how you might use the `.value_counts()` methodology! 
# 
# <p>

# 

# We want to focus our attention on the Neighbourhood Groups that have the top 3 number of Airbnb Listings.
# 
# <b> ii) Calculate the % listings that each Neighbourhood Group contains. </b>
# 
# Hint: Take a look at the examples shown <a href = "https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html"> here!</a>  

# In[5]:


airbnb_data["neighbourhood_group"].value_counts(sort=True)


# <b> Put your code in the box below </b>

# In[6]:


airbnb_data["neighbourhood_group"].value_counts(normalize=True, sort=True)*100


# <h2 style='color:salmon'> Sample Output </h3>

# In[8]:





# <b> iii) Create a new calculated field called Revenue and place this into the Airbnb Dataframe. This is to be calculated by using the Price Column x Number_Of_Reviews Columns </b>
# 
# <b> Put your code in the box below </b>

# In[7]:


airbnb_data["revenue"] = airbnb_data["price"] * airbnb_data["number_of_reviews"]

airbnb_data.head()


# <h2 style='color:salmon'> Sample Output </h3>

# In[14]:





# <b> iv) Create a Bar Plot that shows which Neighbourhood Group has the highest average revenues. In order to best
# calculate this, you'd want to consider how you can use the .groupby() syntax to assist you! </b>
# 
# Hint: If you're stuck, we recommend you go back to <a href = https://learn.datacamp.com/courses/manipulating-dataframes-with-pandas> this </a> datacamp link. Specifically Chapter 4 which covers how GROUP BY is used in Pandas.
# 
# Remember, the syntax for GROUP BY is below:
# 
# `dataframe.groupby(['SomeColumn']).someAggregation()`
# 
# <b> Put your code in the box below </b>

# In[8]:


airbnb_data.groupby("neighbourhood_group")["revenue"].mean().plot(kind="bar")


# <h2 style='color:salmon'> Sample Output </h3>

# In[18]:





# <h3> <span style="color:pink">Challenge Questions</span> </h3>

# <b> V) Filter the Airbnb Dataframe to include only the Neighbourhood Groups `Manhattan`, `Brooklyn` and `Queens`. 
#     
# Upon completion of this, identify the `top 3 Revenue Generating Neighborhoods` within each of the `three Neighbourhood_Groups`. This should give us 9 Overall Rows: 3 of the top generating neighbourhoods within each of the 3 Neighbourhood_Groups </b>
# 
# This is a tricky question that will *test* your group-by skills.
# 
# We recommend you consider breaking down the query into a number of steps.
# 
#     condition1 = someDataFrame['someColumn']=='someCondition'
#     condition2 = someDataFrame['someColumn']=='someCondition'
#     
# <b> Step One - Filter the Dataframe using the Conditions </b>
# 
#     filtered_dataframe = someDataFrame[condition1 OR condition 2] 
#     
# You can also make use of the `.isin()` syntax to help filter on multiple conditions in a cleaner manner!
# 
#     dataframe['SomeColumn'].isin(['A','B','C'])
#         
# <b> Step Two - Group the Data by Neighbourhood_Group and Neighbourhood. </b>
#     
# Remember the dataframe syntax for grouping by is:
#     
# `dataframe.groupby(['SomeColumn']).someAggregation()`
#     
# Once you've now grouped your results - how can you ensure you only return the <u> top 3 for each neighbourhood group?</u>
#     
# This is where you'll need to make use of the following functions:
#     `dataframe.reset_index()`
#     `dataframe.groupby()`
#     `dataframe.head()`
#    
# You will want to make use of the .reset_index(inplace=True) function to help reset the indexes in 
# your Grouped Up Dataframe...!
#       
# <b> Put your code in the box below </b>

# In[13]:


grouped_filtered_airbnb_data = filtered_airbnb_data.groupby(["neighbourhood_group","neighbourhood"])["revenue"].sum().reset_index().sort_values("revenue", ascending=False)

top_filtered_airbnb_data = grouped_filtered_airbnb_data.groupby("neighbourhood_group").head(3)

print(top_filtered_airbnb_data)


# <h2 style='color:salmon'> Sample Output </h3>

# In[4]:





# <b> VI) Building on the previous question where you identified the top 3 Neighbourhoods within each of the three neighbourhood_groups based off Revenues, please filter the Airbnb Dataframe to include only these neighbourhoods. 
#     
# Upon completion of this, identify the  <b>`top average revenue generating room type`</b> for each of the nine neighbourhoods and plot this out in a Bar Chart.</b>
# 
# <b> Step One. Think carefully regarding how you can make use of the <u> list of 9 neighbourhoods </u> you've previously analyzed. </b>
#     
# <b> Step Two. Filter the original `airbnb` dataframe you created, to include only these top 9 neighbourhoods. </b>
# 
# <b> Step Three: Apply your standard aggregation syntax you've previously learned when using the .groupby() function </b>
# 
# <b> Step Four. Just as you previously made use of `.head()` and `.reset_index()` to get the top neighbourhoods - how might you use a similar approach to get the top `room_type` for each `neighbourhood`? </b>
# 
# <b> Step Five. Create a bar plot from your dataframe using the `matplotlib` plotting library syntax. </b>
# 
# We've included an example of the syntax below: 
# 
# `plt.bar(x=dataframe['x-axis'], height=dataframe['y-axis']`
# 
# 
# 
# This is a tricky question that will *test* your group-by skills. Think back to the previous question and how you approached this; you can approach this in a similar manner. 
#    
#     
#  <b> Put your code in the box below </b>      

# In[15]:


nbhd_1 = airbnb_data["neighbourhood"] == "Williamsburg"
nbhd_2 = airbnb_data["neighbourhood"] == "Bedford-Stuyvesant"
nbhd_3 = airbnb_data["neighbourhood"] == "Harlem"
nbhd_4 = airbnb_data["neighbourhood"] == "Hell's Kitchen"
nbhd_5 = airbnb_data["neighbourhood"] == "East Village"
nbhd_6 = airbnb_data["neighbourhood"] == "Bushwick"
nbhd_7 = airbnb_data["neighbourhood"] == "Astoria"
nbhd_8 = airbnb_data["neighbourhood"] == "Long Island City"
nbhd_9 = airbnb_data["neighbourhood"] == "Flushing"

nbhd_airbnb_data = airbnb_data[nbhd_1 | nbhd_2 | nbhd_3 | nbhd_4 | nbhd_5 | nbhd_6 | nbhd_7 | nbhd_8 | nbhd_9]

grouped_nbhd_airbnb_data = nbhd_airbnb_data.groupby(["neighbourhood","room_type"])["revenue"].mean().reset_index().sort_values("revenue", ascending=False)

top_grouped_nbhd_airbnb_data = grouped_nbhd_airbnb_data.groupby("neighbourhood").head(1)

#print(top_grouped_nbhd_airbnb_data)

top_grouped_nbhd_airbnb_data.groupby(["neighbourhood","room_type"], sort=False)["revenue"].mean().plot(kind="bar", title="Popular Airbnb Neighbourhoods by Room Type")


# <h2 style='color:salmon'> Sample Output </h3>

# In[5]:




