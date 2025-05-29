import pandas as pd
import numpy as np

# breakpoint()
# Q1. Creating the dataframe from a Dictionary
print(">"*20, "Q1", ">"*20)
print(pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}))

# Q2. Craete dataframe with specified index labels
print(">"*20, "Q2", ">"*20)
exam_data  = {'name': ['Anastasia', 'Dima', 'Bassi', 'Givonnale', 'Davide', 'Carlo', 'Funda', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
        'time': ['3/11/2000', '3/12/2000', '3/13/2000', '3/11/2000', '3/12/2000', '3/13/2000', '3/11/2000', '3/12/2000', '3/13/2000', '3/11/2000'],
        'comments': [' #fgfk', '@fdgfj ', '@fd34 nknfd#', 'JFR #nnames', '344nfdj @jfj', '3223%^&@', '*kjdhDFF#  ', '#dffd @ere33', '--gfgfgf--', '  ']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print(df)

# Q3. dataframe Basic Summary Information
print(">"*20, "Q3", ">"*20)
print(df.info())

# Q4. Selecting the First 3 Rows
print(">"*20, "Q4", ">"*20)
print(df.iloc[:3,])
print(df.iloc[:3])
print(df.iloc[3]) # this will return series and not dataframe. check the type using - print(type(df.iloc[3]))

# Q5. Selecting 'name' and 'score' Columns
print(">"*20, "Q5", ">"*20)
print(df.loc[:, ['name', 'score']])
print(df[['name', 'score']])
breakpoint()
# Q6. Selecting Specific Columns and Rows
print(">"*20, "Q6", ">"*20)
print(df.iloc[[1, 3, 5, 6], [1, 3]])

# Q7. Selecting Rows Where Attempts > 2
print(">"*20, "Q7", ">"*20)
print(df.loc[df['attempts']>2])
print(df[df['attempts'] > 2])

# Q8.  Counting Rows and Columns
print(">"*20, "Q8", ">"*20)
print('rows', df.shape[0])
print('rows', len(df.axes[0]))
print('columns', df.shape[1])
print('columns', len(df.axes[1]))

# Q9. Selecting Rows with Missing Score
print(">"*20, "Q9", ">"*20)
print(df[df['score'].isna()])
print(df[df['score'].isnull()])

# Q10. Selecting Rows Where Score is Between 15 and 20
print(">"*20, "Q10", ">"*20)
print(df.loc[(df['score']>=15) | (df['score']>=20)])
print(df[(df['score']>=15) | (df['score']>=20)])
print(df[df['score'].between(15, 20)])

# Q11. Selecting Rows with Attempts < 2 and Score > 15
print(">"*20, "Q11", ">"*20)
print(df[(df['attempts']<2) & (df['score']>15)])
print(df.loc[(df['attempts']<2) & (df['score']>15)])

# Q12. Changing the Score in a Specific Row (i.e., row 'd' to 11.5)
print(">"*20, "Q12", ">"*20)
df.loc['d', 'score']=11.5
print(df)

# Q13. Summing Examination Attempts
print(">"*20, "Q13", ">"*20)
print(df['attempts'].sum())
      
# Q14. Calculating the Mean of Scores)
print(">"*20, "Q14", ">"*20)
print(df['score'].mean())

# Q15. Append a new row 'k' to data frame with values for each column. Then delete the new row and return the original dataframe
print(">"*20, "Q15", ">"*20)
# ---- Method 1 - for adding a row
df.loc[len(df.index)+1] = ['Suresh',15.5, 1, 'yes', '3/13/2000', 'drrgrrgf']
df.index.values[len(df.index)-1] = 'k'
# ---- Method 2 - for adding a row
df.loc['l'] = [1, 'Suresh', 'yes', 15.5, '3/13/2000', 'drrgrrgf']
# ---- Method 1 - for deleting a row
df.drop('k', axis=0, inplace=True)
# ---- Method 2 - for deleting a row
df = df.drop('l')
print(df)

# Q16. Sort the dataframe first by 'name' in descending order, then by 'score' in ascending order
print(">"*20, "Q16", ">"*20)
print(df.sort_values(['name', 'score'], ascending=[False, True]))

# Q17. Replace the 'qualify' column containing the values 'yes' and 'no' with True and False
print(">"*20, "Q17", ">"*20)
# ---- Method 1 
def replace_func(data):
    if data == 'yes':
        return True
    else:
        return False
print(df['qualify'].apply(replace_func))
# ---- Method 2
print(df['qualify'].map({'yes': True, 'no': False}))
# NOTE - For inplace change, use below code:
# df['qualify'] = df['qualify'].map({'yes': True, 'no': False})
# df['qualify'] = df['qualify'].apply(replace_func)
print(df) 

# Q18. Change the name 'James' to 'Suresh' in name column 
print(">"*20, "Q18", ">"*20)
# ---- Method 1 
print(df['name'].map({'James': 'Suresh'}))
# ---- Method 2
print(df['name'].replace('James', 'Suresh'))
# ---- Method 3
print(df['name'].apply(lambda x: 'Suresh' if x == 'James' else x))
# ---- Method 4
print(np.where(df['name'] == 'James', 'Suresh', df['name'])) # this returns the list and needs to be assigned to a particular columns

# Q19. Delete the 'attempts' column from the dataframe
print(">"*20, "Q19", ">"*20)
print(df.drop(['attempts'], axis = 1 ))

# Q20. Insert a new column in existing column and new values
print(">"*20, "Q20", ">"*20)
# ---- Method 1 
df['city'] = ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']
# ---- Method 2
df['wealth'] = list(np.random.randint(1000, 2000, size=df.shape[0]))
# ---- Method 3
df['wealth'] = df['wealth']+0.00344453
# ---- Method 4
df['num'] = [i for i in range(1, df.shape[0]+1)]
print(df)

# Q21. Iterating Over dataframe Rows along with its index
print(">"*20, "Q21", ">"*20)
for index, row in df.iterrows():
    print(index, row)

# Q22. Getting List of Column Headers
print(">"*20, "Q22", ">"*20)
# ---- Method 1 
print(list(df.columns))
# ---- Method 2
print(list(df.keys()))

# Q23. Renaming dataframe Columns
print(">"*20, "Q23", ">"*20)
print(df.rename(columns= {'num':'numbers'}))
print(df.rename({'num':'numbers'}, axis=1))

# Q24. Selecting Rows Based on scores of Value 8
print(">"*20, "Q24", ">"*20)
# ---- Method 1 
print(df.loc[df['score'] == 8])
# ---- Method 2
print(df[df['score'] == 8])

# Q25. Altering order of dataframe Columns
print(">"*20, "Q25", ">"*20)
print(df[[ 'num', 'attempts', 'qualify','name', 'score', 'city' ]])

# Q26. Add One Row to the dataframe
print(">"*20, "Q26", ">"*20)
print(df)
# ---- Method 1 
df.loc[len(df.index)+1] = ['Luz',15.5, 1, 'yes', '3/13/2000','66 jjjja', 'Santa clara',6343.34892, 11 ]
print(df)
# ---- Method 2
df2 = {'name': 'Luz', 'score': 15.5, 'attempts': 1, 'qualify':'yes', 'num': 11, 'city':'Seatle', 'time':'3/13/2000'}
print(df._append(df2, ignore_index=True))

# Q27. Write the dataframe to CSV file using tab separator
print(">"*20, "Q27", ">"*20)
df.to_csv('new_file.csv', sep='\t', index=False)

# Q28. City Wise Count
print(">"*20, "Q28", ">"*20)
print(df.groupby('city')['name'].count())
''' NOTE - Difference between size() and count() functions: 
        size() - Counts total number of rows in each group. Includes NaN values (doesn’t care if data is missing). Counts all rows, whether or not they have missing data!
        count() - Counts non-NaN values for each column separately. If a value is NaN, it is not counted. Only valid (non-missing) entries are counted!
'''

# Q29. Delete Rows by Column Value
print(">"*20, "Q29", ">"*20)
print(df[df['num'] != 5])

# Q30. Widen Output Display
print(">"*20, "Q30", ">"*20) # -----?

# Q31. Select Row by Integer Index
print(">"*20, "Q31", ">"*20)
print(df.iloc[4, :])

# Q32. Replace NaN with Zeros
print(">"*20, "Q32", ">"*20)
print(df.fillna(0))

# Q33. Convert Index to Column
print(">"*20, "Q33", ">"*20)
df['index'] = list(df.index.values)
print(df)
print(df.reset_index(level=0)) # what does this means------?

# Q34. Set a given value for particular cell in the dataframe
print(">"*20, "Q34", ">"*20)
# NOTE - df._set_value(8.0, 'score', 10.2) # It was deprecated and removed in latest pandas versions. You should not use private methods in production code.
# ---- Method 1 
df.loc['i', 'score'] = 10.2
# ---- Method 2
df.at['i', 'score'] = 10.2
print(df)

# Q35. Count NaN Values - Number of NaN values in one or more columns
print(">"*20, "Q35", ">"*20)
# ---- Method 1 
print(df.isna().sum()) # difference betwen sum() and any() ----?
print(df.isna().any())
# ---- Method 2
print(df.isnull().sum())
print(df.isnull().any())

print(df.isnull().values.sum()) # check output of this -----?

# Q36. drop a list of rows from a specified dataframe
print(">"*20, "Q36", ">"*20)
print(df.drop(df.index[3:5], axis = 0))

# Q37. Reset dataframe Index
print(">"*20, "Q37", ">"*20)
print(df.reset_index())

# Q38. Create sample from a dataframe by Ratio
print(">"*20, "Q38", ">"*20)
part_70 = df.sample(frac=0.7,random_state=10) # what is meant by random_state -----?
print(part_70)
print(df.drop(part_70.index))

# Q39. Combine Two Series
print(">"*20, "Q39", ">"*20)
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
s2 = pd.Series(['10', '20', 'php', '30.12', '40'])
print(pd.concat([s1, s2], axis=1))

# Q40. Shuffle dataframe Rows
print(">"*20, "Q40", ">"*20)
print(df.sample(frac=1))

# Q41. Convert dataframe column type from string to datetime
print(">"*20, "Q41", ">"*20)
print(pd.to_datetime(df['time']))
'''NOTE - pd.to_datetime() expects a Series — not a full dataframe.
If you pass a full dataframe ([['time']]), it still works, but it internally picks the first column and converts it'''

# Q42. rename a specific column name in the dataframe
print(">"*20, "Q42", ">"*20)
print(df.rename({'time': 'datetime'},axis = 1))

# Q43. get a list of a specified column of the dataframe
print(">"*20, "Q43", ">"*20)
print(list(df['city']))
print(df["city"].tolist())

# Q44. create the dataframe from a Numpy array and specify the index column and column header
print(">"*20, "Q44", ">"*20)
dtype = [('Column1','int32'), ('Column2','float32'), ('Column3','float32')]
values = np.zeros(15, dtype=dtype)
index = ['Index'+str(i) for i in range(1, len(values)+1)]
df2 = pd.DataFrame(values, index=index)
print(df2)

# Q45. find the row for where the value of a given column is maximum
print(">"*20, "Q45", ">"*20)
print(df['attempts'].argmax())
print(df['score'].argmax())

# Q46. Check whether a given column is present in the dataframe or not
print(">"*20, "Q46", ">"*20)
print('col4' in df.columns)

# Q47. Get the specified row value of the dataframe
print(">"*20, "Q47", ">"*20)
print(df.iloc[4])

# Q48. Get the datatypes of columns of the dataframe
print(">"*20, "Q48", ">"*20)
print(df.dtypes)

# Q49. Append Data to Empty dataframe
print(">"*20, "Q49", ">"*20)
empty_data = pd.DataFrame()
print(empty_data._append(df))

# Q50. Sort dataframe by Multiple Columns
print(">"*20, "Q50", ">"*20)
print(df.sort_values(['name', 'score'], ascending=[True, False]))

# Q51. Convert the datatype of a given column (to float)
print(">"*20, "Q51", ">"*20)
print(df['score'].astype(float))

# Q52. Remove infinite values from the dataframe
print(">"*20, "Q52", ">"*20)
df_clean = df.replace([np.inf, -np.inf], np.nan)
print(df_clean.dropna())

# Q53. Insert a given column at a specific column index in the dataframe
print(">"*20, "Q53", ">"*20)
df.insert(loc=2, column='salary', value=10000)
''' NOTE - Above line is different from df['salary'] = 10000 because this will add new column at the end. However, above code will add new column at the second position'''
print(df)

# Q54. Convert List of Lists into dataframe
print(">"*20, "Q54", ">"*20)
my_lists = [['col1', 'col2'], [2, 4], [1, 3]]
headers = my_lists.pop(0) # sets the headers as list
print(pd.DataFrame(my_lists, columns = headers))

# Q55. Group by the first column and get second column as lists in rows
print(">"*20, "Q55", ">"*20)
df2 = pd.DataFrame( {'col1':['C1','C1','C2','C2','C2','C3','C2'], 'col2':[1,2,3,3,4,6,5]})
print(df2.groupby('col1')['col2'].apply(list))

# Q56. Get column index from column name of the dataframe
print(">"*20, "Q56", ">"*20)
print(list(df.columns).index("salary"))
print(df.columns.get_loc('salary'))

# Q57. Count Number of Columns
print(">"*20, "Q57", ">"*20)
print(len(df.columns))

# Q58. Select all columns, except one given column in the dataframe
print(">"*20, "Q58", ">"*20)
print(df.loc[:, df.columns != 'salary'])

# Q59. Get first n records of the dataframe
print(">"*20, "Q59", ">"*20)
print(df.head(3))

# Q60. Get Last n Records
print(">"*20, "Q60", ">"*20)
print(df.tail(3))

# Q61. get topmost n records within each group of the dataframe
print(">"*20, "Q61", ">"*20)
df['score'] = df['score'].astype(float)
print(df.nlargest(3, 'salary'))
print(df.nlargest(3, 'score'))

# Q62. Remove first n rows of the dataframe
print(">"*20, "Q62", ">"*20)
print(df.iloc[3:])

# Q63. Remove first n rows of the dataframe
print(">"*20, "Q63", ">"*20)
print(df.iloc[:3])

# Q64. Add Prefix or Suffix to All Columns
print(">"*20, "Q64", ">"*20)
print(df['name'] + " AB" )
print( "AB " + df['name'] )
print(df.add_suffix("_1")) # This will add suffix to the column names
print(df.add_prefix("A_")) # This will add prefix to the column names

# Q65. Reverse Order of dataframe (Rows, Columns)
print(">"*20, "Q65", ">"*20)
print(df.loc[:, ::-1])
print(df.loc[::-1])

# Q66. Select columns by data type 
print(">"*20, "Q66", ">"*20)
print(df.select_dtypes(include = "number"))
print(df.select_dtypes(include = "object"))

# Q67. Split dataframe into Two Random Subsets
print(">"*20, "Q67", ">"*20)
df1 = df.sample(frac = 0.6)
print(df1)
print(df.drop(df1.index))

# Q68. rename all columns with the same pattern of the dataframe i.e., remove trailing (at the end) whitesapce and convert to lowercase of the columns name
print(">"*20, "Q68", ">"*20)
print(df.columns.str.lower().str.rstrip())

# Q69. merge datasets and check uniqueness i.e., check if merge keys are unique in both left and right datasets, in left dataset and in right dataset
# df2 = df
# df1 = df2.copy(deep = True)
# df2 = df2.drop(['a','b'], axis=0)
# df1 = df1.drop([2],)
# print(pd.merge(df, df1, validate = "one_to_one"))
# print(pd.merge(df, df1, validate = "one_to_many"))
# print(pd.merge(df, df1, validate = "many_to_one"))

# Q70. Convert Continuous Column to Categorical
print(">"*20, "Q70", ">"*20)
print(pd.cut(df["score"], bins = [0, 18, 65, 99], labels = ["Poor", "Medium", "Good"]))

# Q71. display memory usage of the dataframe and every column of the dataframe
print(">"*20, "Q71", ">"*20)
print(df.info(memory_usage = "deep"))
print(df.memory_usage(deep = True))

# Q72. Combine Many Series to Create the dataframe
# Q73. Create dataframes with Mixed Values
# Q74. Fill Missing Values in Time Series Data
# Q75. Use Local Variable Within a Query
# Q76. Clean Object Column with Regex
# Q77. Get Numeric Representation from Distinct Values
# Q78. Replace Value Based on Last Largest Value
# Q79. Create dataframe from Clipboard
# Q80. Check Inequality of Two dataframes
# Q81. Get Lowest n Records Within Each Group



# ###########################################################################################
# STRING QUESTION IN PANDAS
# ###########################################################################################
import re

# Q1. Convert all the string values to upper, lower cases in a pandas series.
print(">"*20, "String in Pandas : Q1", ">"*20)
s = pd.Series(['X', 'Y', 'Z', 'Aaba', 'Baca', np.nan, 'CABA', None, 'bird', 'horse', 'dog'])
print(s)
print(s.str.upper()) # If str not used that it will throw error: AttributeError: 'Series' object has no attribute 'upper'
print(s.str.lower())
# print(s.apply(lambda x: x.lower()))
# print(list(map(lambda x: x.lower(), s)))
'''NOTE - 1. The .str accessor is a string method accessor provided by pandas.
            It lets you apply string operations element-wise to each value in a Series, only when the Series contains strings or mixed types. .str gives you access to 
            vectorized string functions (like .upper(), .lower(), .contains(), etc.) on a Series. It automatically handles NaN or None values safely (without crashing).
            2. The Series s contains np.nan and None, which are not strings: np.nan is a float (float('nan')) snd None is NoneType
            3. s.apply(lambda x: x.lower()) - Works, but slower; needs handling for NaN otherwise will throw error. However, in this case np.nan and None is present so
            when .lower() is called on these, it throws an error because: float and NoneType don't have a .lower() method.
            4. s is a pandas Series of strings (with some NaN/None). In the apply(lambda x: x.str.lower()), each x is a single string like 'X'. You are trying to call .str.lower()
            on a string, but .str is a pandas Series accessor, not a method of Python strings. Therefore use below code:'''
print(s.apply(lambda x: x.lower() if isinstance(x, str) else x)) # This version safely skips NaN/None

# Q2. Remove Whitespaces from both sides of comments column in dataframe
print(">"*20, "String in Pandas : Q2", ">"*20)
# -------- Method 1
print(df['comments'].str.strip())
print(df['comments'].str.lstrip())
print(df['comments'].str.rstrip())
# -------- Method 2
print(df['comments'].apply(lambda x: x.strip())) # This uses python method and not pandas method
# -------- Method 3
print(list(map(lambda x: x.strip(), df['comments']))) # This uses python method and not pandas method
# print(df['comments'].apply(strip())) and print(df['comments'].apply(str.strip())) #- This throws error - TypeError: unbound method str.strip() needs an argument

# Q3. Add leading zeros to the integer column like wealth in the dataframe and makes the length of the field to 14 digit
print(">"*20, "String in Pandas : Q3", ">"*20)
# -------- Method 1
print(df['wealth'].apply(lambda x: '{0:0>14}'.format(x))) # will do padding of 0
print(df['wealth'].apply(lambda x: '{0:5>14}'.format(x))) # will do padding of 5
# -------- Method 2
print(list(map(lambda x: '{0:5>14}'.format(x), df['wealth'])))
'''NOTE - 1. print('{0:5>14}'.format(df['comments'])) # TypeError: unsupported format string passed to Series.__format__
2. {0:...}: This refers to the first argument passed into .format(), i.e., x.
    0>: This is the fill and alignment specification where 0 is the fill character and > means right-align the value.
    14: This is the minimum width of the output string.
    Therefore, it converts x to a string, right-aligns it in a field of width 14, and pads it on the left with zeros if necessary.
    This function works well with character columns as well as shown in the next question'''
print(str(df['wealth']).zfill(10))

# Q4. Add leading zeros to the character column like comments in the dataframe and makes the length of the field to 10 digit
print(">"*20, "String in Pandas : Q4", ">"*20)
# -------- Method 1
print(list(map(lambda x: '{0:0>10}'.format(x), df['comments'])))
# -------- Method 2
print(df['comments'].apply(lambda x: x.zfill(10))) # this will return dataframe
# -------- Method 3
print(list(map(lambda x: x.zfill(10), df['comments']))) # this will return list
'''NOTE - .zfill(10) method to pad each string with leading zeros so that its total length is 10 characters. It's a string method: str.zfill(width). It pads a numeric
    string on the left with zeros to reach the specified width. If the string is already 10 or more characters, it's left unchanged. Assumes that each element is 
    a string (or convertible to one).
    zfill() is a string method in Python, and it cannot be directly applied to integers. To use zfill() with an integer, it must first be converted to a string.'''

# Q5. Proper case for all the string values of name column in the dataframe
print(">"*20, "String in Pandas : Q5", ">"*20)
# -------- Method 1
print(df['name'].str.capitalize())
# -------- Method 2
print(df['name'].apply(lambda x: x.capitalize()))
# -------- Method 3
print(list(map(lambda x: x.capitalize(), df['name'])))
'''NOTE - 1.Inside the lambda, x is a single string (like 'john', 'MARY', etc.). So you're just calling the regular Python string method .capitalize(). 
            x.str.capitalize() would only make sense if x were a pandas Series, not a single value.'Use .str.capitalize() when working on the whole Series directly. 
            This applies the string method to each element in the Series — it's vectorized and faster.
        2.  df['name'].apply(lambda x: x.capitalize()) - Uses Python str.capitalize() per element (slower)
            df['name'].str.capitalize() - Vectorized pandas string method (faster)
            Therefore, Use .str.capitalize() whenever possible — it's simpler and more efficient.
        3. Proper case, also known as sentence case, is a capitalization style where the first letter of the first word in a sentence is capitalized, and the 
            remaining letters are lowercase. It's distinct from title case, which capitalizes the first letter of each word in a title or heading. Therefore, this is 
            the difference between title() and capitalize() functions. capitalize() is used for proper case.'''

# Q6. Count of occurrence of a specified substring (at) in a name column
print(">"*20, "String in Pandas : Q6", ">"*20)
# -------- Method 1
# print( df['name'].count('al')) -- this shows error: TypeError: Series.count() takes 1 positional argument but 2 were given
print(df['name'].str.count("at"))
# -------- Method 2
print(df['name'].apply(lambda x: x.count("at")))
# -------- Method 3
print(list(map(lambda x: x.count("at"), df['name'])))

# Q7. Find the index of a specified substring (at) in a name column
print(">"*20, "String in Pandas : Q7", ">"*20)
# -------- Method 1
print(df['name'].str.find("at"))
# -------- Method 2
df[df['name'].str.contains('at')].index # .str.contains() is case-sensitive by default
df[df['name'].str.contains('at', case=False)].index # To make it case-insensitive
df[df['name'].str.contains('at', na=False)].index
# -------- Method 3
print(df['name'].apply(lambda x: x.find("at")))
# -------- Method 4
print(list(map(lambda x: x.find('at'), df['name'])))
''' NOTE - 1. final returns -1 when 'at' not found in that string and returns 1 which means 'at' found at index 1 in that string
    3. find function is a case sensitive search.
    5. Returns : -1 if 'c' is not found in that range otherwise The position (index) where 'at' is found within that range.
    6. df[...].index gives the index positions.''' 

# Q8. Find the index of a substring (c) of dataframe with beginning and end position
# This ques means that you want to find the index/indices where a certain substring appears in a column.
print(">"*20, "String in Pandas : Q8", ">"*20)
# -------- Method 1
print(df['name'].str.find("c", 0, 5))
# -------- Method 2
print(df['name'].apply(lambda x: x.find("c", 0, 5)))
# -------- Method 3
print(list(map(lambda x: x.find('c', 0, 5), df['name']))) 
'''NOTE - 1. x.find('c', 0, 5) - means Searches for the first occurrence of 'c' in the string x. Only looks in the substring from index 0 (inclusive) to index 5 
(exclusive). Returns: The position (index) where 'c' is found within that range and -1 if 'c' is not found in that range. Only the 6th element (index 5 in 0-based 
indexing) has a 'c' between position 0 and 5 of the string. And in that case, 'c' occurs at position 2. 
2. find() is case-sensitive by default in Python. If you want a case-insensitive search, you can modify it like this: You convert each string to lowercase before 
searching for 'c'. This will treat 'C' and 'c' the same.
3. This questions means code will look for 'c' between position 0 and 5 of the string.
4. If you want a case-insensitive search, you can modify it like this: lambda x: x.lower().find('c', 0, 5)
'''
print(lambda x: x.lower().find('c', 0, 5))

# Q9. Check whether alpha numeric values present in a comments column of the dataframe
print(">"*20, "String in Pandas : Q9", ">"*20)
# -------- Method 1
print(df['comments'].str.isalnum())
# -------- Method 2
print(df['comments'].apply(lambda x: x.isalnum())) # isalnum() returns only true and false
# -------- Method 3
print(list(map(lambda x: x.isalnum(), df['comments'])))

# Q10. Check whether alphabetic values present in a comments column of the dataframe
print(">"*20, "String in Pandas : Q10", ">"*20)
# -------- Method 1
print(df['comments'].str.isalpha())
# -------- Method 2
print(df['comments'].apply(lambda x: x.isalpha())) 
# -------- Method 3
print(list(map(lambda x: x.isalpha(), df['comments'])))

# Q11. Check whether numeric values present in a comments column of the dataframe
print(">"*20, "String in Pandas : Q11", ">"*20)
# -------- Method 1
print(df['comments'].str.isdigit())
# -------- Method 2
print(df['comments'].apply(lambda x: x.isdigit())) 
# -------- Method 3
print(list(map(lambda x: x.isdigit(), df['comments'])))

# Q12. Check whether only lower case or upper case is present in a comments column of the dataframe
print(">"*20, "String in Pandas : Q12", ">"*20)
# -------- Method 1
print(df['comments'].str.islower())
# -------- Method 2
print(df['comments'].apply(lambda x: x.islower())) 
# -------- Method 3
print(list(map(lambda x: x.islower(), df['comments'])))

# Q13. Check whether proper case is present in a name column of the dataframe
print(">"*20, "String in Pandas : Q13", ">"*20)
# -------- Method 1
print(df['name'].str.istitle())
# -------- Method 2
print(df['name'].apply(lambda x: x.istitle())) 
# -------- Method 3
print(list(map(lambda x: x.istitle(), df['name'])))

# Q14. Check whether only space is present in a comments column of the dataframe
print(">"*20, "String in Pandas : Q14", ">"*20)
# -------- Method 1
print(df['comments'].str.isspace())
# -------- Method 2
print(df['comments'].apply(lambda x: x.isspace())) 
# -------- Method 3
print(list(map(lambda x: x.isspace(), df['comments'])))
''' NOTE - isspace() - only returns True if the entire string consists of only whitespace (spaces, tabs, newlines, etc.). It will only return True if the string is 
            only spaces — not if it just contains space(s).'''

# Q15. Get the length of the string present in name column of the dataframe
print(">"*20, "String in Pandas : Q15", ">"*20)
# -------- Method 1
print(df['name'].str.len()) 
# -------- Method 2
print(df['name'].apply(len)) # why this way -------?????
# print(df['name'].apply(lambda x: x.len())) # This will not work
# print(list(map(lambda x: x.len(), df['name'])))  # This will not work

# Q16. Get the length of the integer of a score column of the dataframe
print(">"*20, "String in Pandas : Q16", ">"*20)
# -------- Method 1
print(df['score'].map(str).str.len()) 
# -------- Method 2
print(df['score'].map(str).apply(len))

# Q17. Check if a name column starts with a specified string (lu) in the dataframe
print(">"*20, "String in Pandas : Q17", ">"*20)
# -------- Method 1
print(df['name'].str.startswith('Lu')) 
# -------- Method 2
print(df['name'].apply(lambda x: x.startswith('lu'))) 
# -------- Method 3
print(list(map(lambda x: x.startswith('lu'), df['name'])))
'''NOTE - startswith('lu') returns True if the string starts with "lu", otherwise False.
startswith() is a case sensitive function. Case-Insensitive Version: If you want to match 'Lu', 'LU', etc., use:'''
print(list(map(lambda x: x.lower().startswith('lu'), df['name'])))

# Q18. To swap the cases of comments column in the dataframe
print(">"*20, "String in Pandas : Q18", ">"*20)
# -------- Method 1
print(df['comments'].str.swapcase())
# -------- Method 2
print(df['comments'].apply(lambda x: x.swapcase())) 
# -------- Method 3
print(list(map(lambda x: x.swapcase(), df['comments'])))

# Q19. To convert name column in upper/lower cases in the dataframe
print(">"*20, "String in Pandas : Q19", ">"*20)
# -------- Method 1
print(df['name'].str.upper())
# -------- Method 2
print(df['name'].apply(lambda x: x.lower())) 
# -------- Method 3
print(list(map(lambda x: x.upper(), df['name'])))
print(list(map(lambda x: x.lower(), df['name'])))

# Q20. To convert name column in title case in the dataframe
print(">"*20, "String in Pandas : Q20", ">"*20)
# -------- Method 1
print(df['name'].str.title())
# -------- Method 2
print(df['name'].apply(lambda x: x.title())) 
# -------- Method 3
print(list(map(lambda x: x.title(), df['name'])))

# Q21. To replace one value with other value in the dataframe
print(">"*20, "String in Pandas : Q21", ">"*20)
# -------- Method 1
print(df['name'].str.replace("a", "c"))
# -------- Method 2
print(df['name'].apply(lambda x: x.replace("a", "c"))) 
# -------- Method 3
print(list(map(lambda x: x.replace("a", "c"), df['name'])))
'''NOTE - print(df['name'].replace("a", "c")) - this will not work
replace() does an exact match.
It's case-sensitive and whitespace-sensitive
way out - df['name'].str.lower().replace("luz", "c")
df['name'].replace(r'(?i)^luz$', 'c', regex=True)
df['name'].str.strip().replace("luz", "c")
df['name'].str.replace("a", "c", regex=False)
Also, But "a" is not a full value in the column — it appears within names like "Anastasia". Therefore, Use .str.replace() for string 
content replacement. replace() in pandas is not the same as str.replace() in Python strings.'''

# Q22. To replace more than one value with other values in the dataframe 
print(">"*20, "String in Pandas : Q22", ">"*20)
# -------- Method 1
print(df['name'].str.replace('A', 'L').str.replace('L', 'Y'))
# -------- Method 2
print(df['name'].apply(lambda x: x.replace('A', 'L').replace('L', 'Y'))) 
# -------- Method 3
print(list(map(lambda x: x.replace('A', 'L').replace('L', 'Y'), df['name'])))
'''NOTE - print(df['name'].str.replace(["A", "D"], ["L", "Y"])) - will not work
print(df['name'].str.replace({'A': 'L', 'D': 'Y'}, regex=True)) - will not work '''

# Q23. To split a string of comments column of the dataframe into multiple columns
print(">"*20, "String in Pandas : Q23", ">"*20)
# -------- Method 1
print(df["comments"].str.split(" ", expand = True)) # why using expand = true -----?
# -------- Method 2
print(df['comments'].apply(lambda x: x.split(" "))) 
# -------- Method 3
print(list(map(lambda x: x.split(" "), df['comments'])))
df['name'].replace(r'(?i)^luz$', 'c', regex=True) # (?i) makes it case-insensitive and ^...$ ensures it matches the entire string

# Q24. Extract email from a specified column of string type of the dataframe
print(">"*20, "String in Pandas : Q24", ">"*20)
df1 = pd.DataFrame({
    'name_email': ['Alberto Franco af@gmail.com','Gino Mcneill gm@yahoo.com','Ryan Parkes rp@abc.io', 'Eesha Hinton', 'Gino Mcneill gm@github.com']
    })

def find_email(text):
    email = re.findall(r'[\w\.-]+@[\w\.-]+',str(text))
    return ",".join(email)

print(df1['name_email'].apply(lambda x: find_email(x)))
print(list(map(lambda x: find_email(x), df1['name_email'])))

# Q25. Extract hash attached word from twitter text from the comments column of the dataframe
print(">"*20, "String in Pandas : Q25", ">"*20)
def find_hash(text):
    hword=re.findall(r'(?<=#)\w+',text)
    return " ".join(hword)

print(df['comments'].apply(lambda x: find_hash(x)))
print(list(map(lambda x: find_hash(x), df['comments'])))

# Q26. Extract word mention someone in tweets using @ from the comments column of the dataframe
print(">"*20, "String in Pandas : Q26", ">"*20)
def find_at_word(text):
    word=re.findall(r'(?<=@)\w+',text)
    return " ".join(word)

print(df['comments'].apply(lambda x: find_at_word(x)))
print(list(map(lambda x: find_at_word(x), df['comments'])))

# Q27. Extract only number from the comments column of the dataframe
print(">"*20, "String in Pandas : Q27", ">"*20)
print(df['comments'].str.findall(r'\d+')) # Extract all numbers (even multiple from one string)
print(df['comments'].str.extract(r'(\d+)')) #  Extract only the first number

def find_number(text):
    num = re.findall(r'[0-9]+',text)
    return " ".join(num)
print(df['comments'].apply(lambda x: find_number(x)))
print(list(map(lambda x: find_number(x), df['comments'])))

'''NOTE - Convert to numeric (if needed): df['first_number'] = pd.to_numeric(df['first_number'], errors='coerce')'''

# Q28. Extract only phone number from the specified column of the dataframe
print(">"*20, "String in Pandas : Q28", ">"*20)
df1 = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'company_phone_no': ['Company1-Phone no. 4695168357','Company2-Phone no. 8088729013','Company3-Phone no. 6204658086', 'Company4-Phone no. 5159530096', 'Company5-Phone no. 9037952371']
    })

def find_phone_number(text):
    ph_no = re.findall(r"\b\d{10}\b",text)
    return "".join(ph_no)

print(df1['company_phone_no'].apply(lambda x: find_phone_number(x)))
print(list(map(lambda x: find_phone_number(x), df1['company_phone_no'])))

# Q29. Extract year between 1800 to 2200 from the specified column of the dataframe
print(">"*20, "String in Pandas : Q29", ">"*20)
df1 = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })

def find_year(text):
    #line=re.findall(r"\b(18[0][0]|2[0-2][00])\b",text)
    result = re.findall(r"\b(18[0-9]{2}|19[0-8][0-9]|199[0-9]|2[01][0-9]{2}|2200)\b",text)
    return result

print(df1['year'].apply(lambda x: find_year(x)))
print(list(map(lambda x: find_year(x), df1['year'])))

# Q30. Extract only non alphanumeric characters from the comments column of the dataframe
print(">"*20, "String in Pandas : Q30", ">"*20)
def find_nonalpha(text):
    result = re.findall("[^A-Za-z0-9 ]",text)
    return result

print(df['comments'].apply(lambda x: find_nonalpha(x)))
print(list(map(lambda x: find_nonalpha(x), df['comments'])))

''' Q31. Extract only punctuations from the comments column of the dataframe. Note that They include things like periods, commas,
question marks, and exclamation points'''
print(">"*20, "String in Pandas : Q31", ">"*20)
def find_punctuations(text):
    result = re.findall(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*', text)
    string="".join(result)
    return list(string)
print(df['comments'].apply(lambda x: find_punctuations(x)))
print(list(map(lambda x: find_punctuations(x), df['comments'])))

# Q32. Remove repetitive characters from the comments column of the dataframe
print(">"*20, "String in Pandas : Q32", ">"*20)
def rep_char(str1):
    tchr = str1.group(0)
    if len(tchr) > 1:
        return tchr[0:1] # can change the value here on repetition
def unique_char(rep, sent_text):
    convert = re.sub(r'(\w)\1+', rep, sent_text) 
    return convert
print(df['comments'].apply(lambda x : unique_char(rep_char,x)))
print(list(map(lambda x: unique_char(rep_char, x), df['comments'])))

# Q33. Extract numbers greater than 940 from the comments column of the dataframe
print(">"*20, "String in Pandas : Q33", ">"*20)
def test_num_great(text): 
    result = re.findall(r'95[5-9]|9[6-9]\d|[1-9]\d{3,}',text)
    return " ".join(result)
print(df['comments'].apply(lambda x : test_num_great(x)))
print(list(map(lambda x: test_num_great(x), df['comments'])))

# Q34. Extract numbers less than 100 from the comments column of the dataframe
print(">"*20, "String in Pandas : Q34", ">"*20)
def test_num_less(n):
    nums = []
    all_num = []
    for i in n.split():
        result = re.findall(r'\b(0*(?:[1-9][0-9]?|100))\b',i)
        nums.append(result)
        all_num=[",".join(x) for x in nums if x != []]
    return " ".join(all_num)

print(df['comments'].apply(lambda x : test_num_less(x)))
print(list(map(lambda x: test_num_less(x), df['comments'])))

# Q35. Check whether two given words present in a comments column of the dataframe
print(">"*20, "String in Pandas : Q35", ">"*20)
def test_and_cond(text):
    result = re.findall(r'(?=.*Ave.)(?=.*9910).*', text) 
    return " ".join(result)

print(df['comments'].apply(lambda x : test_and_cond(x)))
print(list(map(lambda x: test_and_cond(x), df['comments'])))

# Q36. Extract date (format: mm-dd-yyyy) from a given column of the dataframe
print(">"*20, "String in Pandas : Q36", ">"*20)
def find_valid_dates(dt):
    #format: mm-dd-yyyy
    result = re.findall(r'\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\b',dt)
    return result
print(df['time'].apply(lambda dt : find_valid_dates(dt)))
print(list(map(lambda x: find_valid_dates(x), df['time'])))

# Q37. Extract only words from a comments column of the dataframe
print(">"*20, "String in Pandas : Q37", ">"*20)
def search_words(text):
    result = re.findall(r'\b[^\d\W]+\b', text)
    return " ".join(result)

print(df['comments'].apply(lambda x : search_words(x)))
print(list(map(lambda x: search_words(x), df['comments'])))

# Q38. Extract the sentences where a specific word is present in a given column of the dataframe
print(">"*20, "String in Pandas : Q38", ">"*20)
def pick_only_key_sentence(str1, word):
    result = re.findall(r'([^.]*'+word+'[^.]*)', str1)
    return result

print(df['comments'].apply(lambda x : pick_only_key_sentence(x,'ff')))
print(list(map(lambda x: pick_only_key_sentence(x,'ff'), df['comments'])))

# Q39. Extract the unique sentences from a given column of the dataframe
print(">"*20, "String in Pandas : Q39", ">"*20)
def find_unique_sentence(str1):
    result = re.findall(r'(?sm)(^[^\r\n]+$)(?!.*^\1$)', str1)
    return result

print(df['comments'].apply(lambda st : find_unique_sentence(st)))
print(list(map(lambda x: find_unique_sentence(x), df['comments'])))

# Q40. Extract words starting with capital words from a given column of the dataframe
print(">"*20, "String in Pandas : Q40", ">"*20)
def find_capital_word(str1):
    result = re.findall(r'\b[A-Z]\w+', str1)
    return result

print(df['comments'].apply(lambda cw : find_capital_word(cw)))
print(list(map(lambda x: find_capital_word(x), df['comments'])))

# Q41. to remove the html tags within the specified column of the dataframe
print(">"*20, "String in Pandas : Q41", ">"*20)
def remove_tags(string):
    result = re.sub('<.*?>','',string)
    return result
print(df['comments'].apply(lambda cw : remove_tags(cw)))
print(list(map(lambda x: remove_tags(x), df['comments'])))

# Q42. If you want to detect presence of at least one space
print(">"*20, "String in Pandas : Q42", ">"*20)
print(df['comments'].apply(lambda x: ' ' in x))

# Q43. If you want to check for strings that contain only spaces (or are empty/blank after stripping):
df['comments'].apply(lambda x: x.strip() == '') # This checks whether the string is only spaces or empty. .strip() removes all leading/trailing whitespace.
breakpoint()

# Remove all whitespace - use ''.join(x.split()) or re.sub(r'\s+', '', x)


# ###########################################################################################
# FILTER QUESTION IN PANDAS
# ###########################################################################################

# Q1. Select rows where the value in the 'A' column is greater than 4
print(df[df['A'] > 4])

# Q2. Select only the 'X' and 'Y' columns from the dataframe
print(df[['X', 'Y']])

# Q3. Set a MultiIndex and access specific data using it
print(df.loc[('one', 6)])

# Q4. Slice dataframe based on MultiIndex levels
df = df.set_index(['C', 'A'])
print(df.loc['one'])

# Q5. Swap the levels of a MultiIndex dataframe
df = df.set_index(['Z', 'X'])
print(df.swaplevel())

# Q6. reset the index of a MultiIndex dataframe
df = df.set_index(['C', 'A'])
print(df.reset_index())

# Q7. uses .loc for indexing
print(df.loc[1])

# Q8. use Boolean indexing to select rows where column 'x' > 6
print(df[df['X'] > 6])

# Q9. select the first three rows using iloc
print(df.iloc[:4])

# Q10. use .loc to select rows based on a condition
print(df.loc[df['P'] > 3])

# Q11. uses .loc to set values in the dataframe
df.loc[df['X'] > 5, 'Y'] = 0
print(df)

# Q12. uses .loc to slice dataframe based on row and column labels
print(df.loc[1:3, ['X', 'Z']])

# Q13. select rows where column 'X' > 5 and column 'Y' < 5
print(df[(df['X'] > 5) & (df['Y'] < 5)])

# Q14. uses .loc to slice a MultiIndex dataframe
df = df.set_index(['C', 'A'])
# Sort the MultiIndex
df = df.sort_index()
print(df.loc['one':'two'])

# Q15. uses MultiIndex to select data based on conditions
df = df.set_index(['Z', 'X'])
print(df.loc[('one', slice(None))])



# ###########################################################################################
# JOIN & MERGE QUESTION IN PANDAS
# ###########################################################################################
# Q1. Join the two given dataframes along rows and assign all data
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})

