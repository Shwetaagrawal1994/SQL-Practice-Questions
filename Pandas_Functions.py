# ###################
#  SCRIPT FOR PANDAS
#  Date - 19th Feb 2025

import pandas as pd
import numpy as np
import os

# READ DATA
df = pd.read_csv(os.getcwd() + "/mckinsey.csv")
copy_df = df
movies = pd.read_csv(os.getcwd() + "/movies.csv")
director = pd.read_csv(os.getcwd() + "/directors.csv")
pfizer = pd.read_csv(os.getcwd() + "/Pfizer_1.csv")

# VIEW DATAFRAME
print(df)
print(df.head(10)) # without 10, the default value is 5
print(df.tail(10))
print(df.keys)

# # SHAPE OF DATAFRAME
print(df.shape)

# # ACCESS PARTICULAR COLUMN/S --- where to keep?
print(df['country'].head())
print(df[['country']].head())
print(df[['country', 'life_exp']].head()) # Note that df['country', 'life_exp'] will throw an error

# # CHECK TYPE
print(type(df))  # returns = <class 'pandas.core.frame.DataFrame'> which means its a dataframe
print(type(df['country']))

# # DATATYPE OF df ALONG WITH NUMBER OF NULL VALUES
print(df.info())

# # CREATE CUSTOM df
# Below is the row oriented approach
print(pd.DataFrame([['A', 70, 40], ['B', 60, 30]], columns= ['Name', 'Weight', 'Age']))
# Below is the column oriented approach
print(pd.DataFrame({'Name':['A', 'B'], 'Weight':[70, 60], 'Age':[40, 30]}))

# ########## ---- SELECTION ------ ############
print("# ########## ---- SELECTION ------ ############")
# # EXPLICT AND IMPLICIT INDICES
# ---- Explict indices : Labels (Keys/ Column names) and used with loc
print(">"*30, "Explict indices", ">"*30)
# Access Single row
print(df.loc[1]) # or print(df.loc[1, :]) 
# Access Multiple rows
print(df.loc[3:13]) # NOTE - Both bounds are included
# Access Columns by skipping rows
print(df.loc[1:10:2])
# Access non consecutive rows
print(df.loc[[1, 30, 40], :])

# Access Single Column
print(df['country'])
print(df.loc[:, 'country'])
# Access Multiple Columns
print(df.loc[:, 'country':'continent'])
# Access non consecutive Columns
print(df.loc[:, ['country','continent']])

# Access both rows and Columns together
print(df.loc[1:30, 'country': 'life_exp']) # NOTE - df.loc[1:5, ['country', 'life_exp']] - This will throw error as ['country'] is not an index

# ---- Implicit indices : Integer based positions and used with iloc
print(">"*30, "Implicit indices", ">"*30)
# Access Single row
print(df.iloc[1]) # or print(df.iloc[1,:])
# Access Multiple rows
print(df.iloc[3:13])
print(df.iloc[:13])
print(df.iloc[1600:])
# Access non consecutive rows
print(df.iloc[[3,13,10]]) # NOTE - df.iloc[3,13,10] - This will throw error. Pass non consecutive numbers as list of index
# Negative Indexing
print(df.iloc[-1]) # NOTE - df.loc[-1] - This will throw error because loc workd with labels and not position
# Access Columns by skipping rows
print(df.iloc[1:10:2])

# Access Single Column
print(df.iloc[:,1])
# Access Multiple Columns
print(df.iloc[:,1:5])
# Access non consecutive Columns
print(df.iloc[:,[1,5]])

# Access both rows and Columns together
print(df.iloc[5, 4])
print(df.iloc[1:5, 2:4])
# Access specific rows and Columns together
print(df.iloc[[1, 300, 500], [2, 5, 4]])

# ########## ---- BASIC OPERATIONS ON COLUMNS ------ ############
print("# ########## ---- BASIC OPERATIONS ON COLUMNS ------ ############")
# # COLUMN NAMES
print(df.columns) # returns column names as list
print(df.keys())

# # RENAME COLUMNS
print(df.rename(columns = {'country' : 'Country', 'continent': 'Continent'}))
print(df.rename({'country' : 'Country', 'continent': 'Continent'}, axis = 1, inplace = True))
# print(df.rename({'country' : 'Country', 'continent': 'Continent'}, axis = 1))

# # ADD COLUMNS
# First way - Create a column using existing columns
df['Yr+7'] = df['year'] + 7
df['gdp'] = df['gdp_cap']*df['population']

