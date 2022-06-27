#!/usr/bin/env python
# coding: utf-8

# ### THIS IS MY CLEANED FILE FOR SUBMITTAL.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Calculate the percentage of students who passed math **and** reading (% Overall Passing)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# #### THESE FIRST CODE BLOCKS ARE TO ANALYZE THE DATAFRAME CREATED FROM THE COMBINED CSVs.

# In[2]:


school_data_complete.head() # to see columns


# In[3]:


school_data_complete.describe() # to see statistical information that can be used


# In[4]:


school_data_complete["school_name"].nunique() # https://www.geeksforgeeks.org/how-to-count-distinct-values-of-a-pandas-dataframe-column/
# total number of schools


# In[5]:


school_data_complete["school_name"].value_counts() # how many students at each school


# In[6]:


school_data_complete["school_name"].value_counts().sum() # to verify total number of students


# #### Calculate the total number of schools.  ANSWER = 15

# In[7]:


school_data_complete["School ID"].nunique() # another way to get total number of schools


# In[8]:


total_schools = school_data_complete["School ID"].nunique() # to put into a variable name to add to summary dataframe
total_schools


# #### Calculate the total number of students.  ANSWER = 39170

# In[9]:


school_data_complete["Student ID"].nunique() # another way to get total students


# In[10]:


school_data_complete["Student ID"].count() # checking to see if count works


# In[11]:


total_students = school_data_complete["Student ID"].nunique() # to get into a variable to add to a summary dataframe
total_students


# #### Calculate the total budget.  ANSWER  = $24,649,428.00

# In[12]:


total_budget_amount = school_data_complete["budget"].unique().sum().round(2) # total budget
total_budget_amount


# In[13]:


# to round total budget
total_budget = "${:,.2f}".format(total_budget_amount) # https://www.adamsmith.haus/python/answers/how-to-format-currency-in-python
total_budget


# In[14]:


school_data_complete.dtypes  # I found I had to consistently keep track of datatypes.


# #### I WANTED TO TRY DIFFERENT METHODS TO GET ROUNDED NUMBERS FOR THE COMPUTED RESULTS.
# #### HENCE METHOD 1 AND METHOD 2.  BOTH METHODS SHOW THE RESULTS IN THE REQUIRED FORMAT.

# In[15]:


# Method 1 - using named variables for the rounded values


# #### Calculate the average math score.  ANSWER = 78.99

# In[16]:


average_math = school_data_complete["math_score"].mean()
rounded_math_average = round(average_math,2)
rounded_math_average


# #### Calculate the average reading score.  ANSWER = 81.88

# In[17]:


average_reading = school_data_complete["reading_score"].mean()
rounded_reading_average = round(average_reading,2)
rounded_reading_average


# #### THIS IS THE START OF CALCULATIONS TO Calculate the percentage of students with a passing math score (70 or greater)
# 

# In[18]:


passed_math = (school_data_complete["math_score"]>=70).sum() # https://stackoverflow.com/questions/50539880/python-count-dataframe-column-values-meeting-condition
passed_math


# #### PERCENTAGE OF STUDENS WITH A PASSING MATH SCORE (70 OR GREATER) = 74.98

# In[19]:


percent_passed_math = (((school_data_complete["math_score"]>=70).sum())/total_students)*100
rounded_percent_passed_math = round(percent_passed_math,2)
rounded_percent_passed_math


# #### Calculate the percentage of students with a passing reading score (70 or greater).  ANSWER = 85.81
# 
# 

# In[20]:


passed_reading = (school_data_complete["reading_score"]>=70).sum()
passed_reading


# In[21]:


percent_passed_reading = (((school_data_complete["reading_score"]>=70).sum())/total_students)*100
rounded_percent_passed_reading = round(percent_passed_reading,2)
rounded_percent_passed_reading


# In[22]:


passed_both = ((school_data_complete["reading_score"]>=70) & (school_data_complete["math_score"]>=70)).sum()
passed_both


# In[23]:


# one thing I noticed did not work
# passed_both = (passed_math & passed_reading).sum() # this gave a wildly different amount (522)
# also, this amount stayed in "passed_both" until I ran the code blocks again using the sum against the "and" of the dataframe columns


# #### Calculate the percentage of students who passed math **and** reading (% Overall Passing).  ANSWER = 65.17
# 

# In[24]:


percent_passed_both = (passed_both/total_students)*100
rounded_percent_passed_both = round(percent_passed_both,2)
rounded_percent_passed_both


# #### Create a dataframe to hold the above results
# 

# In[25]:


summary = [{"Total Schools": total_schools, "Total Students":total_students,
                                    "Total Budget":total_budget,
                                    "Average Math Score": rounded_math_average,
                                    "Average Reading Score": rounded_reading_average,
                                    "% Passing Math": rounded_percent_passed_math,
                                   "% Passing Reading": rounded_percent_passed_reading,
                                   "% Overall Passing": rounded_percent_passed_both}]
District_Summary_df = pd.DataFrame(summary)
District_Summary_df


# In[26]:


# Method 2 - using built in functions to round values


# In[27]:


average_math = school_data_complete["math_score"].mean()
round(average_math,2)


# In[28]:


average_reading = school_data_complete["reading_score"].mean()
round(average_reading,2)


# In[29]:


passed_math = (school_data_complete["math_score"]>=70).sum() # https://stackoverflow.com/questions/50539880/python-count-dataframe-column-values-meeting-condition
passed_math


# In[30]:


percent_passed_math = (((school_data_complete["math_score"]>=70).sum())/total_students)*100
round(percent_passed_math,2)


# In[31]:


passed_reading = (school_data_complete["reading_score"]>=70).sum()
passed_reading


# In[32]:


percent_passed_reading = (((school_data_complete["reading_score"]>=70).sum())/total_students)*100
round(percent_passed_reading,2)


# In[33]:


passed_both = ((school_data_complete["reading_score"]>=70) & (school_data_complete["math_score"]>=70)).sum()
passed_both


# In[34]:


percent_passed_both = (passed_both/total_students)*100
round(percent_passed_both,2)


# In[35]:


summary = [{"Total Schools": total_schools, "Total Students":total_students,
                                    "Total Budget":total_budget,
                                    "Average Math Score": round(average_math,2),
                                    "Average Reading Score": round(average_reading,2),
                                    "% Passing Math": round(percent_passed_math,2),
                                   "% Passing Reading": round(percent_passed_reading,2),
                                   "% Overall Passing": round(percent_passed_both,2)}]
District_Summary_df = pd.DataFrame(summary)
District_Summary_df


# # DATAFRAME TO SHOW THE DISTRICT SUMMARY

# In[36]:


District_Summary_df.set_index("Total Schools") # to hide index - https://python-forum.io/thread-32275.html


# ## STARTING SCHOOL SUMMARY

# In[37]:


# school_data_complete.head() # ran output again to cut down on scrolling


# In[38]:


# START of new dataframe so as not to affect the original.
schools_df = school_data_complete
# schools_df.head()


# In[39]:


# And made another copy of the copy to preserve datatypes.
schools70_df1 = schools_df.copy(deep=False) # https://appdividend.com/2020/08/07/pandas-dataframe-copy/


# In[40]:



# schools70_df1.head()


# In[41]:


# math70 = schools70_df["math_score"] >= 70
# reading70 = schools70_df["reading_score"] >= 70
# both70 = schools70_df[(schools70_df["math_score"] >= 70) & (schools70_df["reading_score"] >= 70)]
# these were initially used to clear error message in which >= was not recognized in groupby series and int. 


# In[42]:


# ADDED THESE EXTRA COLUMNS BECAUSE THEY ARE USEFUL LATER ON WITH THE GROUPBY OPERATION.


# In[43]:


schools70_df2 = schools70_df1.copy(deep=False)


# In[44]:


schools70_df2["math-over-70"] = schools70_df2["math_score"] >= 70


# In[45]:


schools70_df2["reading-over-70"] = schools70_df2["reading_score"] >= 70


# In[46]:


schools70_df2["both-over-70"] = (schools70_df2["math_score"] >= 70) & (schools70_df2["reading_score"] >= 70)


# In[47]:


schools70_df2.rename(columns={"budget": "Total School Budget", "type": "School Type",
                              "school_name": "School Name", "size": "Total Students"}, inplace=True)
# schools70_df2.head()
# TO GET COLUMN NAMES IN THE DESIRED FORMAT.


# In[48]:


# to keep track of the datatypes for budget columns
# schools70_df2.dtypes


# In[49]:


schools70_df2["Per Student Budget"] = schools70_df2["Total School Budget"] / schools70_df2["Total Students"]


# In[50]:


# schools70_df2.head()


# In[51]:


# TO MAKE SURE BUDGET DATATYPES REMAINED AS INT64 OR FLOAT64.
# schools70_df2.dtypes 


# In[52]:


# before formatting on budget columns changes from float to object
top_schools = schools70_df2.groupby(["School Name"])
# THIS IS THE BEGINNING OF THE "SCHOOL NAME" BECOMING A PERSISTENT KEY.
# top_schools.head() 


# In[53]:


# schools70_df2.dtypes


# In[54]:


# schools70_df2 to schools70_df3
# to use when map format budgets into dollars
schools70_df3 = schools70_df2.copy()
# schools70_df3.dtypes


# In[55]:


schools70_df3["Total School Budget"] = schools70_df3["Total School Budget"].map('${:,.2f}'.format)
schools70_df3["Per Student Budget"] = schools70_df3["Per Student Budget"].map('${:,.2f}'.format)
# schools70_df3.head()


# In[56]:


# budget columns datatypes have changed to object
# schools70_df3.dtypes


# In[57]:


# new groupby after formatting on budget columns changes from float to object
top_schools1 = schools70_df3.groupby(["School Name"])
# top_schools1.head() 


# In[58]:


# top_schools1 did nothing to group columns, but it kept the key at "School Name"
# This aided with calculates run after the groupby.


# In[59]:


# NOTE! NOTE! NOTE! Left all the rest of the calculations with
# top_schools in place.  Have not changed to top_schools1 yet.
# Will probably need to use top_schools1 for "School Summary" portion.
# FIXED


# In[60]:


# schools70_df2.head()


# In[61]:



# schools70_df2["math_score"].head()


# In[62]:


math_test1 = round(schools70_df2["math_score"].mean(),2)
# IT MATTERS WHICH DATAFRAME IS BEING REFERENCED NOW, WHETHER THE KEY IS PICKED UP OR NOT.
# SINCE DF IS schools70_df2, THE RESULTS OF math_test1 DON'T SHOW AGAINST EACH SCHOOL NAME LIKE THEY ARE
# GROUPBY DATAFRAME (top_schools1) IS USED.
#  Hence, the single value result versus the 15 results when the groupby key "School Name" is active.
# As shown in the next code block.
math_test1


# ### START OF ALL CALCULATIONS NEEDED FOR SCHOOL SUMMARY RESULTS

# In[63]:


math = round(top_schools1["math_score"].mean(),2)
math


# In[64]:


reading = round(top_schools1["reading_score"].mean(),2)
reading


# In[65]:


top_schools_total_students = top_schools1["Student ID"].nunique()
top_schools_total_students


# In[66]:


sum_math70 = top_schools1["math-over-70"].sum()
sum_math70


# In[67]:


total_students_top_schools = top_schools1["Total Students"]
total_students_top_schools.count()


# In[68]:


top_school_percent_passed_math = (sum_math70 / (total_students_top_schools.count()) * 100)
math_percent = round(top_school_percent_passed_math, 2)
math_percent


# In[69]:


sum_reading70 = top_schools1["reading-over-70"].sum()
sum_reading70


# In[70]:


top_school_percent_passed_reading = (sum_reading70 / (total_students_top_schools.count()) * 100)
reading_percent = round(top_school_percent_passed_reading, 2)
reading_percent


# In[71]:


sum_both70 = top_schools1["both-over-70"].sum()
sum_both70


# In[72]:


top_school_percent_passed_both = (sum_both70 / (total_students_top_schools.count()) * 100)
overall_percent = round(top_school_percent_passed_both, 2)
overall_percent


# In[73]:


# converted entire "budget" column too soon, and this caused formula to not work.
# Needed both "size" and "budget" to be int64 dtypes
# This forced me to go back and redo dataframes and new groupby with key "School Name" to preserve datatypes
# DON'T DO FORMATTING UNTIL ALL CALCULATIONS ARE DONE!
per_student_budget = top_schools1["Per Student Budget"]
per_student_budget.value_counts()                                                        


# In[74]:


top_schools_type = top_schools1["School Type"].unique()
#top_schools_type.value_counts()
top_schools_type


# In[75]:


top_schools_name = top_schools1["School Name"].unique()
# top_schools_name.value_counts()
top_schools_name


# In[76]:


budget_top_schools = top_schools1["Total School Budget"]
# formatted_total_budget = budget_top_schools.unique()
formatted_total_budget = budget_top_schools.value_counts()
formatted_total_budget.head()


# In[77]:


# top_schools1.head()


# In[78]:


top_schools1["School Name"].count()


# In[79]:


# top_schools1.nunique()


# In[80]:


# "School Name": top_schools_name.unique(),
# "Total School Budget": formatted_total_budget
# budget_top_schools.value_counts()


# ## SCHOOL SUMMARY RESULTS DATAFRAME

# In[81]:


schools_summary_df = pd.DataFrame({
                                   "School Type": top_schools_type,
                                   "Total Students": total_students_top_schools.count(),
                                   "Total School Budget": budget_top_schools.unique()
                                  })


# In[82]:


schools_summary_df["Per Student Budget"] = per_student_budget.unique()
schools_summary_df["Average Math Score"] = round(top_schools1["math_score"].mean(),2)
schools_summary_df["Average Reading Score"] = round(top_schools1["reading_score"].mean(),2)
schools_summary_df["% Passing Math"]  = round(top_school_percent_passed_math, 2)
schools_summary_df["% Passing Reading"] = round(top_school_percent_passed_reading, 2)
schools_summary_df["% Overall Passing"] = round(top_school_percent_passed_both, 2)
schools_summary_df#.set_index("school_name")


# In[83]:


# schools_summary_df.dtypes


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * % Overall Passing (The percentage of students that passed math **and** reading.)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# ### TOP PERFORMING SCHOOLS BY % OVERALL PASSING RESULTS DATAFRAME

# In[84]:


schools_summary_df.sort_values("% Overall Passing", ascending=False).head(5)


# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# ### BOTTOM PERFORMING SCHOOLS BY % OVERALL PASSING RESULTS DATAFRAME

# In[85]:


schools_summary_df.sort_values("% Overall Passing", ascending=True).head(5)


# In[86]:


# schools_summary_df.count()


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[87]:



# math_mean_df = schools70_df2.loc[(schools70_df2["grade"]), :]
# math_mean_df.head()


# In[88]:


# math_mean_by_grade = schools70_df2[["School Name", "grade", "Average Math Score"]]
# math_mean_by_grade.groupby(["School Name", "grade"]).mean()
# mm_by_grade = schools70_df2.value_counts(["School Name", "grade"])
# mm_by_grade.head()
mm_group = schools70_df2[["School Name", "grade", "math_score"]]
mm_group1 = mm_group.groupby(["School Name", "grade"])["math_score"].mean()
mm_group1.head()
# mm_group1.to_frame()


# In[89]:


mm_group = schools70_df2[["School Name", "grade", "math_score"]]
# mm_group1 = mm_group.groupby(["School Name", "grade"])["math_score"].mean()
# mm_group1.to_frame()
# mm_group9 = pd.DataFrame(mm_group.loc[mm_group["grade"]=="9th"])
# mm_group9.head()
# mm_group.head()


# In[90]:


# mm_group = schools70_df2[["School Name", "grade", "math_score"]]
# mm_group.groupby(["School Name", "grade"])["math_score"].mean()
mm_group2 = mm_group.groupby(["grade", "School Name"])["math_score"].mean()
# mm_group2.to_frame()


# In[91]:


mm_group3 = mm_group.groupby(["grade","School Name"])[["grade","math_score"]].mean()
# mm_group3


# In[92]:


mm_group4 = mm_group.groupby(["School Name","grade"])[["grade","math_score"]].mean().reset_index()
# mm_group4


# In[93]:


# FOR CONVENIENCE
# schools70_df2.head()


# In[94]:


# NEXT STEP! Try to drive .loc back to schools70_df2 - before any groupby
# repeat schools70_df2 for reference
schools70_df2.shape


# In[95]:


schools70_df2.columns


# In[96]:


# test1_df = schools70_df2[["School Name", "grade", "math_score"]]
# test1_df.head()
# don't need


# ### START OF CALCULATIONS USED IN MATH SCORES BY GRADE

# In[97]:


test1_df9 = schools70_df2.loc[schools70_df2["grade"] == "9th", ["School Name", "math_score"]]
# test1_df9.head()


# In[98]:


test1_df9_group = round(test1_df9.groupby(["School Name"])["math_score"].mean(),2)
test1_df9_group


# In[99]:


test1_df10 = schools70_df2.loc[schools70_df2["grade"] == "10th", ["School Name", "math_score"]]
test1_df10_group = round(test1_df10.groupby(["School Name"])["math_score"].mean(),2)
test1_df10_group


# In[100]:


test1_df11 = schools70_df2.loc[schools70_df2["grade"] == "11th", ["School Name", "math_score"]]
test1_df11_group = round(test1_df11.groupby(["School Name"])["math_score"].mean(),2)
test1_df11_group


# In[101]:


test1_df12 = schools70_df2.loc[schools70_df2["grade"] == "12th", ["School Name", "math_score"]]
test1_df12_group = round(test1_df12.groupby(["School Name"])["math_score"].mean(),2)
test1_df12_group


# ### START OF CALCULATIONS FOR READING SCORE BY GRADE
# * DONE SAME WAY AS MATH SCORE BY GRADE

# In[102]:


# start the same process for reading
read_ave_df9 = schools70_df2.loc[schools70_df2["grade"] == "9th", ["School Name", "reading_score"]]
read_ave_df9_group = round(read_ave_df9.groupby(["School Name"])["reading_score"].mean(),2)
read_ave_df9_group


# In[103]:


read_ave_df10 = schools70_df2.loc[schools70_df2["grade"] == "10th", ["School Name", "reading_score"]]
read_ave_df10_group = round(read_ave_df10.groupby(["School Name"])["reading_score"].mean(),2)
read_ave_df10_group


# In[104]:


read_ave_df11 = schools70_df2.loc[schools70_df2["grade"] == "11th", ["School Name", "reading_score"]]
read_ave_df11_group = round(read_ave_df11.groupby(["School Name"])["reading_score"].mean(),2)
read_ave_df11_group


# In[105]:


read_ave_df12 = schools70_df2.loc[schools70_df2["grade"] == "12th", ["School Name", "reading_score"]]
read_ave_df12_group = round(read_ave_df12.groupby(["School Name"])["reading_score"].mean(),2)
read_ave_df12_group


# #### THESE WERE THE INITIAL CALCULATIONS FOR MATH SCORE BY GRADE, BUT THE DATAFRAME DID NOT WORK.

# In[106]:


mm9 = mm_group4.loc[lambda mm_group4: mm_group4["grade"] == "9th"]
mean_math_9 = round(mm9, 2)
# mean_math_9


# In[107]:


mm10 = mm_group4.loc[lambda mm_group4: mm_group4["grade"] == "10th"]
mean_math_10 = round(mm10, 2)
# mean_math_10


# In[108]:


mm11 = mm_group4.loc[lambda mm_group4: mm_group4["grade"] == "11th"]
mean_math_11 = round(mm11, 2)
# mean_math_11


# In[109]:


mm12 = mm_group4.loc[lambda mm_group4: mm_group4["grade"] == "12th"]
mean_math_12 = round(mm12, 2)
# mean_math_12


# In[110]:


# mm12 = mm_group4.loc[lambda mm_group4: mm_group4["grade"] == "12th"].mean()
# mean_math_12 = [round(mm12, 2)]
# mean_math_12


# In[111]:


# mm9


# In[112]:


# "School Name": [mm_group4["School Name"]],


# ### MATH SCORES BY GRADE RESULTS DATAFRAME

# In[175]:


math_mean_by_grade = pd.DataFrame({
                                   "9th": test1_df9_group,
                                  "10th": test1_df10_group,
                                  "11th": test1_df11_group,
                                  "12th": test1_df12_group})
math_mean_by_grade


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# ### READING SCORE BY GRADE RESULTS DATAFRAME

# In[114]:


reading_mean_by_grade = pd.DataFrame({"9th": read_ave_df9_group,
                                      "10th": read_ave_df10_group,
                                      "11th": read_ave_df11_group,
                                      "12th": read_ave_df12_group})
reading_mean_by_grade


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[115]:


# REPEATED FOR CONVENIENCE
# schools_summary_df.head()


# In[116]:


# schools_summary_df.dtypes


# ### TO DETERMINE BIN SIZES FOR PER STUDENT SPENDING RANGE

# In[117]:


schools_summary_df["Per Student Budget"].sort_values()
# bins on Per Student Budget: range = 655-578 = 77 
# round range up to 100/4, so 4 bins of 25 starting at 575
# 575 - 600, 600 - 625, 625 - 650, 650 - 675


# In[118]:


# schools_spending_df = schools_summary_df[[
#                                          "Average Math Score", "Average Reading Score",
#                                          "% Passing Math", "% Passing Reading",
#                                          "% Overall Passing"]]
# schools_spending_df["Per Student Budget"] = schools70_df2["Per Student Budget"]
# schools_spending_df.head()
# keep getting NaN in this new column.  Move cells up before cut and rerun.


# In[119]:


# schools_summary_df["PSB"] = schools_summary_df["Per Student Budget"].replace({'$':''}), regex = True
# schools_summary_df["PSB"] = schools_summary_df["Per Student Budget"].astype(str).astype(int)
# schools_summary_df["PSB"]

# kept getting errors with trying to change dtypes
# abandoned


# ### BINS AND LABELS SET UP

# In[120]:


bins = [ 575, 600, 625, 650, 675]
group_names = ["<$600", "$600 - $625", "$625 - $650", "$650 - $675"]


# In[121]:


# schools_summary_df["Per School Per Student Budget"] = pd.cut(schools_summary_df["Per Student Budget"], bins, labels=group_names, include_lowest=True)
# because budget columns were changed to object datatype after mapping
# to show thousands of dollars, switching back to schools70_df2
# which was created with change in dtypes
# test cut with schools70_df2


# In[122]:


# schools70_df2.head()
# CRAP!  Did it again!  Did not pay attention that I added a column to the schools70_df2
# after I did the cut!
# need to make schools70_df4 to keep from altering schools70_df2


# In[123]:


schools70_df4 = schools70_df2.copy()
# to keep from adding column to schools70_df2
# even this copy affects schools70_df2
# make a new series out of schools70_df2 column and try slice 
# test_cut = schools70_df2[["Per Student Budget"]]
# test_cut.rename(columns={"Per Student Budget" : "PSB"})
schools70_df4["PSB"] = schools70_df4["Per Student Budget"]
# schools70_df4.head()


# In[124]:


schools70_df4["per PSB"] = pd.cut(schools70_df4["PSB"], bins, labels=group_names, include_lowest=True)
# schools70_df4["Per Student Budget"]
# schools70_df4["per PSB"].value_counts()
# STILL NOT THE NEEDED RESULTS


# In[125]:


# make another dataframe like schools_summary_df except with dtypes to allow cuts
# kept getting errors when making schools_spending_df from schools_summary_df
# need to generate from pd.DataFrame


# In[126]:


per_student_budget1 = top_schools["Per Student Budget"].unique()
per_student_budget1.head()


# #### START OF PER STUDENT SPENDING DATAFRAME CREATION

# In[127]:


schools_spending_df = pd.DataFrame({
                                   "Student_Budget": per_student_budget1,
                                   "Average Math Score" : round(top_schools1["math_score"].mean(),2),
                                   "Average Reading Score" : round(top_schools1["reading_score"].mean(),2),
                                   "% Passing Math"  : round(top_school_percent_passed_math, 2),
                                   "% Passing Reading" : round(top_school_percent_passed_reading, 2),
                                   "% Overall Passing" : round(top_school_percent_passed_both, 2) 
                                  })
schools_spending_df.head()


# In[128]:


schools_spending_df["Spending Range per Student"] = pd.cut(schools_spending_df["Student_Budget"], bins, labels=group_names, include_lowest=True)
# schools70_df4["Per Student Budget"]
# schools_spending_df["Spending Range per Student"].value_counts()


# In[129]:


schools_spending_df.head()


