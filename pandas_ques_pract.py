# 1. custom function that squares each element of a Pandas DataFrame element-wise using applymap() function
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

def square(x):
    return x ** 2

# on particular column
df['Sq_col'] = df['A'].apply(square)
print(df)
# on all columns - same columns but now contains square of each elements
df_sq = df.apply(square)
print(df_sq)
df_sq = df.applymap(square)
print(df_sq)

''' apply():
Scope: Works on either a Series (column) or a DataFrame.
Application: Applies a function along an axis (rows or columns) of the DataFrame or on the entire Series
applymap():
Scope: Works only on a DataFrame.
Application: Applies a function element-wise to every cell in the DataFrame
1. apply() works on rows, columns, or the entire DataFrame, while applymap() works on individual cells
2. apply() can handle different data types within a row or column, while applymap() requires all elements to be of the same type
3. applymap() is generally faster for element-wise operations, while apply() provides more flexibility'''

# 2. custom function that calculates the sum of each row in a DataFrame using apply() function
def row_sum(x):
    return x.sum()
print("Q2", "*"*20)
# on particular column
print(df[['A']].apply(row_sum))
# on all columns
print(df.apply(row_sum, axis = 1))
# Using apply() on Multiple Columns
df[['A', 'B']] = df[['A', 'B']].apply(row_sum)
print(df)

# 3. custom function to calculate the mean of each column using apply() column-wise
# Define a custom function to calculate the mean of a column
def column_mean(column):
    return column.mean()
print("Q3", "*"*20)
# on particular column
means = df[['A']].apply(column_mean)
print(means) 
# on all columns
means = df.apply(column_mean, axis=0)
df.loc['Mean'] = means # Add the means as a new row to the DataFrame
print(df) 
# Using apply() on Multiple Columns
means = df[['A', 'B']].apply(column_mean)
print(means)

# NOTE - df['A_doubled'] = df['A'].apply(double) - the function you pass must be designed to work element-wise when applied to a Series

# 4. custom function to calculate the square of each column using apply() column-wise
def double(x):
    return x * 2
print("Q4", "*"*20)
# on particular column
df[['A']] = df[['A']].map(double)
print(df)
# on all columns
df = df.map(double)
print(df)

# 5. custom function to add 1 to col A and multiply by 2 to column B element using apply()
def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2
print("Q5", "*"*20)
df['A'] = df['A'].apply(add_one)
df['B'] = df['B'].apply(multiply_by_two)
print(df)

# 6. Apply a lambda function that halves the values of a column
print("Q6", "*"*20)
# on particular column
df['A'] = df['A'].apply(lambda x: x / 2)
print(df)
# on all columns
df = df.apply(lambda x: x / 2)
print(df)

# 7. modify multiple columns of a DataFrame based on a specific condition
def subtract_values(row):
    return row['B'] - row['A'] 
print("Q7", "*"*20)
df['A_minus_B'] = df.apply(subtract_values, axis=1)
print(df)

# 8. apply a custom function to rows based on a condition
def add_if_condition(row):
    return row['A'] + row['B'] if row['C'] > 150 else row['A']
print("Q8", "*"*20)
df['Conditional_Sum'] = df.apply(add_if_condition, axis=1)
print(df)

# 9. use map() function to replace values in a Pandas Series based on a dictionary mapping
s = pd.Series([1, 2, 3, 4, 5])
replace_dict = {1: 'one', 2: 'two', 3: 'three'}
print("Q9", "*"*20)
print(s.map(replace_dict))

# 10. apply different operations on columns based on their data types using apply()
def modify_based_on_type(x):
    if isinstance(x, int):
        return x + 10  # Add 10 if integer
    elif isinstance(x, float):
        return x * 2  # Double if float
    else:
        return x.upper()  # Uppercase if string
print("Q10", "*"*20)
print(df.applymap(modify_based_on_type))

# 11. custom function that uses conditional logic to set values based on a threshold
def threshold(row):
    return 'High' if row['A'] > 15 else 'Low'
print("Q11", "*"*20)
df['A_threshold'] = df.apply(threshold, axis=1)
print(df)

# 12. apply a custom function to transform date values in a DataFrame
df2 = pd.DataFrame({
    'Date': ['2023-01-01', '2023-06-15', '2023-12-31']
})
print("Q12", "*"*20)
# Convert the 'Date' column to datetime
df2['Date'] = pd.to_datetime(df2['Date'])
print(df2)

# 13. Define a custom function to extract the year
def get_year(date):
    return date.year
print("Q13", "*"*20)
df2['Year'] = df2['Date'].apply(get_year)
print(df2)

# 14. apply a custom function with multiple conditions to create a new column in a DataFrame
def categorize(row):
    if row['A'] > 20 and row['B'] > 20:
        return 'High-High'
    elif row['A'] > 20:
        return 'High-Low'
    elif row['B'] > 20:
        return 'Low-High'
    else:
        return 'Low-Low'
print("Q14", "*"*20)
# Apply the function row-wise to create a new category column
df['Category'] = df.apply(categorize, axis=1)
print(df)

# 15. map() function with a lambda expression to apply a simple mathematical operation on a Series
print("Q15", "*"*20)
df['A'] = df[['A']].map(lambda x: x * 3)
print(df)

# 16. custom function to fill missing values in a DataFrame based on column-specific logic
def fill_missing(x):
    if pd.isna(x):
        return 0  # Fill NaN with 0
    return x
print("Q16", "*"*20)
print(df.applymap(fill_missing))

# 17. apply a custom function to normalize (scale) the values in a DataFrame
def normalize(column):
    return (column - column.min()) / (column.max() - column.min())
print("Q17", "*"*20)
print(df[['A', 'B']].apply(normalize, axis=0))

# 18. apply() to calculate a custom rolling window average over a DataFrame column
def rolling_average(series, window):
    return series.rolling(window=window).mean()
print("Q18", "*"*20)
# Apply the function to column 'A' with a window of 2
df['A_rolling_avg'] = rolling_average(df['A'], window=2)
print(df)

# 19. grouped a DataFrame by a specific column and apply a custom aggregation function using apply()
df3 = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 15, 25]
})
def custom_agg(group):
    return group['Value'].sum()
print("Q19", "*"*20)
# Group by 'Category' and apply the custom aggregation function
print(df3.groupby('Category').apply(custom_agg))

# 20. applied a custom function to standardize all numeric values in a DataFrame using applymap()
def standardize(x, mean, std):
    return (x - mean) / std if std != 0 else 0  # Avoid division by zero
print("Q20", "*"*20)
print(df.apply(lambda col: col.apply(standardize, args=(col.mean(), col.std()))))