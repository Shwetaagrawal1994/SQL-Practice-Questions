import pandas as pd
import numpy as np

# Lambda Functions
''' Lambda functions are similar to user-defined functions but without a name. They're commonly referred to as anonymous functions.
They are efficient whenever you want to create a function that will only contain simple expressions – that is, expressions that are 
usually a single line of a statement. 
                            Syntax - lambda argument(s) : expression

where, lambda: The keyword to define the function
arguments: A comma-separated list of input parameters (like in a regular function)
expression: A single expression that is evaluated and returned 
'''
s2 = lambda func: func.upper()
print(s2('GeeksforGeeks'))

a = 2
print(lambda x: a + 1)
print((lambda x: x + 1)(2))
print((lambda x: x + 1)(10))

strs = lambda x: x.upper()
print(strs("shweta"))

# Lamba with if else
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(4))  
print(check(7))

# Lambda with multiple expressions
calc = lambda x, y: (x + y, x * y)
print(calc(3, 4))

# Lambda with filter()
lst = [33, 3, 22, 2, 11, 1]
print(filter(lambda x: x > 10, lst))

func = list(filter(lambda x: x > 10, [33, 3, 22, 2, 11, 1]))
print(func)
print(list(filter(lambda x: x > 10, [33, 3, 22, 2, 11, 1])))

# Lambda with map()
# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

# Lambda with reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 1, 2, 3, 4]
print(reduce(lambda x, y: x + y, numbers, 0))
print(reduce(lambda x, y: x + y, numbers, 5))

''' One common pitfall when using the reduce() function is handling empty iterables. Passing an empty iterable to reduce() without 
an initializer raises a TypeError because there’s no initial value to start the reduction process. To avoid this, always provide an 
initializer when the iterable might be empty.'''
numbers = []
sum_result = reduce(lambda x, y: x + y, numbers, 0)
print(sum_result)

# Usage of Lambda in pandas dataframe

df = pd.DataFrame(
    {"name": ["IBRAHIM", "SEGUN", "YUSUF", "DARE", "BOLA", "SOKUNBI"],
     "score": [50, 32, 45, 45, 23, 45]
    }
)

# Lambda with apply()
df["name"] = df["name"].apply(lambda x: x.lower())

# Both will return same output
df['score2'] = df['score'].map(lambda x: x + 10)
print(df)
df['score2'] = df['score'].apply(lambda x: x + 10)
print(df)

df=pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':['Jeremy','Frank','Janet','Ryan','Mary'],
    'age':[20,25,15,10,30],
    'income':[4000,7000,200,0,10000]
})
print(df)

# Lambda With Apply
df['age']=df['age'].apply(lambda x: x+3)
df['age']=df.apply(lambda x: x['age']+3,axis=1)

# Lambda With Filter Function
print(df[df['age'].apply(lambda x: x > 18)])
print(df)

''' It’s performance appraisal time, and the employees’ income gets increased by 20%. This means we have to increase each person’s 
salary by 20% in our Pandas dataframe.'''
# Lambda With Map Function
df['income']=list(map(lambda x: int(x+x*0.2),df['income']))
print(df)

# Lambda With Reduce Function
# let’s see the total income of the family. 
reduce(lambda a,b: a+b,df['income'])
print(df)

# In the family dataframe, we must categorize people into ‘Adult’ or ‘Child.’ 
df['category']=df['age'].apply(lambda x: 'Adult' if x>=18 else 'Child')
print(df)

# floor the salary values
df["floor_salary"] = df.income.apply(np.floor)
print(df.loc[0:5,['income',"floor_salary"]])

# Finding the maximum values of all rows of the columns
print(df.loc[:,["income","age"]].apply(max,axis =1))

# Returning the maximum values of the columns
print(df.loc[:,["income","age"]].apply(max,axis =0))

# Returns indices of the columns with the maximum elements (salary and borrowed amount)
print(df.loc[:,["income","age"]].apply(np.argmax,axis =0))

print(df.apply(np.sum, axis=1))

# Apply() with User defined Function
def cal_diff(fs):
    return np.max(fs) - np.min(fs)
print(df["income","age"].apply(cal_diff,axis=0))