# ### SCORES BY SCHOOL SPENDING RESULTS DATAFRAME

# In[130]:


grouped_schools_spending_df = round(schools_spending_df.groupby("Spending Range per Student").mean(),2)
grouped_schools_spending_df


# In[131]:


# FOR CONVENIENCE
# schools70_df2


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[132]:


total_students_top_schools = top_schools1["Total Students"].count()
# total_students_top_schools.head()


# In[133]:


# schools70_df2["Total Students"].value_counts()


# ### BIN SIZE DETERMINATION AND LABEL ASSIGNMENTS

# In[134]:


# school size range: from 4976 - 427 = 4549, 5000 - 400 = 4600
# roughly 3 bins of 1800: 200 + 1800 = 2000, 2000 + 1500 = 3500, 3500 + 1500 = 5000


# In[135]:


bins_school_size = [ 200, 2000, 3500, 5000]
group_names_school_size = ["Small (<1500)", "Medium (1500 - 3000)", "Large (>3000)"]


# ### INITIAL SCHOOL SIZE DATAFRAME

# In[136]:


schools_size_df = pd.DataFrame({"School Size": total_students_top_schools,
                                "Average Math Score" : round(top_schools1["math_score"].mean(),2),
                                "Average Reading Score" : round(top_schools1["reading_score"].mean(),2),
                                "% Passing Math"  : round(top_school_percent_passed_math, 2),
                                "% Passing Reading" : round(top_school_percent_passed_reading, 2),
                                "% Overall Passing" : round(top_school_percent_passed_both, 2)
                                  })
schools_size_df.head()


# In[137]:


schools_size_df["School Size Averages"] = pd.cut(schools_size_df["School Size"], bins_school_size, labels=group_names_school_size, include_lowest=True)
schools_size_df["School Size Averages"].value_counts()


# In[138]:


schools_size_df.head()


# ### FINAL SCORES BY SCHOOL SIZE RESULTS DATAFRAME 

# In[139]:


school_size_averages_df = schools_size_df[["School Size Averages", "Average Math Score",
                                          "Average Reading Score", "% Passing Math",
                                          "% Passing Reading", "% Overall Passing"]]
grouped_school_size_averages_df = round(school_size_averages_df.groupby(["School Size Averages"]).mean(),2)
grouped_school_size_averages_df


# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[140]:


top_schools_type1 = top_schools1["School Type"]
# top_schools_type1.value_counts()


# In[141]:


# INITIALLY TRIED TO USE EVERYTHING FROM PREVIOUS RESULTS DATAFRAME AND TAILOR IT TO GET ONE SCHOOL TYPE 
# TRIED TO SET UP BINNING FOR SCHOOL TYPE, BUT COULD NOT GET IT TO WORK
# EVEN AFTER I CREATED INTEGER VALUES TO REPRESENT THE OBJECT DTYPES FOR "CHARTER" AND "DISTRICT"
# REPEATED PREVIOUS SOLUTION DATAFRAME FOR CONVENIENCE 
# school_size_averages_df.head()


# In[142]:


schools70_df5 = schools70_df2.copy()
# schools70_df5.head()


# In[143]:


# school_size_averages_df.count()


# In[144]:


# print(schools70_df5["School Type"][39165])


# In[145]:


# print(schools70_df5["School Type"][29117])


# In[146]:


schools70_type = [schools70_df5["School Type"]]


# In[147]:


# print(schools70_type)


# In[148]:


# type(schools70_type)


# In[149]:


schools70_df5["School Type Des"] = schools70_df5["School Type"]
# schools70_df5.head().set_index("School Type")


# In[150]:


schools70_df5["School Type Des"].replace({"District":969, "Charter": 970}, inplace = True)
# schools70_df5.set_index("School Type Des").head()


# In[151]:


# schools70_df5["School Type Des"].dtype


# In[152]:


# schools70_df5.head()


# In[153]:


schools_type_group_test_df = schools70_df5.groupby(["School Type Des", "School Type"])[["math_score", "reading_score"]].mean()
# schools_type_group_test_df


# In[154]:


# FIRST INDICATION THAT ONLY A GROUPBY WAS NEEDED WITHOUT THE BINNING
schools_type_group_test_df = schools70_df5.groupby("School Type")[["math_score", "reading_score"]].mean()
schools_type_group_test_df