# Second way - Create a column using new values
df['new_index'] = [i for i in range(df.shape[0])]
print(df)

# # DROP COLUMNS
# ---- Drop single column
# First way : Drop single column by using axis
df.drop('new_index', axis = 1)

# Second way : Drop single column by using columns
df.drop(columns = 'new_index', inplace = True)

# ---- Drop multiple columns
# First way : Drop single column by using axis
df.drop(['Yr+7', 'gdp'], axis = 1)

# Second way : Drop single column by using columns
df.drop(columns = ['Yr+7', 'gdp'], inplace = True)
print(df)

# # UNIQUE VALUE OF A COLUMN
print(df['Country'].unique()) # returns the list of unique values
print(df['Country'].value_counts())

# ########## ---- BASIC OPERATIONS ON ROWS ------ ############
print("# ########## ---- BASIC OPERATIONS ON ROWS ------ ############")
# # VIEW ROW NAMES
print(df.index.values)

# # RENAME ROW
#  First way : Rename with new names
copy_df.index = [i for i in range(1, copy_df.shape[0] + 1)]
print(copy_df)
# Second way : Rename with existing columns i.e., set one column as row index
copy_df = df.set_index("Country")
print(copy_df)
print(copy_df.loc['Zimbabwe'])
# # change row labels type
# copy_df.index = np.arrange(1, copy_df.shape[0]+1, dtype = float)
# print(df)

# Second way : To have original row names
copy_df.reset_index(drop= True, inplace= True)
print(copy_df)

# # ADD ROWS
# First way : Using dict
new_row = {'Country': 'India', 'year':2000, 'life_exp':37, 'population':1350000, 'gdp_cap': 300}
print(df._append(new_row, ignore_index = True) )
''' NOTE - 1. df.append(df2) - will not work 
           2. Parameter ignore_index = True is required when appending dict to a dataframe
'''
# Second way : Using list
df.iloc[len(df.index)-1] = ['India', 2000, 13500000,'Asia', 37, 900] # NOTE - Please dont use df.iloc[len(df.index)] as at that index value exists
print(df)

# # DROP ROWS
# ---- Drop single row
print(df.drop(3, axis = 0))
# ---- Drop multiple rows
print(df.drop([1, 3, 5], axis = 0))

# # UNIQUE ROWS OR CHECK FOR DUPLICATED ROWS
# ---- Check for duplicated rows
print(df.duplicated())
# ---- extract duplicated rows
print(df.loc[df.duplicated()])
# ---- drop duplicated rows
print(df.drop_duplicates())
print(df.drop_duplicates(keep='first')) # NOTE - keep='first' means keeps first one
print(df.drop_duplicates(keep='last')) # NOTE - keep='last' means keeps last one
print(df.drop_duplicates(keep=False)) # NOTE - keep=False means all duplicated are dropped
print(df.drop_duplicates(subset=['Country'], keep='first')) # NOTE - subset agrument is used to look for duplicacy only for a few columns
print(df.drop_duplicates(subset=['Country', 'Continent'], keep='first')) # NOTE - subset agrument is used to look for duplicacy only for a few columns

# ########## ---- BASIC BUILT IN OPERATIONS ------ ############
print("# ########## ---- BASIC BUILT IN OPERATIONS ------ ############")
print(df['life_exp'].mean())
print(df['Country'].count())

# ########## ---- SORTING------ ############
print("# ########## ---- SORTING ------ ############")
# ---- Sort based on single column
print(df.sort_values(['life_exp'])) # NOTE - default sorting is by ascending order
print(df.sort_values(['life_exp'], ascending=False))
# ---- Sort based on multiple columns
print(df.sort_values(['year', 'life_exp']))
print(df.sort_values(['life_exp', 'life_exp'], ascending=[False, True]))

# ########## ---- CONCATE DATAFRAMES ------ ############
print("# ########## ---- CONCATE DATAFRAMES ------ ############") 
# ---- Create new dataframe to clearly show concatenate function of pandas
df = pd.DataFrame({"userID":[1,2,3], "Name": ['Ada', 'Santiago', 'Raul']})
df2 = pd.DataFrame({"userID":[1,3,3], "Height":[168, 170, 175]})
print(df, df2)
# ---- Concatenate Vertically 
print(pd.concat([df, df2]))
print(pd.concat([df, df2], ignore_index=True))
# ---- Concatenate Horizontally 
print(pd.concat([df, df2]))
print(pd.concat([df, df2], axis=1))

# ########## ---- MERGE DATAFRAMES ------ ############
print("# ########## ---- MERGE DATAFRAMES ------ ############") 
print(df.merge(df2, on = 'userID'))
print(df.merge(df2, on = 'userID', how='outer'))
print(df.merge(df2, on = 'userID', how='right'))

# ---- how to merge when column names are different
print(df.rename(columns={'userID':'ID'}, inplace= True))
print(df.merge(df2, left_on = 'ID', right_on= 'userID'))

# ###################################################################################################
# ----------------------------- USING ANOTHER DATA SET ----------------------------------------------
print(movies.head())
print(director.head())
# NOTE - We can see that both data has unnamed column and we want to remove this while reading the data
movies = pd.read_csv(os.getcwd() + "/movies.csv", index_col=0)
director = pd.read_csv(os.getcwd() + "/directors.csv", index_col=0)
print(movies.head())
print(director.head())

# Q. How do we get the number of unique directors in movie & dirctor dataset?
print(movies['director_id'].nunique())
print(director['id'].nunique())
# Q. How do we check if all director id from movie data is present in the director dataset?
print(movies['director_id'].isin(director['id']))
''' NOTE - 1. Difference between in and isin is that in works for one element and isin works for all the values in the column
            2. isin is like a boolean mask
            3. isin returns df similar to orginal df
'''
# Q. Shortcut for the above question 
print(np.all(movies['director_id'].isin(director['id'])))
# Q. Merge both dataset to create a single dataset
print(movies.merge(director, how='left', left_on='director_id', right_on='id'))
# NOTE - The merged out has id_x and id_y columns because both data has id column. Therefore, use dop function to remove one of 2 columns

# ########## ---- SUMMARIZE ------ ############
print(director.describe())
print(director.describe(include=object))

# ########## ---- ROUND OFF ------ ############
print(movies['revenue'].round(7))

# ########## ---- BOOLEAN MASKING ------ ############
# ---- With single condition
# First way : Using loc
print(movies['vote_average']>7)

# Second way : Without using loc
print(movies.loc[movies['vote_average']>7])

#  ---- With single condition and specific columns
print(movies.loc[movies['vote_average']>7, ['title', 'director_id']])

# ---- With multiple conditions with and operator
print(movies.loc[(movies['vote_average']>7) & (movies['year']>=2015) ]) 
# NOTE - This code does not work without () i.e., print(movies.loc[movies['vote_average']>7 & movies['year']>=2015 ])

# ---- With multiple conditions with or operator
print(movies.loc[(movies['day']=='Friday') | (movies['day']=='Monday') ] ) 

# Q. List of movies released in 2020
print(movies.loc[movies['year']== 2015, ['title']])

# ########## ---- APPLY ------ ############
# ---- Apply with single column
# Convert gender column to 0 and 1 in director table
def encode(data):
    if data == 'Male':
        return 0
    else:
        return 1

director['gender_flag'] = director['gender'].apply(encode)
print(director)

# ---- Apply with multiple columns
# across column
print(movies[['revenue', 'budget']].apply(np.sum))
# across row
print(movies[['revenue', 'budget']].apply(np.sum, axis = 1))

# ########## ---- GROUPINGS ------ ############
# ---- Create groups
print(movies.groupby('year')) # NOTE - output is <pandas.core.groupby.generic.DataFrameGroupBy object at 0x107c01d00>
print(movies.groupby('day').groups) # how to interpret this?

# ---- Count groups
print(movies.groupby('year').ngroups) # explore ngroup role ?. The one used in this is ngroups

# ---- Select particular group
print(movies.groupby('year').get_group(2015))

# ---- Group based aggregates
# Count overall rows of a filtered data
print(movies.loc[movies['year']== 2015, ['title']].count())
# Aggregation based on single column
print(movies.groupby('year')['id'].count())
# Aggregation based on multiple columns
print(movies.groupby(['title'])['year'].aggregate(['min', 'max']))
# Aggregation with sort
print(movies.groupby('year')['id'].count().sort_values(ascending= False))

# ---- Group based filtering
# Long way
part_movie = movies.groupby(['title'])['year'].max().reset_index()
print(part_movie)
names = part_movie.loc[part_movie['year']>= 2015, 'title']
print(movies.loc[movies['title'].isin(names)])

# Short way
print(movies.groupby(['title']).filter(lambda x:x['year'].max() >= 2015) )

# ---- Group based apply
def func(x):
    x['risky'] = x['budget'] - x['revenue'].mean() >= 0
    return x
risky_movies = movies.groupby('title').apply(func)
print(risky_movies.loc[risky_movies['risky']])
# print(movies.groupby('title').apply(func))

# ########## ---- MULTI - INDEXING ------ ############
multi_index_data = (movies.groupby(['title'])[['year', 'day']].aggregate({'year':['min', 'max'], 'day':['count']}))
print(multi_index_data)

print(multi_index_data.columns)
print(multi_index_data['year'])

# Convert back to data frame with only one level
multi_index_data.columns = ['_'.join(col) for col in multi_index_data.columns]
print(multi_index_data.reset_index()) # to convert row labels into a column

# ###################################################################################################
# ----------------------------- USING ANOTHER DATA SET ----------------------------------------------
print(pfizer.head())

# ########## ---- RESTRUCTURE DATA ------ ############
# ---- melt data (Wide to long format)
print(pd.melt(pfizer, id_vars=['Date', 'Drug_Name', 'Parameter']))
# ---- melt data (Wide to long format) along with rename new columns
data_melt = pd.melt(pfizer, id_vars=['Date', 'Drug_Name', 'Parameter'], var_name='time', value_name='reading')
print(data_melt)

# ---- Pivot data (long format to Wide) --- how is pivot and pivot table different????
print(data_melt.pivot(index= ['Date', 'Drug_Name', 'Parameter'], columns = 'time', values= 'reading')) 
# NOTE - This will return wide data with multiple indices. To get ride of multiple indices, use below code:
print(data_melt.pivot(index= ['Date', 'Drug_Name', 'Parameter'], columns = 'time', values= 'reading').reset_index()) 

# ---- Restructure melted data to remove multiple rows representing single experiment i.e., group rows
print(data_melt.pivot(index= ['Date', 'time', 'Drug_Name'], columns= 'Parameter', values= 'reading'))
# if remove multi- index
data_tidy = data_melt.pivot(index= ['Date', 'time', 'Drug_Name'], columns= 'Parameter', values= 'reading').reset_index()
print(data_tidy)
# NOTE - index columns appears with a 'Parameter' name which can be reanmed by using below code
data_tidy.columns.name = 'None' 

# ---- Pivot table to summarize data
# print(pd.pivot_table) 

# ########## ---- MISSING DATA ------ ############
# NOTE - 2 TYPES OF MISSING - None and NaN (stands for Not a Number)
print(type(None))
print(type(np.nan))
# ---- Storage of missing values in pandas
print(pd.Series([1, np.nan, 2, None]))
print(pd.Series(['1', np.nan, '2', None]))
print(pd.Series(['1', 'np.nan', '2', np.nan]))

# ---- Count missing values across column
print(pfizer.isna().head())
print(pfizer.isnull().head())

print(pfizer.isna().sum())

# ---- Count missing values across row
print(pfizer.isna().sum(axis= 1))
print(pfizer.isnull().any( axis= 1))

# ---- Drop missing rows
print(pfizer.dropna())

# ---- Drop missing columns
print(pfizer.dropna(axis= 1))

# ---- Fill missing rows
print(pfizer.fillna(0))

# ---- Fill specific column with missing value
print(pfizer['2:30:00'].fillna(0))

# ---- Fill missing rows with mean
print(pfizer['2:30:00'].fillna(pfizer['2:30:00'].mean()))

# ---- Fill missing rows with mean of specific column  with another column
print(pfizer['3:30:00'].fillna(pfizer['6:30:00']))

# ---- Fill missing rows with mean of each column in their respective columns
# def mean_temp(x):
#     x['Temp_avg'] = x['Temperature'].mean()
#     return x

# ########## ---- BINNING DATA ------ ############
temp_points = [5, 20, 35, 50, 60]
temp_labels = ['low','medium','high','very_high'] 
data_tidy['Temp_category'] = pd.cut(data_tidy['Temperature'], bins = temp_points, labels= temp_labels)
print(data_tidy)

# ########## ---- STRING OPERATION ------ ############
# ---- Filter rows with the name which contains  hydrochloride
print(data_tidy.loc[data_tidy['Drug_Name'].str.contains('hydrochloride')])

# ---- Split date column by -
print(data_tidy['Date'].str.split('-'))

# ---- Extract year from the above splitted date 
print(data_tidy['Date'].str.split('-').apply(lambda x:x[2]))

# ---- Concatenate 2 columns
data_tidy['timestamp'] = data_tidy['Date'] + " " + data_tidy['time']
print(data_tidy)

# ########## ---- DATE TIME HANDLING ------ ############
print(pd.to_datetime(data_tidy['timestamp']))