print(pd.concat([student_data1, student_data2]))

# Q2. Join the two given dataframes along columns and assign all data
print(pd.concat([student_data1, student_data2], axis = 1))

# Q3. Append rows to an existing dataframe and display the combined data
print(student_data1.append(s6, ignore_index = True))

# Q4. append a list of dictioneries or series to a existing dataframe and display the combined data
print(student_data1.append(dicts, ignore_index=True, sort=False))

# Q5. join the two given dataframes along rows and merge with another dataframe along the common column id
print(pd.concat([student_data1, student_data2]))
print(pd.merge(result_data, exam_data, on='student_id'))

# Q6. Join the two dataframes using the common column of both dataframes
print(pd.merge(student_data1, student_data2, on='student_id', how='inner'))

# Q7. join the two dataframes with matching records from both sides where available
print(pd.merge(student_data1, student_data2, on='student_id', how='outer'))

# Q8. join (left join) the two dataframes using keys from left dataframe only
print(pd.merge(data1, data2, how='left', on=['key1', 'key2']))

# Q9. join two dataframes using keys from right dataframe only
print(pd.merge(data1, data2, how='right', on=['key1', 'key2']))
print(pd.merge(data2, data1, how='right', on=['key1', 'key2']))

# Q10. merge two given datasets using multiple join keys
print(pd.merge(data1, data2, on=['key1', 'key2']))

# Q11. create a new DataFrame based on existing series, using specified argument and override the existing columns names
s1 = pd.Series([0, 1, 2, 3], name='col1')
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5], name='col3')
print(pd.concat([s1, s2, s3], axis=1, keys=['column1', 'column2', 'column3']))

# Q12. create a combination from two dataframes where a column id combination appears more than once in both dataframes
print(pd.merge(data1, data2, on='key1'))

# Q13. combine the columns of two potentially differently-indexed DataFrames into a single result DataFrame
print(data1.join(data2))

# Q14. merge two given dataframes with different columns
print(pd.concat([data1,data2], axis=0, ignore_index=True))

# Q15. Combine two DataFrame objects by filling null values in one DataFrame with non-null values from other DataFrame
print(df1.combine_first(df2))


# ###########################################################################################
# ADVANCED JOIN & MERGE QUESTION IN PANDAS
# ###########################################################################################

# Q1. merge two DataFrames on a single column
print(pd.merge(df1, df2, on='ID'))

# Q2. performed an outer join on two DataFrames to include all rows from both DataFrames, with missing values filled as NaN
print(pd.merge(df1, df2, on='ID', how='outer'))

# Q3. left join of two DataFrames, including all rows from the left DataFrame and matching rows from the right
print(pd.merge(df1, df2, on='ID', how='left'))

# Q4. perform a right join to include all rows from the right DataFrame and matching rows from the left
print(pd.merge(df1, df2, on='ID', how='right'))

# Q5. how to merge two DataFrames on multiple columns using pd.merge()
print(pd.merge(df1, df2, on=['ID', 'Name']))

# Q6. merge two DataFrames that have overlapping column names, and specify how to handle those overlaps
print(pd.merge(df1, df2, on=['ID', 'Name'], suffixes=('_left', '_right')))

# Q7. merge two DataFrames on their indexes using the left_index and right_index options
print(pd.merge(df1, df2, left_index=True, right_index=True))

# Q8. merged two DataFrames where the column names we want to join on are different in each DataFrame
print(pd.merge(df1, df2, left_on='Employee_ID', right_on='ID'))

# Q9. merge three DataFrames on a common column
print(pd.merge(pd.merge(df1, df2, on='ID'), df3, on='ID'))


# ###########################################################################################
# GROUPING QUESTION IN PANDAS
# ###########################################################################################

# Q1. Write a Pandas program to split the following dataframe into groups based on school code
print(df.groupby(['school_code']))

# Q2. Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school
print(df.groupby('school_code').agg({'age': ['mean', 'min', 'max']}))

# Q3. Write a Pandas program to split the following given dataframe into groups based on school code and class
print(student_data.groupby(['school_code', 'class']))

# Q4. Write a Pandas program to split the following given dataframe into groups based on school code and cast grouping as a list
print(student_data.groupby(['school_code']))

# Q5. Write a Pandas program to split the following given dataframe into groups based on single column and multiple columns. Find the size of the grouped data
print(student_data.groupby(['school_code', 'class']))

# Q6. Write a Pandas program to split the following given dataframe into groups based on school code and call a specific group with the name of the group
print(student_data.groupby(['school_code']))

# Q7. Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group. Using the following dataset find the mean, min, and max values of purchase amount (purch_amt) 
# group by customer id (customer_id)
print(orders_data.groupby('customer_id').agg({'purch_amt': ['mean', 'min', 'max']}))

# Q8. Write a Pandas program to split a dataset to group by two columns and count by each row
print(orders_data.groupby(['salesman_id','customer_id']).size().reset_index().groupby(['salesman_id','customer_id'])[[0]].max())

# Q9. Write a Pandas program to split a dataset to group by two columns and then sort the aggregated results within the groups.
print(df.groupby(['customer_id','salesman_id']).agg({'purch_amt':sum}))
print(df_agg['purch_amt'].groupby(level=0, group_keys=False))

# Q10. Write a Pandas program to split the following dataframe into groups based on customer id and create a list of order date for each group.
print(df.groupby('customer_id')['ord_date'].apply(list))

# Q11. Write a Pandas program to split the following dataframe into groups and calculate monthly purchase amount.
df['ord_date']= pd.to_datetime(df['ord_date'])
print(df.set_index('ord_date').groupby(pd.Grouper(freq='M')).agg({'purch_amt':sum}))

# Q12. Write a Pandas program to split the following dataframe into groups, group by month and year based on order date and find the total purchase amount year wise, month wise
df['ord_date']= pd.to_datetime(df['ord_date'])
print(df.groupby([df['ord_date'].dt.year, df['ord_date'].dt.month]).agg({'purch_amt':sum}))

# Q13. Write a Pandas program to split the following dataframe into groups based on first column and set other column values into a list of values.
print(df.groupby('X').aggregate(lambda tdf: tdf.unique().tolist()))

# Q14. Write a Pandas program to split the following dataframe into groups based on all columns and calculate GroupBy value counts on the dataframe
print(df.groupby(['id', 'type', 'book']).size().unstack(fill_value=0))

# Q15. Write a Pandas program to split the following dataframe into groups and count unique values of 'value' column
print(df.groupby('value')['id'].nunique())

# Q16. Write a Pandas program to split a given dataframe into groups and list all the keys from the GroupBy object
print(df.groupby('school_code'))

# Q17. Write a Pandas program to split a given dataframe into groups and create a new column with count from GroupBy.
print(df.groupby(["book_name", "book_type"])["book_type"].count().reset_index(name="count"))

# Q18. Write a Pandas program to split a given dataframe into groups with bin counts
print(df.groupby(['customer_id', pd.cut(df.sales_id, 3)]))
print(groups.size().unstack())

# Q19. Write a Pandas program to split a given dataframe into groups with multiple aggregations
print(df.groupby(['school_code','class']).agg({'height': ['max', 'mean'],
                                 'weight': ['sum','min','count']}))

# Q20. Write a Pandas program to split a given dataframe into groups and display target column as a list of unique values
print(new_df.apply(lambda x: (','.join([str(s) for s in x['book']])), axis = 1))

# Q21. Write a Pandas program to split the following dataframe into groups and calculate quarterly purchase amount
df['ord_date']= pd.to_datetime(df['ord_date'])
print(df.set_index('ord_date').groupby(pd.Grouper(freq='Q')).agg({'purch_amt':sum}))

# Q22. Write a Pandas program to split the following dataframe into groups by school code and get mean, min, and max value of age with customized column name for each school
print(student_data.groupby('school_code').agg(Age_Mean = ('age','mean'),Age_Max=('age',max),Age_Min=('age',min)))

# Q23. Write a Pandas program to split the following datasets into groups on customer id and calculate the number of customers starting with 'C', the list of all products and the difference of 
# maximum purchase amount and minimum purchase amount
def customer_id_C(x):
    return (x.str[0] == 'C').sum()
print(df.groupby(['salesman_id'])\
  .agg(customer_id_start_C = ('customer_id', customer_id_C),
       customer_id_list = ('customer_id', lambda x: ', '.join(x)),
       purchase_amt_gap   = ('purch_amt', lambda x: x.max()-x.min())
      ))

# Q24. Write a Pandas program to split the following datasets into groups on customer_id to summarize purch_amt and calculate percentage of purch_amt in each group
gr_data = df.groupby(['customer_id','salesman_id']).agg({'purch_amt': 'sum'})
print(gr_data.apply(lambda x:  100*x / x.sum()))

# Q25. Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group, also change the column name of the aggregated metric. Using the following dataset find the mean, 
# min, and max values of purchase amount (purch_amt) group by customer id (customer_id)
print(df.groupby('school_code').agg({'age': [("mean_age","mean"), ("min_age", "min"), ("max_age","max")]}))

# Q26. Write a Pandas program to split a given dataset, group by two columns and convert other columns of the dataframe into a dictionary with column header as key
dict_data_list = list()

for gg, dd in df.groupby(['school_code','class']):
    group = dict(zip(['school_code','class'], gg))
    ocolumns_list = list()
    for _, data in dd.iterrows():
        data = data.drop(labels=['school_code','class'])
        ocolumns_list.append(data.to_dict())
    group['other_columns'] = ocolumns_list
    dict_data_list.append(group)

print(dict_data_list) 

# Q27. Write a Pandas program to split a given dataset, group by one column and apply an aggregate function to few columns and another aggregate function to the rest of the columns of the dataframe
print(df.groupby('salesman_id').agg(lambda x : x.sum() if x.name in ['sale_jan','sale_feb','sale_mar'] else x.mean()))

# Q28. Write a Pandas program to split a given dataset, group by one column and remove those groups if all the values of a specific columns are not available.
print(df[(~df['height'].isna()).groupby(df['school_code']).transform('any')])

# Q29. Write a Pandas program to split a given dataset using group by on specified column into two labels and ranges.
# Split the group on 'salesman_id',
# Ranges:
# 1) (5001...5006)
# 2) (5007..5012)
print(df.groupby(pd.cut(df['salesman_id'], 
                  bins=[0,5006,np.inf],  
                  labels=['S1', 'S2']))['sale_jan'].sum().reset_index())

# Q30. Write a Pandas program to split the following dataset using group by on first column and aggregate over multiple lists on second column.
print(df.set_index('student_id')['marks'].groupby('student_id').apply(list).apply(lambda x: np.mean(x,0)))

# Q31. Write a Pandas program to split the following dataset using group by on 'salesman_id' and find the first order date for each group.
print(df.groupby('salesman_id')['ord_date'].min())

# Q32. Write a Pandas program to split a given dataset using group by on multiple columns and drop last n rows of from each group.
print(df.drop(df.groupby(['salesman_id', 'customer_id']).tail(n).index, axis=0))

# ###########################################################################################
# ADVANCED GROUPING QUESTION IN PANDAS
# ###########################################################################################

# Q1. Write a Pandas program to group data by multiple columns to perform complex data analysis and aggregations
print(df.groupby(['Category', 'Type']).sum())

# Q2. Write a Pandas program to apply multiple aggregation functions to grouped data using for enhanced data insights
print(df.groupby('Category').agg(['sum', 'mean', 'max']))

# Q3. Write a Pandas program to implement custom aggregation functions within groupby for tailored data analysis
def custom_agg(x):
    return x.max() - x.min()

print(df.groupby('Category').agg(custom_agg))

# Q4. Write a Pandas program that implements the technique of grouping and filtering groups to refine your data analysis and insights
grouped = df.groupby('Category')
print(grouped.filter(lambda x: x['Value'].sum() > 5))

# Q5. Write a Pandas program to group data and apply custom functions to groups for flexible data transformations
def scale_values(x):
    return x / x.max()
print(df.groupby('Category').transform(scale_values))

# Q6. Write a Pandas program to use different aggregation functions on different columns for versatile data analysis
print(df.groupby('Category').agg({'Value1': 'sum', 'Value2': 'mean'}))

# Q7. Write a Pandas program to use lambda functions within groupby for flexible and efficient data transformations
print(df.groupby('Category').agg(lambda x: x.max() - x.min()))

# Q8. Write a Pandas program to perform grouping and aggregation operations using multiple index levels
print(df.groupby(['Category', 'Type']).sum())

# Q9. Write a Pandas program that applies different functions to different columns in Pandas GroupBy for tailored data analysis.
print(df.groupby('Category').agg({'Value1': 'mean', 'Value2': 'sum'}))

# Q10. Write a Pandas program to use named aggregations in GroupBy to make your data aggregation operations more readable and organized
print(df.groupby('Category').agg(
    Value1_mean=('Value1', 'mean'),
    Value2_sum=('Value2', 'sum')
))

# Q11. Write a Pandas program to combine GroupBy with Transform to perform complex data transformations on grouped data
print(df.groupby('Category').transform('mean'))

# Q12. Write a Pandas program that uses dictionaries to apply different functions to different columns in GroupBy
print(df.groupby('Category').agg({'Value1': 'sum', 'Value2': 'mean'}))

# Q13. Write a Pandas program to create a new column with aggregated data from a GroupBy operation for enriched data insights
print(df.groupby('Category')['Value'].transform('sum'))

# Q14. Write a Pandas program to handle missing data in GroupBy operations to ensure accurate and reliable data analysis
print(df.fillna(0).groupby('Category').sum())

# Q15. Write a Pandas program to apply multiple aggregations with named functions in GroupBy for detailed data analysis
print(df.groupby('Category').agg(
    Total_Value1=('Value1', 'sum'),
    Average_Value2=('Value2', 'mean')
))


# string.count(substring)

#     row['name'], row['score']
# exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James'],
#         'score': [12.5, 9, 16.5, np.nan]}
# labels = ['a', 'b', 'c', 'd']

# print(df)
# print([np.random.randint(1, 101, size=10)])
# breakpoint()

# diner club
# indian oil
# millenum 
# swiggy