# In[155]:


# schools_type_group_test1_df = schools70_df5.groupby("School Type")[["Average Math Score":"math_score"],
#                                                                     ["Average Reading Score":"reading_score"]].mean()
# schools_type_group_test1_df


# In[156]:


group_test1 = schools70_df5.groupby("School Type").groups
# print(group_test1)


# ### START OF MAKING NEW DATAFRAME TO CLEAR GROUPBY KEY "SCHOOL NAME"

# In[157]:


schools70_df6 = schools70_df1.copy()
schools70_df6.head()


# In[158]:


# previous groupby["School Name"] keeps this index persistent even if the groupby did not work
# See total_schools and total_schools1 dataframes.  They did not work to group anything, but the key used,
# "School Name" stayed persistent throughout all the rest of the dataframes.
# This prevented the groupby["School Type"] from working as it should, and it made me go down rabbit holes
# trying to bin and cut the two strings for school type.  I converted the object dtypes to int64 by
# making each string to a numberic value (969, 970) to see I could get the bin and cut to work.
# Ultimately, I had to completely rebuild a new dataframe in order to use groupby against "School Type"
# This is the start of the rebuild.
# schools70_df6.head()


# ### NEW GROUPBY KEY "SCHOOL TYPE"

# In[159]:


schools70_df6["School Type"] = schools70_df6["type"]
schools70_df6.drop(columns=["type"])
# AFTER INITIALLY USED GROUPBY KEY "TYPE", IT WAS HARD TO CLEAR IT OUT OF THE DATAFRAME.
# I LEFT IT IN RATHER THAN REDO EVERYTHING AND JUST MOVED THIS CODE BLOCK UP.
schools70_df6.head()


# In[160]:


group_type_df6 = schools70_df6.groupby(["School Type"])
# group_type_df6.nunique()


# In[161]:


# group_type_df6.dtypes


# ### START OF CALCULATIONS RERUN WITH NEW GROUPBY KEY "SCHOOL TYPE"

# In[162]:


ave_math = round(group_type_df6["math_score"].mean(),2)
ave_math


# In[163]:


ave_read = round(group_type_df6["reading_score"].mean(),2)
ave_read


# In[164]:


schools70_df6["Pass Math"] = schools70_df6["math_score"] >= 70
schools70_df6["Pass Read"] = schools70_df6["reading_score"] >= 70
schools70_df6["Pass Both"] = (schools70_df6["reading_score"] >= 70) & (schools70_df6["math_score"] >= 70)
# THESE WERE CREATED TO CLEAR ERROR MESSAGE WHERE >= COULD NOT BE RECOGNIZED BETWEEN GROUPBY SERIES AND INT
# schools70_df6.head()


# In[165]:


# schools70_df6.rename(columns = {"type" : "School Type"})
# schools70_df6.columns


# ### CONTINUTATION OF CALCULATIONS AFTER USING NEW GROUPBY KEY "SCHOOL TYPE"

# In[166]:


pass_math_df6 = group_type_df6["Pass Math"].sum()
pass_math_df6


# In[167]:


pass_read_df6 = group_type_df6["Pass Read"].sum()
pass_read_df6


# In[168]:


pass_both_df6 = group_type_df6["Pass Both"].sum()
pass_both_df6


# In[169]:


per_math = round(((pass_math_df6 / (group_type_df6["Student ID"].count())) * 100), 2)
per_math


# In[170]:


per_read = round(((pass_read_df6 / (group_type_df6["Student ID"].count())) * 100), 2)
per_read


# In[171]:


per_both = round(((pass_both_df6 / (group_type_df6["Student ID"].count())) * 100), 2)
per_both


# In[172]:


# "School Type": group_type_df6["type"].unique(),


# In[173]:


# SUCCESS!!!


# ### SCORES BY SCHOOL TYPE RESULTS DATAFRAME

# In[174]:


type_summary_df = pd.DataFrame({
                                "Average Math Score": ave_math,
                                "Average Reading Score": ave_read,
                                "% Passing Math": per_math,
                                "% Passing Reading": per_read,
                                "% Overall Passing": per_both
                               })
type_summary_df.head()


# In[ ]:




