#!/usr/bin/env python
# coding: utf-8

# In[1]:


# List of high schools

high_schools = ["Hernandez High School" , "Figueroa High School" , "Wilson High School", "Wright High School"]


# In[2]:


for school in high_schools:
    print(school)


# In[10]:


# A dictionairy of high schools and the type of school.

high_school_types = [{"High School": "Griffin", "Type": "District"},
                    {"High School": "Figueroa", "Type": "District"},
                    {"High School": "Wilson" , "Type": "Charter"},
                    {"High School": "Wright", "Type": "Charter"}]


# In[13]:


for type in high_school_types:
    print(type)


# In[14]:


# List of High Schools

high_schools = ["Huang High School", "Figueroa High School", "Shelton High School", "Hernandez High School", "Griffin High School", "Wilson High School",]


# In[15]:


# Add the Pandas dependency.

import pandas as pd


# In[16]:


# Create a Pandas Series from a list.

school_series = pd.Series(high_schools)


# In[17]:


# Create a Pandas Series from a list.

school_series = pd.Series(high_schools)

school_series


# In[18]:


# A dictionary of high schools

high_school_dicts = [{"School ID": 0, "school_name": "Huang High    School", "type": "District"},
                   {"School ID": 1, "school_name": "Figueroa High School", "type": "District"},
                    {"School ID": 2, "school_name":"Shelton High School", "type": "Charter"},
                    {"School ID": 3, "school_name":"Hernandez High School", "type": "District"},
                    {"School ID": 4, "school_name":"Griffin High School", "type": "Charter"}]


# In[19]:


school_df = pd.DataFrame(high_school_dicts)

school_df


# In[20]:


# Three separate lists of information on high schools

school_id = [0, 1, 2, 3, 4]

school_name = ["Huang High School", "Figueroa High School", "Shelton High School", "Hernandez High School", "Griffin High School"]

type_of_school = ["District", "District", "Charter", "District", "Charter"]


# In[21]:


# Initilalize a new DataFrame

schools_df = pd.DataFrame()


# In[22]:


#Add the list to a new Data Frame

schools_df["School ID"] = school_id

#Print the DataFrame

schools_df


# In[23]:


schools_df["School Name"] = school_name

schools_df["Type of School"] = type_of_school

schools_df


# In[24]:


# Create a dictionary of information on high schools.

high_schools_dict = {'School ID': school_id, 'School Name':school_name, 'type':type_of_school}


# In[25]:


school_df = pd.DataFrame(high_school_dicts)

school_df


# In[27]:


school_df.columns


# In[29]:


school_df.values


# In[53]:


# Add the Pandas dependency.

import pandas as pd


# In[54]:


# Files to load

school_data_to_load = "Resources/schools_complete.csv"

student_data_to_load = "Resources/students_complete.csv"


# In[55]:


# Read the school data file and store it in a Pandas DataFrame.

school_data_df = pd.read_csv(school_data_to_load)

school_data_df


# In[46]:


# Read the student data file and store it in a Pandas DataFrame.

student_data_df = pd.read_csv(student_data_to_load)

student_data_df.head()


# In[50]:


# Read the student data file and store it in a Pandas DataFrame.

student_data_df = pd.read_csv(student_data_to_load)

student_data_df.head


# In[ ]:




