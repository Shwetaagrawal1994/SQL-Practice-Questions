# breakpoint()
################################################################
########### >>>>>>>>>>>>>>>>>> IF ELSE >>>>>>>>>>>>>>>> ###########
################################################################
print(" If else begins", "*"*80)

age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# short hand - value_if_true if condition else value_if_false
number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number is {result}.")

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

################################################################
########### >>>>>>>>>>>>>>>>>> SETS >>>>>>>>>>>>>>>> ###########
################################################################
print(" Sets begins", "*"*80)
''' A set is an unordered collection of unique items. Sets are mutable, meaning you can add or remove items after its creation but it 
contains immutable objects. Sets are defined by enclosing elements in curly braces {} or by using the set() function. '''

####### >>>>>>>>>>>>>>>>>>>>> Create a set
## ------ Using Curly Braces {}
S = {'red', 'green', 'blue'} # One type of elements
print("Create a set - first way: ", S)

## ------ using set constructor
S = set('abc')
print("Create a set - second way: ", S)
# S = set(1,2,3) # This will throw an error because set() function takes a single iterable argument

## ------ create set with range function
S = set(range(0, 4)) # Set of successive integers
print("Create a set of successive integers: ", S)

## ------ create set with mixed data type elements
S = {1, 'abc', 1.23, (3+4j), True} # Different types of elements
print("Create a set of Different types of elements: ", S)

# Sets don’t allow duplicates. They are automatically removed during the creation of a set. Why? Because sets store only unique hash 
# values.
S = {'red', 'green', 'blue', 'red'}
print(S)

## ------ create an empty set  
# Using empty curly braces {} creates an empty dictionary, not an empty set. Therefore, use set() function to create an empty set.
S = set()
print("Create an empty set: ", S)

''' Nested Sets: you cannot have a standard, mutable set within another set in Python, because sets can only contain hashable elements, 
and regular sets are not hashable (they are mutable). To create a nested set structure, you must use frozenset objects for the inner 
sets. Frozensets are immutable (cannot be changed after creation) and thus are hashable. '''

####### >>>>>>>>>>>>>>>>>>>>> Set with other data structures
# Set constructors with mutable elements are not allowed
''' A set itself is mutable (changeable), but it cannot contain mutable objects. Therefore, immutable objects like numbers, strings, 
tuples can be a set item, but lists and dictionaries are mutable, so they cannot be. '''
# S = {[1, 2, 3]} or S = {1, 2.3, 'abc', [1, 2, 3]} # This will raise an error because lists are mutable
print(S)
# why error? Because lists are mutable and unhashable, and set elements must be hashable.

''' QUESTION: What does “hashable” mean?
An object is hashable if:
--> Its value does not change (immutable)
--> It has a fixed hash value during its lifetime
✔ Hashable Items: int, float, str, tuple (only if it contains hashable items)
❌ Not hashable Items: list, dict, set 
why required? Python uses the hash value to store and quickly look up items in hash tables (sets & dicts).
NOTE - Sets and dicts are implemented using hash tables.
object	Mutable?	Hashable?
int	No	Yes
str	No	Yes
tuple	No*	Yes*
list	Yes	No
set	Yes	No
frozenset	No	Yes
'''

## ------ Convert list into set
S = set([1, 2, 3]) # but cannot use {[1, 2, 3]}
print("Convert list into set: ", S)

''' QUESTION: why set([1, 2, 3]) works but {[1, 2, 3]} does not?
set([1, 2, 3]) works because it is using the set() function to create a set from a list. The list [1, 2, 3] is passed as an argument to
the set() function, which then creates a set containing the elements of the list. On the other hand, {[1, 2, 3]} is attempting to create 
a set using curly braces, but it is trying to include a list [1, 2, 3] as an element of the set. Since lists are mutable and cannot be 
included in a set, this will raise a TypeError.

set([1, 2, 3]) → {1, 2, 3}
This creates a set whose elements are integers and integers are immutable and hashable. Sets can only contain hashable (immutable) elements
Lists are mutable → not hashable → cannot be elements of a set

{[1, 2, 3]} → type error
This tries to create a set containing a list. A list is mutable. Mutable objects are not hashable. Set elements must be hashable

Sets use hashing for fast lookup. If a mutable object were allowed:
--> Its value could change
--> Its hash would change
--> The set would lose track of where the element is stored
That would break the data structure.

set([1, 2, 3]) → list is just an input, elements are integers → OK
{[1, 2, 3]} → list is an element of the set → NOT OK
'''

## ------ Convert tuple into set
S = set((1, 2, 3)) # tuple is immutable
print("Convert tuple into set - first way: ", S)
S = {(1,2,3)}
print("Convert tuple into set - second way: ", S)

## ------ Converting dict to set
S = set({'a':1, 'b':2})
print("Converting dict to set: ",  S) # Output: {'a', 'b'} Only keys are taken when converting a dictionary to a set.

# QUESTION: What is the output of the following code and why?
S = {True, 1, 1.0}
print(S) # Output: {True} 
# Why this output? because True and 1 are considered equal in Python sets i.e., True == 1 == 1.0 or hash(True) == hash(1) == hash(1.0) 
# and sets cannot have duplicate elements.

####### >>>>>>>>>>>>>>>>>>>>>  Add Items to a Set
## ------ Add single item to a set
S = {'red', 'green', 'blue'}
S.add('yellow')
print("Add Items to a Set: ", S) 
''' NOTE - 1. 'yellow' can be appended in S but at any position since sets are unordered i.e., order of elements in the output may vary
each time you run the code.
2. Only 1 item can be added with add() method. '''

## ------ Add multiple items to a set
S = {'red', 'green', 'blue'}
S.update(['yellow', 'orange'])
print("Add multiple items to a set: ", S)
''' NOTE: 'yellow' & 'orange' can be appended in S but at any position since sets are unordered i.e., order of elements in the output 
mayvary each time you run the code.'''

####### >>>>>>>>>>>>>>>>>>>>>  Remove Items from a Set
## ------ Remove single item from a set
# → remove() method: With remove method() in sets, following points to note:
''' 
1. If the specified item is not present in the set, remove() method raises a KeyError -- ❌ KeyError 
2. The set is modified in-place and does not return a new set -- ✅ in-place
3. If the specified item is present multiple times (not possible in sets), only the first occurrence is removed -- ✅ only 1 item
4. If the set is empty, calling remove() will raise a KeyError -- ❌ KeyError
2. The Python remove() method can only take a single item to remove at a time. '''
S = {'red', 'green', 'blue'}
S.remove('red')
print("Remove Items from a Set - first way: ", S)


# → discard() method: With discard() method in sets, following points to note:
'''
1. Difference between remove() vs discard() - Both methods work exactly the same. The only difference is that if specified item
is not present in a set: remove() method raises KeyError discard() method does nothing -- ✅ No error
2. If the set is empty, calling discard() will not raise any error -- ✅ No error
3. All other properties are same as remove() method -- ✅ in-place, ✅ only 1 item '''
S = {'red', 'green', 'blue'}
# S.discard('red')
S.discard('xyz')
print("Remove Items from a Set - second way: ", S)


# → pop() method: With pop method() in sets, following points to note:
''' 
1. Remove random item from a set and the removed item can be viewed
2. If the method is called on an empty set, it raises a KeyError
3. The method modifies the original set in-place by removing the returned element
4. pop() method with sets does not take any arguments
x = S.pop('red') # TypeError: set.pop() takes no arguments (1 given) '''
S = {'red', 'green', 'blue'}
x = S.pop()
print("Remove random item from a set using pop() method: ", S)
print("view the removed item: ",x)

# → clear() method - remove all items and creates an empty set
S = {'red', 'green', 'blue'}
S.clear()
print("Clear all items from a set: ", S)

## ------ Remove multilple items from a set
# → Using difference_update()
S = {1, 2, 3, 4, 5, 6}
elements_to_remove = {2, 4, 6}  # Can be a set, list, or tuple
S.difference_update(elements_to_remove)
print("Remove multilple items - Method 1: ", S)

# → Using the -= operator
S = {10, 20, 30, 40, 50}
elements_to_remove = [10, 30]
S -= set(elements_to_remove) # The operand for -= must be a set
print("Remove multilple items - Method 2: ", S)

# → Using discard() in a loop
S = {1, 2, 3, 4, 5}
elements_to_remove = [2, 6, 4]  # '6' is not in the set, but won't cause an error
for element in elements_to_remove:
    S.discard(element) # Safely removes the element if it exists
print("Remove multilple items - Method 3: ", S)

# →  Using difference() to create a new set
# All above methods modify the original set. If you want to create a new set without certain elements, use difference() method.
S = {1, 2, 3, 4, 5}
to_remove = {2, 4}
new_set = S.difference(to_remove)
print("Remove multilple items - Method 4: ", new_set) 
print(S) # Original set remains unchanged

## ------ Delete a Set: delete the set completely with del keyword.
S = {"apple", "banana", "cherry"}
del S
# print(S) # This would raise a NameError

####### >>>>>>>>>>>>>>>>>>>>>  Find Set Size
S = {'red', 'green', 'blue'}
print("Set Size: ", len(S))

####### >>>>>>>>>>>>>>>>>>>>>  Iterate Through a Set
S = {'red', 'green', 'blue'}
print("Iterate Through a Set:")
for item in S:
    print(item)

####### >>>>>>>>>>>>>>>>>>>>>  Check if an Item Exists or not exits in a Set
## ------Check for presence
S = {'red', 'green', 'blue'}
if 'red' in S:
    print('yes')
## ------Check for absence
S = {'red', 'green', 'blue'}
if 'yellow' not in S:
    print('yes')

####### >>>>>>>>>>>>>>>>>>>>> Set Operations
# Sets are commonly used for computing mathematical operations such as intersection, union, difference, and symmetric difference.

## ------ Set Union: You can perform union on two or more sets using union() method or  |  operator. 
# Union of the sets A and B is the set of all items in either A or B
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}
C = {'yellow', 'red', 'pink'}
# →  by operator
print("2 Set Union - first way(by operator): ", A | B)
print("3 Set Union - first way(by operator): ", A | B | C)
# →  by method
print("2 Set Union - second way(by method): ", A.union(B))
print("3 Set Union - second way(by method): ", A.union(B, C))
print("3 Set Union - second way(by method): ", A.union(B).union(C))

## ------ Set Intersection: You can perform intersection on two or more sets using intersection() method or  &  operator
# Intersection of the sets A and B is the set of all common items in either A or B
# →  by operator
print("2 Set Intersection - first way(by operator): ", A & B)
print("3 Set Intersection - first way(by operator): ", A & B & C)
# →  by method
print("2 Set Intersection - second way(by method): ", A.intersection(B))
print("3 Set Intersection - second way(by method): ", A.intersection(B, C))

## ------ Set Difference: You can perform difference on two or more sets using difference() method or  -  operator
# Set Difference of A and B is the set of all items that are in A but not in B.
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}
# →  by operator
print("2 Set Difference - first way(by operator): ", A - B)
print("3 Set Difference - first way(by operator): ", A - B - C)
# →  by method
print("2 Set Difference - second way(by method): ", A.difference(B))
print("3 Set Difference - second way(by method): ", A.difference(B, C))

## ------ Symmetric diff: You can perform difference on two or more sets using symmetric_difference() method or  ^ operator
# symmetric difference of sets A and B is the set of all elements in either A or B, but not both
# →  by operator
print("2 Set Symmetric Difference - first way(by operator): ", A ^ B)
print("3 Set Symmetric Difference - first way(by operator): ", A ^ B ^ C)
# →  by method
print("2 Set Symmetric Difference - second way(by method): ", A.symmetric_difference(B))
print("3 Set Symmetric Difference - second way(by method): ", A.symmetric_difference(B).symmetric_difference(C))

'''QUESTION: Why are sets useful in data science?
→ Remove duplicates quickly
→ Fast membership testing (O(1) average)
→ Set operations (intersection, union, difference) for feature comparison, customer overlap, etc. '''

''' QUESTION : How is set membership faster than list?
Set → Hash table → O(1) i.e., x in S   # faster
List → Sequential scan → O(n) i.e., x in my_list  # slower '''
# Example to demonstrate performance difference
import time
large_set = set(range(1000000))
large_list = list(range(1000000))
start = time.time()
for i in range(10000):
    999999 in large_set
end = time.time()
print("Set membership test time:", end - start)
# start = time.time() # commented as it takes time to execute
# for i in range(10000):
#     999999 in large_list
# end = time.time()
# print("List membership test time:", end - start)

####### >>>>>>>>>>>>>>>>>>>>> frozenset
''' Frozenset - Immutable version of set
Hashable → can be used as dictionary keys or inside sets'''
fs = frozenset([1, 2, 3])
print("Create a frozenset: ", fs)

####### >>>>>>>>>>>>>>>>>>>>> Real data science use cases of sets
features_A = {1, 2, 3}
features_B = {3, 4, 5}
model_A_features = set(features_A)
model_B_features = set(features_B)
common_features = model_A_features & model_B_features
unique_to_A = model_A_features - model_B_features

''' Other methods: all()	Returns True if all items in a set are true
any()	Returns True if any item in a set is true
enumerate()	Takes a set and returns an enumerate object
len()	Returns the number of items in the set
max()	Returns the largest item of the set
min()	Returns the smallest item of the set
sorted()	Returns a sorted set
sum()    Returns the sum of all items in the set'''

''' Other methods: 
intersection_update()	Removes the items from this set that are not present in other sets
difference_update()	Removes the items from this set that are also included in another set
symmetric_difference_update()	Modify this set with the symmetric difference of this set and other set
isdisjoint()	Determines whether or not two sets have any elements in common
issubset()	Determines whether one set is a subset of the other
issuperset()	Determines whether one set is a superset of the other '''





###################################################################
########### >>>>>>>>>>>>>>>>>> LIST >>>>>>>>>>>>>>>> ##############
###################################################################
print(" List Function begins", "*"*80)
''' A list is an ordered collection of items/ elements/ objects. The values in a list are called items or elements or object. Lists 
are defined by enclosing elements in square brackets [] or by using the list() function. 
LIST PROPERTIES::
→ Lists are ordered - Lists remember the order of items inserted.
→ Accessed by index - Items in a list can be accessed using an index.
→ Lists can contain any sort of item/ object/ elements - It can be numbers, strings, tuples and even other lists.
→ Lists are changeable (mutable) - You can change a list in-place, add new items, and delete or update existing items ie, you can add, 
remove, or change items after the list is created
'''

####### >>>>>>>>>>>>>>>>>>>>> Create a list
## ------ Using square Braces []
L = [1, 2, 3, 4, 5]
print("Create a List - first way: ", L)    

## ------ using list constructor
L = list([1, 2, 3]) # list() Constructor - You can also create a list using the built-in list() constructor.
L = list((1, 2, 3))
# L = list(1, 2, 3) # This will throw an error because list() function takes a single iterable argument
print("Create a List - second way: ", L) 

## ------ create list with range function
L = list(range(6))
L = list(range(1, 6)) # Output: [ 1, 2, 3, 4, 5]
print("create list with range function: ", L) 
L = [range(6)] # Output: [ range(0, 6) ] and not [0, 1, 2, 3, 4, 5]
print("create list with range function - wrong way=: ", L) 

## ------ create list with mixed data types elements
L = ['red', 'green', 'blue'] # A list of strings
print("Create a List for strings: ", L)

L = [1, 'abc', 1.23, True] # A list with mixed datatypes
print("Create a List for mixed datatypes: ", L)

## ------ create an empty list  
# A list containing zero items is called an empty list and you can create one with emptybrackets []
L = []
print("Create an empty List: ", L)

####### >>>>>>>>>>>>>>>>>>>>> List with other data structures
## ------ String to a list
L = list('abc')
print("String to a list: ", L) 

## ------ Tuple to a list
L = list((1, 2, 3)) # or [(1, 2, 3)]
print("Tuple to a list: ", L)    

## ------ Set to a list
L = list({'red', 'green', 'blue'}) # or [{'red', 'green', 'blue'}]
print("Set to a list: ", L) 

## ------ Nested Lists 
L = ['red', ['green', 'blue'], 'yellow']
print("Nested Lists: ", L)

####### >>>>>>>>>>>>>>>>>>>>> Access items 
## ------ by values/item 
print("Access List Index: ", L.index('red')) 
''' index() method - Find Index of Item in the list and gives index of first occurence
syntax:                                      list.index(element, start, end)
L.index('red', 'blue') - throws error (TypeError: slice indices must be integers or have an __index__ method). Therefore, can access
only single item at a time.'''

## ------ by index - using an index in square brackets. Note that list indexing starts from 0.
L = ['red', 'green', 'blue', 'cyan', 'black']
print(L[0]) # first item
print(L[2]) # third item   

# → Negative Indexing: 
# You can also access a list by negative indexing. Negative indexes count backward from the end of the list and it starts with -1. So, 
# L[-1] refers to the last item., L[-2] is the second-last, and so on.
print(L[-1]) # last item
print(L[-3]) # third-last item 

# → Out of range Index: 
# NOTE - If you try to access an index that is out of range, Python will raise an IndexError.
# print(L[10]) -- commented as it will throw error

## ------ Access Nested List Items:
# You can access items in a nested list by using multiple indices in square bracket.
L = ['red', ['green', 'blue'], 'yellow']
print("Access Nested List Items: ", L[1][0]) # output is 'green'
print("Access Nested List Items: ", L[1][1]) # output is 'blue' 
# NOTE - For list with string elements/items, if index is not for the inner list then accessing is done based on letters: 
L = ['red', 'pink', ['green', 'blue'], 'yellow']
print("Access Nested List Items: ", L[1][0]) # output is p
# For list with non string elements/items,if index is not for the inner list then it will throw error:
# L = [1, 3, [5, 7], 3]
# print("Access Nested List Items: ", L[1][0]) # output is type error

####### >>>>>>>>>>>>>>>>>>>>> Slicing a List
''' You can access a range of items in a list by using the slicing operator colon : inside square brackets.
A segment of a list is called a slice and you can extract one by using a slice operator. A slice of a list is also a list.
The slice operator [n:m] returns the part of the list from the “n-th” item to the “m-th” item, including the first but excluding 
the last. Its syntax is:                                L[start:stop:step]
where, 
→ start: The index at which the slice begins (inclusive). If omitted, the slice starts from the beginning of the list.
→ stop: The index at which the slice ends (exclusive). If omitted, the slice goes up to the end of the list.
→ step: The interval between elements in the slice. If omitted, the default step is 1.'''

L = ['red', 'green', 'blue', 'cyan', 'black']
print(L[1:4]) # items from index 1 to 3
print(L[:3])  # items from start to index 2
print(L[2:])  # items from index 2 to end
print(L[:])   # all items
print(L[3:-1]) # items from index 3 to second-last item
print(L[1:6:2]) # items from index 1 to 5 with a step of 2

'''NOTE - 
1. print(L[[0]] ) # list indices must be integers or slices, not list

2. Start argument greater than stop: If you try to create a slice where the starting index is the same as or greater than the stopping 
index (and the step is positive), you'll get an empty list:
print("Start argument greater than stop: ", L[5:2])

3. Out of Range Indices: When you use indices that go beyond the boundaries of a list, Python adjusts the indices to the nearest valid 
values instead of causing an error i.e., returns rest of the list. Attempt to slice up to index 40 (which doesn't exist)
print("Out of Range Indices: ",L[3:40]) # items from 2nd till end
print("Out of Range Indices: ",L[40:3]) # returns empty list
print("Out of Range Indices: ",L[1:4:40]) # returns only 2nd item

4. Stop argument is 0:
print(" Stop is 0: ", L[1:0:1]) # output is []

5. Step Size 0: Specifying a step size of 0 is not allowed and will result in a ValueError:
# print(L[1:4:0]) -- commenting as it will throw error '''

####### >>>>>>>>>>>>>>>>>>>>>  Reversing a List
print("Reversing a List: ", L[::-1])
''' You can reverse the order of elements in a list by using slicing with a negative step value. This means coder has omitted both the 
start and stop indices while specifying a negative step value of -1 reverses the order of elements in the slice. '''

####### >>>>>>>>>>>>>>>>>>>>>  Modify List 
# Slicing can also be used to modify lists. You can replace elements within a list by assigning a new list to a slice of the original 
# list.
## ------ Replacing a Slice: 
# →  Replace single item with a new item
L[0] = 'orange'
print("replace single item with a new item: ", L)
L[-1] = 'violet'
print("replace single item with a new item: ", L)

# →  Replace multiple and equal number of items
#  Replace the elements from index 1 to 3 (inclusive) with the values 1, 2, and 3:
L[1:4] = [1, 2, 3]
print("Replace multiple and equal number of items: ", L) # output is ['red', 1, 2, 3, 'black']

# -- Replace multiple and unequal number of items
L[1:4] = [1, 2]
print("Replace multiple and unequal number of items: ", L) # output is ['red', 1, 2, 'black'] so size of the list has reduced

# -- Replace single element with multiple elements 
L[1:2] = ['green', 'blue', 'cyan', 'black']
print("Replace single element with multiple elements : ", L)

## ------ Insert/add Elements by Slice Assignment: 
# →  Insert at the start
# You can efficiently insert new elements into a list without replacing existing ones by specifying a zero-length slice.
L[:0] = [1, 2, 3]
print("Insert at the start: ", L)

# →  Insert at the end
# If you want to insert elements at the end, you can use a slice that starts at the current length of the list (L[len(L):]) and assign 
# the new elements there.
L[len(L):] = [1, 2, 3]
print("Insert at the end: ", L)

# →  Insert in the middle
# If you want to insert elements at the middle, slice with the same start and stop index, you can insert elements at
# the desired position within the list without overwriting any existing elements.
L[1:1] = [1, 2, 3]
print("Insert in the middle: ", L)

## ------ Insert/add items to a list by append() and extend() ;methods
''' We cannot specify position with append() and extend() method.
append() method - This method adds 1 item only to the end of the list. This method accepts only 1 argument otherwise type error will 
occurs. Also, appending a list creates a nested list.
extend() method - You can merge one list into another by using extend() method i.e., it takes a list as an argument and appends all of 
the elements. '''

L.append('yellow')
print("append() method - add single item: ", L)
# L.append('yellow', 'xyz')  # This method accepts only 1 argument so type error will occur

L.append(['yellow', 'xyz']) # This will create a nested list at the end
print("append() method - add list: ", L)

L.extend([1,2,3]) 
print("extend() method: ", L)

## ------ Insert/add items to a list by operator + 
L = L + [1,2,3]
print("Add items to a list by operator + :", L)    

## ------ Insert/add items to a list by augmented assignment operator +=
L += ['red', 'green', 'blue']
print("Add items to a list by augmented assignment operator +=: ", L)

## ------ Insert/add items to a list by insert() method
# insert() method - lets you insert an item at a specific position in a list. Note that all of the values in the list after the inserted
# value will be moved down one index.
L.insert(1,'blue')
print("Add items to a list by insert() method: ", L)

####### >>>>>>>>>>>>>>>>>>>>> Remove items from a list
## ------ Remove an Item by Index
# →  Remove single item
# →  → del statement:
del L[1]  # remove item at index 1
print("Remove single item by del statement: ", L)

# →  Remove Multiple Items
# →  →  del statement:
del L[1:3] # use the del keyword with a slice index and remove elements from index 1 to 3 (exclusive)
print("Remove multiple items by del statement: ", L)

# →  → by assigning an empty list to the desired slice
L[1:3] = [] # Remove elements from index 1 to 3 (exclusive)
print("Remove multiple items by  assigning an empty list to the desired slice: ", L)

## ------ Remove an Item by Value
# -- Remove single item
# →  → remove() method: With remove method() in lists, following points to note:
''' 
1. If the specified item is not present in the list, remove() method raises a KeyError -- ❌ KeyError 
2. The list is modified in-place and does not return a new list -- ✅ in-place
3. If the specified item is present multiple times (not possible in sets), only the first occurrence is removed -- ✅ only 1 item
4. If the list is empty, calling remove() will raise a KeyError -- ❌ KeyError
2. The Python remove() method can only take a single item to remove at a time. '''
L.remove('red') 
print("Remove an Item by Value by using remove() method: ", L)

'''NOTE - L.remove(100) -  ValueError: list.remove(x): x not in list
Additionally for list, there is no discard() method. L.discard(100) - throws attribute error. To avoid a ValueError, you can check if 
the item exists first, as shown below: '''
if 'red' in L:
    L.remove('red') 

# →  → pop() method: With pop method() in list, following points to note:
''' 
1. It removes the first occurrence of the specified value 
2. It removes 1 item at a time. 
3. Addremoved item can be accessed/viewed by assigning it to a variable
4. If the index is not specified, it removes and returns the last item in the list 
5. If the list is empty or the index is out of range, it raises an IndexError
'''
print("List before pop method: ", L)
x = L.pop(2) 
print("Remove single item by pop method: ", L, ", removed item is: ", x)
x = L.pop() # pop() removes and returns the last item in the list.
print("Remove single item by pop method: ", L, ", removed item is: ", x)

# -- Remove Multiple Items - no inbult function to remove multiple items at once by value

## ------ Remove all Items
La = [1, 2, 3, 4]
La.clear() # returns an empty list
print("Remove all Items: ", La)

####### >>>>>>>>>>>>>>>>>>>>> List Replication
print("List Replication: ", ['red', 'green', 'blue'] * 3)  # The replication operator * repeats a list a given number of times.

####### >>>>>>>>>>>>>>>>>>>>> List Length
print(len(L))

####### >>>>>>>>>>>>>>>>>>>>> Check if an item Exists in a List
# Check for presence
if 'red' in L:
    print('yes')

# Check for absence
if 'yellow' not in L:
    print('yes')

####### >>>>>>>>>>>>>>>>>>>>> Iterate Through a List
print("Loop through value ")
for val in L:
    print(val) 
# This works well if you only need to read the items of the list. But if you want to update them, you need the indexes. A common way 
# to do that is to combine the range() and len() functions.
print("Loop through index ")
for index in range(len(L)):
    print(index)

print("Loop through index and value together ")
for index, val in enumerate(L):
    print(index, val)

# Eg: Double each item of the list
La = [1, 2, 3, 4]
for i in range(len(La)):
    La[i] = La[i] * 2
print(La)
    
####### >>>>>>>>>>>>>>>>>>>>> Copy entire List (deep vs shallow copy)
'''In Python, when you assign one list to another (e.g., new_list = old_list), you're not creating a true copy. 
Instead, you are creating a new reference that points to the same underlying list object. Any changes made to either new_list or 
old_list will affect both, as they share the same data. This is neither shallow nor deep copy — it's just reference assignment. This 
happens because in Python, variables don't store objects directly. They store references (addresses) to objects in memory.

SHALLOW COPY: 
To create an actual copy of the list, you can use the slicing operator. By omitting both the start and stop indices (L2 = L1[:]), you 
create a copy of the entire list L1. This means L2 is a new list object containing the same elements as L1, but changes to one list
won't affect the other. A shallow copy creates:
→ A new list object
→ But does NOT copy the inner objects
→ Inner objects are shared
In short, Shallow copy means a new list is made, but if the original list contains mutable objects (like nested lists or dictionaries), 
those objects are not duplicated. Both lists share references to the same mutable objects.

DEEP COPY:
Deep Copy (copies everything recursively)
→ Creates a new outer list
→ Creates new inner lists
→ Creates new objects at all levels
For deeper copies where nested mutable objects are also duplicated, you can use the copy.deepcopy() function (if you need to copy nested
objects recursively)

NOTES - 1. Memory usage is Lower in shallow copy compared to deep copy
2. Execution speed is Faster in shallow copy compared to deep copy

One liner for interviews: Shallow copy duplicates the container but shares the contents, whereas deep copy duplicates both the 
container and all nested objects recursively.'''

a = [1, 2, 3]
b = a
b.append(4)
print("reference assignment: original list ---> ", a, "new list ---->", b)  # both list have been updated - a and b points to the same 
# list. No copy is made at all

# Create a shallow copy - Ways to make a shallow copy of a list
import copy
b = a.copy() # Method 1
b = list(a) # Method 2
b = a[:] # Method 3
b = copy.copy(a) # Method 4

# Eg 1: Shallow copy with simple elements (works “fine”)
a = [1, 2, 3]
b = a.copy()
b.append(4)
print("Create a shallow copy of a: ", a)  # [1, 2, 3]
print("Create a shallow copy of b: ", b)  # [1, 2, 3, 4]
print(b is a) # Output: False (Confirms they are different list objects)

# Eg 2: Shallow copy with nested lists (problem appears)
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print("Create a shallow copy of a: ", a)  # [[1, 2, 99], [3, 4]]
print("Create a shallow copy of a: ", b)  # [[1, 2, 99], [3, 4]]
# Why both list changed? a and b are different outer lists but both point to the same inner lists i.e., So modifying b[0] modifies the
# same inner object that a[0] points to. in short, only the outer list is copied. Inner objects are shared.

# Eg 3: Shallow copy with nested lists (no problem)
a = [[1, 2], 3, 4]
b = a.copy()
b.append(99)
print("Create a shallow copy of a: ", a)  # [[1, 2], 3, 4]
print("Create a shallow copy of a: ", b)  # [[1, 2], 3, 4, 99]

# Create a deep copy
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)

print(a)  # [[1, 2], [3, 4]]
print(b)  # [[1, 2, 99], [3, 4]] # Everything is copied recursively — no shared references.

####### >>>>>>>>>>>>>>>>>>>>> List Comprehension
''' A comprehension is a compact way of creating a Python data structure from iterators. With comprehensions, you can combine loops and 
conditional tests with a less verbose syntax. Comprehension is considered more Pythonic and often results in more readable code. 

List comprehension is a concise way to create lists in Python. It consists of brackets containing an expression followed by a for 
clause, and can include optional if clauses to filter items. List comprehensions provide a more compact and readable way to generate 
lists compared to traditional for loops. Here's the basic syntax:

                                    [expression for item in iterable if condition]
where,

→ expression: This is the return value or operation that produces the items to be included in the new list.
→ item: This represents each element in the iterable as the loop iterates over it.
→ iterable: This is the collection (like a list, tuple, or range) that you want to loop through. It can iterate over any type of 
iterable such as lists, strings, files, ranges, and anything else that supports the iteration protocol.
→ condition (optional): This is a filter that determines whether the item should be included in the new list. If the condition evaluates
 to True, the item is included; otherwise, it is skipped.

A comprehension is a compact way of creating a Python data structure from iterators. With comprehensions, you can combine loops and 
conditional tests with a less verbose syntax.

why you should use list comprehension more often? 
List comprehensions are more concise to write and hence they turn out to be very useful in many contexts.
Since a list comprehension is an expression, you can use it wherever you need an expression (e.g. as an argument to a function, in a 
return statement). List comprehensions run substantially faster than manual for loop statements (roughly twice as fast). It offers a 
major performance advantage especially for larger data sets.

List Comprehensions and Variable Scope:
In Python 2, the iteration variables defined within a list comprehension remain defined even after the list comprehension is executed.
For example, in [x for x in L], the iteration variable x overwrites any previously defined value of x and is set to the value of the 
last item, after the resulting list is created. Therefore, remember to use variable names that won't conflict with names of other local 
variables you have. Fortunately, this is not the case in Python 3 where the iteration variable remains private, so you need not worry.

Basic Example: Suppose you want to create a list of all integer square numbers from 0 to 4. You could build that list by appending one 
item at a time to an empty list:s'''
# Method 1 - append() method
L = []
L.append(0)
L.append(1)
L.append(4)
L.append(9)
L.append(16)
print(L) # Repeat same function again and square the numbers manually

# Method 2 - range() function
L = []
for x in range(5):
    L.append(x**2)
print(L)

# Method 3 - list comprehension : a more Pythonic way to build a list
L = [x**2 for x in range(5)]
print("List comprehension output: ", L)
# In this example, list comprehension has two parts.
# The first part collects the results of an expression on each iteration and uses them to fill out a new list.
# The second part is exactly the same as the for loop, where you tell Python which iterable to work on. Every time the loop goes over 
# the iterable, Python will assign each individual element to a variable x.

# Eg 1: List comprehension that uses string as an iterable - Repeat each character in the string 3 times
L = [x*3 for x in 'RED']
print("List comprehension that uses string as an iterable: ", L)

# Eg 2: List comprehension to apply an in-built function to each element in an iterable - Apply abs() function to all the elements in 
# a list.
L = [-4, -2, 0, 2, 4]
L = [abs(x) for x in L]
print("List comprehensions with built-in method abs(): ", L)

# Eg 3: List comprehension to apply an in-built function to each element in an iterable - Apply strip() function on each element in a 
# list to remove whitespace characters from the start and end of each string
L = ['  red  ', '  green  ', '  blue  ']
L = [x.strip() for x in L]
print("List comprehensions with built-in method strip(): ", L)

# Eg 4: List comprehension to create a list of (number, square) tuples
L = [(x, x**2) for x in range(6)]
print("List comprehensions to create a list of (number, square) tuples: ", L)    

# Eg 5: List Comprehension with if Clause - A list comprehension may have an optional associated if clause to filter items out of the 
# result. Filter list to exclude negative numbers
vec = [-4, -2, 0, 2, 4]
L = [x for x in vec if x >= 0]
print("List Comprehension with if Clause: ", L) # This will filter L and select elements which are >= 0
# This list comprehension is the same as a for loop that contains an if statement as shown below:
vec = [-4, -2, 0, 2, 4]
L = []
for x in vec:
    if x >= 0:
        L.append(x)
print(L)

# Eg 6: List Comprehension with multiple if Clause i.e., more than 1 condition - Filter positive even numbers 
vec = [-4, -2, 0, 1, 2, 3, 4]
L = [x for x in vec if x >= 0 if x % 2 == 0]
print(L)
# This is equivalent to:
vec = [-4, -2, 0, 1, 2, 3, 4]
L = []
for x in vec:
    if x >= 0:
        if x % 2 == 0:
            L.append(x) 
print(L) 

####### >>>>>>>>>>>>>>>>>>>>> Lambda Functions
''' Lambda functions are similar to user-defined functions but without a name. They're commonly referred to as anonymous functions.
They are efficient whenever you want to create a function that will only contain simple expressions - that is, expressions that are 
usually a single line of a statement. Syntax of lambda function is -
                                    lambda parameters (s) : expression

where, lambda: The keyword to define the function
parameters: A comma-separated list of input parameters (like in a regular function)
expression: A single expression that is evaluated and returned 

Anonymous function does not have a return keyword because it will automatically return the result of the expression in the function 
once it is executed.
'''
## ------ Lambda with single argument
s2 = lambda x:x*2
print("Lambda function to square a single number: ", s2(5))
s2 = lambda x: x.upper() 
print(s2('GeeksforGeeks'))

## ------ Lambda with multiple argument
'''NOTE - Lambda functions are limited to a single expression. They cannot contain multiple statements, assignments, or complex logic.
If you specify more than one expression, it will result in a SyntaxError. For example, the following lambda function is invalid:
s2 = lambda x:x-2
print( s2([10,20]) ) # throws syntax error
But if list has pre-defined meaning for operators then it will work. Eg: * is used to replicate the list'''
s2 = lambda x:x*2
print("Lambda function to repeat the list: ", s2([10,20]))  # replicates the list twice but dont perform element wise operation
'''If you want to double each element in the list, you can use the map() function along with a lambda function as shown below which 
will be discussed in detail later:'''
print("Lambda function to square list: ", list(map(lambda x: x ** 2, L)) )

## ------ Lambda without variable to store reference
a = 2
print(lambda x: a + 1) # gives memory location - <function <lambda> at 0x10121a2a0>
# If you dont want to store the reference of the lambda function in a variable then write it in the following way:
print((lambda x: x + 1)(2))
print((lambda x: x + 1)(10))

## ------ Lamba with if else (single condition)
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(" Lamba with if else (single condition): ", check(4))  
print(" Lamba with if else (single condition): ", check(7))

## ------ Lamba with if else (multiple condition)
print(" Lamba with if else (multiple condition): ", (lambda x: x*10 if x>10 else (x*5 if x<5 else x))(11) )

## ------ Lambda with multiple expressions
calc = lambda x, y: (x + y, x * y)
print("Lambda with multiple expressions: ", calc(3, 4))

## ------ Lambda with filter()
''' filter() function - when you want to focus on specififc value in an iterable, you can use filter function. Syntax is:
                                    filter(function, iterable)
Note that this filter function require another function based on which operation will be performed on the iterable.
Filter function is used to filter iterables based on a given condition. It returns elements that satisfy the conditions.'''
L = [33, 3, 22, 2, 11, 1]
print(filter(lambda x: x > 10, L)) # NOTE - will return <filter object at 0x1056efb20> which is memory location
print("Lambda with filter(): ", list(filter(lambda x: x > 10, L))) # NOTE - will return [33, 22, 11]
print("Lambda with filter(): ", list(filter(lambda x: x > 10, [33, 3, 22, 2, 11, 1])))

## ------ Lambda with map()
''' map() function - is used whenever you want to modify every value in an iterable. It applies the function to each item in an iterable
and returns an iteratir containing the result. Syntax is:
                                        map(function, iterable)
where, function refers to the function that you want to apply to each element
Iterable means elements that you want ti process'''
# Eg: Double each number in a list
a = [1, 2, 3, 4]
print("Lambda with map(): ", list(map(lambda x: x * 2, a)))

## ------ Lambda with reduce()
''' reduce() function - performs cummulative operation on iterable. 
How does it works? It starts with first elements of an iterable, applies the function to them, then uses the result with the next 
element. This process continues untill all elements are processed, resulting in a single cummulative value
Syntax:                        from functools import reduce
                                reduce(function, iterable, initializer)
where, initializer (optional) - refers to starting value for the accumulation '''
from functools import reduce
numbers = [1, 2, 3, 4, 1, 2, 3, 4]
print("Lambda with reduce(): ", reduce(lambda x, y: x + y, numbers, 0))
print("Lambda with reduce(): ", reduce(lambda x, y: x + y, numbers, 5))

''' One common pitfall when using the reduce() function is handling empty iterables. Passing an empty iterable to reduce() without 
an initializer raises a TypeError because there's no initial value to start the reduction process. To avoid this, always provide an 
initializer when the iterable might be empty.'''
numbers = []
print("pitfall with reduce(): ", reduce(lambda x, y: x + y, numbers, 0))

####### >>>>>>>>>>>>>>>>>>>>> List Comprehension vs map() and filter() with lambda
## ------ List Comprehension vs map() + lambda:
''' When all you're doing is calling an already-defined function on each element, map(f, L) is a little faster than the corresponding list 
comprehension [f(x) for x in L]. Following are 2 examples:
'''
# Eg 1: Convert each character in a string to uppercase
# With list comprehension
L = [x.upper() for x in 'foo']
print(" With list comprehension: ", L)
# With map() function
# L = list(map(str.upper(), 'foo')) # TypeError: unbound method str.upper() needs an argument
L = list(map(str.upper, 'foo'))
L = list(map(lambda x: x.upper(), 'foo'))
print( " With map() function: ", L)

'''However, when evaluating any other expression, [some_expr for x in L] is faster and clearer than map(lambda x: some_expr, L), because
# the map incurs an extra function call for each element. Following example creates a list of all integer square numbers. '''
# Eg 2: Create a list of all integer square numbers from 0 to 4
# With list comprehension
L = [x ** 2 for x in range(5)]
print(" With list comprehension: ", L)
# With map() function
L = list(map((lambda x: x ** 2), range(5)))
print(" With map() function: ", L)

## ------ List Comprehension vs filter() + lambda: 
''' List comprehension with if clause can be thought of as analogous to the filter() function as they both skip an iterable’s items for 
which the if clause is not true. Following example filters a list to exclude odd numbers.
'''
# With list comprehension
L = [x for x in range(10) if x % 2 == 0]
print(" With list comprehension: ", L)
# With filter() function
L = list(filter((lambda x: x % 2 == 0), range(10)))
print(" With filter() function: ", L) # As with map() function, filter() is slightly faster if you are using a built-in function.

''' Python List Methods
copy()	Returns a shallow copy of the list
count()	Returns the count of specified item in the list
index()	Returns the index of first instance of the specified item
reverse()	Reverses the items of the list in place
sort()	Sorts the items of the list in place'''

''' Built-in Functions with Lists: Python provides several built-in functions that can be used with lists. Here are some commonly used built-in functions:
1. all() - Returns True if all items in a list are true
2. any() - Returns True if any item in a list is true
3. enumerate() - Takes a list and returns an enumerate object  

all()	Returns True if all list items are true
any()	Returns True if any list item is true
enumerate()	Takes a list and returns an enumerate object
max()	Returns the largest item of the list
min()	Returns the smallest item of the list 
sorted()	Returns a sorted list
sum()	Sums items of the list'''

#################################################################
########### >>>>>>>>>>>>>>>>>> TUPLE >>>>>>>>>>>>>>>> ###########
#################################################################
print(" TUPLE Function begins", "*"*80)
''' A tuple is an ordered collection of items.
Tuples are a lot like lists:
1. Tuples are ordered - Tuples maintains a left-to-right positional ordering among the items they contain.
2. Accessed by index - Items in a tuple can be accessed using an index.
3. Tuples can contain any sort of object - It can be numbers, strings, lists and even other tuples.
except: Tuples are immutable - you can't add, delete, or change items after the tuple is defined.

You can create a tuple by placing a comma-separated sequence of items in parentheses ().
'''

####### >>>>>>>>>>>>>>>>>>>>> Create a tuple
## ------ Using round Braces ()
T = (1, 2, 3, 4, 5)
print("Create a tuple: ", T)

## ------ tuple constructor
T = tuple(('red', 'green', 'blue'))
print("Create a tuple with string: ", T)

## ------ tuple with mixed datatypes
T = (1, 'abc', 1.23, True)
print("Create a tuple with mixed datatypes: ", T)

## ------ empty tuple - A tuple containing zero items is called an empty tuple and you can create one with emptybrackets ()
T = ()
print("Create an empty tuple: ", T)

## ------ Create a tuple without parentheses
# NOTE - Parentheses are optional, except in the empty tuple case. a tuple is just a comma-separated list of values. You don’t need the 
# parentheses to create a tuple. It’s the trailing commas that really define a tuple. 
T = 1, 'abc', 1.23, True
print("Create a tuple without parentheses: ", T)

## ------ Singleton Tuple
T = (4,)
print("Check type of Singleton Tuple: ", type(T))
# If you have only one value in a tuple, you can indicate this by including a trailing comma , just before the closing parentheses.
# Otherwise, python will think you’ve just typed a value inside regular parentheses i.e., 4 is recognized as an integer, not a tuple as
# shown below:
T = (4)
print(type(T))

####### >>>>>>>>>>>>>>>>>>>>> tuple with other data structures
# Convert a list to a tuple
T = tuple([1, 2, 3]) # or ([1, 2, 3])
print("Convert a list to a tuple: ", T)

# Convert a string to a tuple
T = tuple('abc') # or ('a', 'b', 'c')
print("Convert a string to a tuple: ", T)

# Nested Tuples
T = ('red', ('green', 'blue'), 'yellow')
print("Create Nested Tuples: ", T)

####### >>>>>>>>>>>>>>>>>>>>> Access Tuple Items
## ------ by values/item 
T = ('red', 'green', 'blue', 'cyan', 'yellow', 'orange')
print("Access tuple Index: ", T.index('green')) 
''' index() method - Find Index of Item in the tuple and gives index of first occurence
syntax:                                      tuple.index(element, start, end)
L.index('red', 'blue') - throws error (TypeError: slice indices must be integers or have an __index__ method). Therefore, can access
only single item at a time.
It searches the tuple for a specified value and returns the position of where it was found'''

## ------ by index - using an index in square brackets. Note that tuple indexing starts from 0.
print("Access Tuple Items: ", T[0]) # first item
print("Access Tuple Items: ", T[2]) # third item   

# → Negative Indexing: 
# NOTE - You can access a tuple by negative indexing as well. Negative indexes count backward from the end of the tuple. So, T[-1] 
# refers to the last item, T[-2] is the second-last, and so on.
print("Access Tuple Items - negative indexing: ", T[-1]) # last item
print("Access Tuple Items - negative indexing: ", T[-3]) # third-last item

# → Out of range Index: 
# print(T[20]) # IndexError: tuple index out of range

## ------ Access Nested tuple Items:
Ta = ('red', ('green', 'blue'), 'yellow')
print("Access Nested tuple Items: ",Ta[1][0]) # Accessing nested tuple item - output is 'green'
print("Access Nested tuple Items but non nested element: ",Ta[2][0]) # Accessing nested tuple item - output is 'y'

####### >>>>>>>>>>>>>>>>>>>>> Slicing a Tuple
''' You can access a range of items in a tuple by using the slicing operator colon : inside square brackets.
To access a range of items in a tuple, you need to slice a tuple using a slicing operator. Tuple slicing is similar to list slicing.'''
print(T[1:4]) # items from index 1 to 3
print(T[:3])  # items from start to index 2
print(T[2:])  # items from index 2 to end
print(T[:])   # all items
print(T[3:-1]) # items from index 3 to second-last item
print(T[::2])  # items with step 2- ('red', 'blue', 'yellow')
print(T[1::2]) # items with step 2 starting from index 1 - ('green', 'cyan', 'orange')

## ------ Slicing with out of range indexes
print(T[30:4]) # ()
print(T[3:40]) # ('cyan', 'yellow', 'orange')
print(T[1:4:40]) # ('green',)

## ------ Slicing with 0 arguments
print(T[30:0]) # ()
print(T[0:40]) # ('red', 'green', 'blue', 'cyan', 'yellow', 'orange')
# print(T[1:4:0]) # ValueError: slice step cannot be zero

## ------ Slicing with start index greater than end index
print(T[30:2]) # ()

####### >>>>>>>>>>>>>>>>>>>>>  Reversing a Tuple
print(T[::-1]) # items in reverse order - ('orange', 'yellow', 'cyan', 'blue', 'green', 'red')

####### >>>>>>>>>>>>>>>>>>>>> Modify Tuple Items 
# Tuples are immutable, meaning you cannot change, add, or remove items after the tuple is created. The tuple immutability is applicable
# only to the top level of the tuple itself, not to its contents. For example, a list inside a tuple can be changed as usual.
T = (1, [2, 3], 4)
T[1][0] = 'xx'
print("Change Tuple Items - first way: ", T)

# Another way to change tuple items - Convert the tuple to a list, make changes, and then convert it back to a tuple.
T = ('red', 'green', 'blue', 'cyan', 'yellow', 'orange')
L = list(T) # Convert tuple to a list
L[1] = 'yellow' # Change the list
T = tuple(L) # Convert the list back to a tuple
print("Change Tuple Items - second way: ", T)

####### >>>>>>>>>>>>>>>>>>>>> Remove Tuple Items 
# Delete a Tuple: Tuples cannot be modified, so obviously you cannot delete any item from it so pop(), remove(), discard() method will
# not work. However, you can delete the tuple completely with del keyword.
T = ('red', 'green', 'blue')
del T
# print("Delete a Tuple: ", T) # NameError: name 'T' is not defined. Did you mean: 'Ta'?

####### >>>>>>>>>>>>>>>>>>>>> Count occurence of an item in a tuple
T = ('red', 'green', 'blue', 'cyan', 'yellow', 'orange')
# count() method - Returns the number of times a specified value occurs in a tuple
print("count occurence of an item in a tuple - count() method: ", T.count('green'))

####### >>>>>>>>>>>>>>>>>>>>> Tuple Concatenation
''' Concatenate - Tuples can be joined using the concatenation operator +
Since tuples are immutable, you cannot add items to an existing tuple. However, you can create a new tuple that is the concatenation 
of the existing tuple and the new items. '''
T = ('red', 'green', 'blue') + (1, 2, 3)
print("Tuple Concatenation: ", T)

####### >>>>>>>>>>>>>>>>>>>>> Tuple Repetition
# Replicate - Tuples can be joined using the Replication operator *
T = ('red',) * 3
print("Tuple Replication: ", T)

####### >>>>>>>>>>>>>>>>>>>>> Tuple Length
# To find how many items a tuple has, use len() method.
T = ('red', 'green', 'blue')
print(" Tuple Length: ", len(T))

####### >>>>>>>>>>>>>>>>>>>>> Check if item exists in a tuple
# Check for presence
T = ('red', 'green', 'blue')
if 'red' in T:
    print('yes')

# Check for absence
T = ('red', 'green', 'blue')
if 'yellow' not in T:
    print('yes')

####### >>>>>>>>>>>>>>>>>>>>> Iterate through a tuple
T = ('red', 'green', 'blue')
for item in T:
    print(item)

'''Tuple Sorting: Since tuples are immutable, they do not have a sort() method like lists. However, you can sort a tuple by converting 
it to a list, sorting the list, and then converting it back to a tuple. There are two methods to sort a tuple.
Method 1: Use the built-in sorted() method that accepts any sequence object. It returns a new sorted list from the elements of the given
tuple.
Method 2: Convert a tuple to a mutable object like list (using list constructor), gain access to a sorting method call (sort()) and 
convert it back to tuple.
'''
# Method 1: Using sorted() method
T = ('cc', 'aa', 'dd', 'bb')
print(tuple(sorted(T)))
# Method 2: Converting to list, sorting, and converting back to tuple
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)    # convert tuple to list
tmp.sort()       # sort list
T = tuple(tmp)   # convert list to tuple
print(T) 

''' Built-in Functions with Tuples: Python provides several built-in functions that can be used with tuples. Here are some commonly used built-in functions:
1. all() - Returns True if all items in a tuple are true
2. any() - Returns True if any item in a tuple is true
3. enumerate() - Takes a tuple and returns an enumerate object
5. max() - Returns the largest item of the tuple
6. min() - Returns the smallest item of the tuple
7. sorted() - Returns a sorted list of the tuple's items


all()	Returns True if all tuple items are true
any()	Returns True if any tuple item is true
enumerate()	Takes a tuple and returns an enumerate object
max()	Returns the largest item of the tuple
min()	Returns the smallest item of the tuple
sorted()	Returns a sorted tuple
sum()	Sums items of the tuple'''

###################################################################
########### >>>>>>>>>>>>>>>>>> STRINGS >>>>>>>>>>>>>>>> ###########
###################################################################
print(" STRINGS Function begins", "*"*80)
''' Strings are ordered collections of Unicode characters. The values in a strings are called characters. Strings are defined by 
enclosing characters in single quotes ' ' or double quotes " ". You can create a multiline string using triple-quotes: """  """ or 
'''  '''. STRING PROPERTIES::
→ Strings are ordered
→ Accessed by index -  each character has a specific position (index)
→ Strings can contain any sort of character - letters, numbers, symbols, whitespace characters etc.
→ Strings are immutable - you cannot change a string in-place after it is created. Any operation that seems to modify a string actually 
creates a new string with the desired changes.
'''

####### >>>>>>>>>>>>>>>>>>>>> Create a string
## ------ Using single or double quotes
St = 'Hello, World!'  # single quotes
print("Create a string - first way: ", St)

St = "Hello, World!"   # double quotes
print("Create a string - second way: ", St)

## ------ Using str() Constructor
St = str('Hello, World!')  # str() constructor
print("Create a string - third way: ", St)

## ------ create strings with mixed data types 
St = "123 abc 1.23 True"
print("Create a string with mixed data types : ", St)

## ------ create an empty string using several methods: 
St = '' # Single Quotes
St = "" # Double Quotes
St = """""" # Triple Quotes Triple Quotes (for multiline contexts): 
St = str() # str() Constructor
print("Create an empty string: ", St)

## ------ strings within parentheses
# You can also put several strings within parentheses to join them together. This feature is useful when you want to break long strings.
S = ('Put strings within parentheses '
    'to join them together.')
print(S)

## ------ Nested string:
# In Python, the term "nested string" usually refers to using one string literal delimiter inside another string, or, more commonly, 
# to nested f-strings (formatted string literals) for dynamic formatting which will be covered later. 

####### >>>>>>>>>>>>>>>>>>>>> strings with other data structures
# Number to a string
St = str(123)
print("Number to a string - value: ", St)   
print("Number to a string - type: ", type(St))

# List to a string
St = str([1,1])
print("List to a string - value: ", St)
print("List to a string - type: ", type(St))

####### >>>>>>>>>>>>>>>>>>>>> Access Characters 
## ------ by values/item 
# → find(): 
# Returns the index of the first occurrence (lowest index ) of the specified value or substring. If the value is not found or string is 
# empty, it returns -1.
St = "programming"
print("The first 'r' is at index by find(): ", St.find('r') )
St = "programming helps a lot"
print("The first 'lot' is at index by find(): ", St.find('lot') )

# → index(): 
# Returns the index of the first occurrence of the specified value. If the value is not found or string is empty, it raises a ValueError. 
print("The first 'r' is at index by index(): ", St.index('r') )
St = "programming helps a lot"
print("The first 'lot' is at index by index(): ", St.index('lot') )

## ------ by Index 
# You can access individual characters in a string using an index in square brackets. The string indexing starts from 0.
# → Positive Indexing: 
print(St[0])  # first character
print(St[7])  # eighth character

# → Negative Indexing: 
print(St[-1]) # last character
print(St[-5]) # fifth-last character

# → Out of range Index: 
# print(St[20]) # IndexError: string index out of range

####### >>>>>>>>>>>>>>>>>>>>> Slicing a String
''' Theory of slicing of a string is same as that of list slicing. Refer to list slicing section for more details.
Note that a slice of a string is also a string'''
St = "programming"
print(St[0:5])  # characters from index 0 to 4
print(St[7:12]) # characters from index 7 to 11
print(St[:5])   # characters from start to index 4
print(St[7:])   # characters from index 7 to end
print(St[:])    # all characters
print(St[2:-2]) # characters from index 2 to second-last character   
print(St[1:6:2]) # characters from index 1 to 5 with a step of 2


## ------ Slicing with out of range indexes
print("Slicing with out of range indexes - start = out of range: ", St[30:4]) # nothing - empty space
print("Slicing with out of range indexes - end = out of range: ", St[3:40]) # gramming
print("Slicing with out of range indexes - step = out of range: ", St[1:4:40]) # r

## ------ Slicing with 0 argument
print("Slicing with 0 argument - start = 0: ",  St[30:0]) # nothing - empty space
print("Slicing with 0 argument - end = 0: ",  St[0:40]) # programming
# print("Slicing with 0 argument - step = 0: ",  St[1:4:0]) # ValueError: slice step cannot be zero

## ------ Slicing with start index greater than end index
print("Slicing with start index greater than end index: ", St[30:2]) #  nothing - empty space

####### >>>>>>>>>>>>>>>>>>>>>  Reversing a string
print("Reversing a string: ",St[::-1]) # characters in reverse order 

####### >>>>>>>>>>>>>>>>>>>>>  String Concatenation: 
# You can concatenate (join) two or more strings together to form a new string in several ways:
## ------ String concatenation by operator
S = 'Hello,' + ' World!'
print("String concatenation by operator: ", S)

## ------ String concatenation by augmented assignment operator
S = 'Hello,'
S += ' World!'
print("String concatenation by augmented assignment operator: ",S)

## ------ Implicit concatenation
# In Python, two or more strings next to each other are automatically concatenated, known as Implicit concatenation
S = 'Hello,' " World!"
print("Implicit concatenation: ", S) 

# NOTE - Implicit concatenation only works with two string literals though, not with variables or expressions.
str1 = 'Hello,'
str2 = ' World!'
# S =  str1 str2  # This will raise an error because part1 and part2 are variables and not string literals.
# s = "hello" str(123) # This will also raise an error because str(123) is a function call and not string literal. str(123) result is 
# known only at runtime. Therefore, concatenation cannot be done implicitly.
S = str1 + str2  
print(S)

####### >>>>>>>>>>>>>>>>>>>>> String Formatting/String Interpolation
''' In Python, there are three major ways to embed variables inside a string.
1. printf-style % String Formatting
2. str.format() Built-in Method
3. f-String Formatter '''

## ------ printf-style % string formatting
S = '%s is %d years old.' % ('Bob', 25)
print("printf-style % string formatting: ", S)

## ------  format() Built-in Method
S = '{1} is {0} years old.'.format(25, 'Bob')
print("str.format() Built-in Method: ", S)

## ------  f-String Formatter
name = 'Bob'
age = 25
S = f"{name} is {age} years old."
print("f-String Formatter: ", S)

# f-String Formatter using for concatenation
str1 = "Hello"
str2 = "World"
result = f"{str1} {str2}"
print("Using f-strings (Formatted String Literals): ", result)

####### >>>>>>>>>>>>>>>>>>>>> Modify a String 
''' Strings are immutable, meaning you cannot change, add, or remove characters after the string is created i.e., individual characters 
of the existing string cannot be changed. The best you can do is create a new string that is a variation of the original. Therefore,
S = 'Hello, World!'
S[0] = 'h'  -- This will raise an error because strings are immutable in Python. 
Concatenation always creates a new string rather than modifying the existing one.'''
new_S = 'J' + St[1:]
print(new_S) # returns Jrogramming
St = 'J' + St[1:]
print(St) # returns Jrogramming

''' QUESTION 1 - We learned that Strings are immutable but above codes is working St = 'J' + St[1:] print(St) # returns Jrogramming.
Is this a contradiction to theory? Explain

Immutability = the existing string object cannot be modified in place i.e., Changing characters inside the same string object. Once a 
string object is created, its characters and length are frozen.
What is allowed? 
→ Creating new strings
→ Reassigning a variable to point to a different string object

What actually happens internally (step-by-step)?
→ "programming" is created in memory
→ St[1:] creates a new string → "rogramming"
→ 'J' + "rogramming" creates another new string → "Jrogramming"
→ St = ... rebinds the variable St to this new string
⚠️ The original "programming" string was never modified

QUESTION 2 - How can we check if the original string is intact or not in python?
you can't “check” a string object directly once you've lost the reference — but you can prove it using object identity (id) or multiple 
references.'''
# Proof 1: 
St = "programming"
print("Check memory address of St:", id(St))
St = 'J' + St[1:]
print("Check memory address of St after concatenation:",id(St)) # Different ids = different objects
# Proof 2:
s1 = "programming"
s2 = s1   # second reference
s1 = 'J' + s1[1:]
print(s1)  # Jrogramming
print(s2)  # programming
'''s2 still points to the original string. If strings were mutable, s2 would also change. Since it didn't → immutability confirmed ✅ '''

## ------ Replace Text Within a String: use the replace() method to create a new string with specified text replaced by new text. If 
# the string to replace is not found, the original string is returned unchanged.
print("Original String: ", St) # programming
new_S = St.replace('World', 'Universe') # returns actual string - programming
new_S = St.replace('ing', 'ers') # returns programmers
print(new_S)
St = St.replace('ing', 'ers') # returns programmers
print(St)
'''NOTE - Again St returns programmers. Why?
str.replace() does NOT modify the string. It returns a new string.
Again - Original string → unchanged and New string → created. Variable St → now refers to the new string'''

## ------ Split strings: 
# Use split() method to chop up a string into a list of substrings, around a specified delimiter. And each substring becomes an item in
# the list which can be accessed by index.
St = 'apple, banana, cherry'
fruits = St.split(',')
print('Split strings: ', fruits, fruits[0])

## ------ join() method : .
'''the join() method is used to concatenate elements of an iterable (such as a list, tuple, or dictionary keys) into a single string 
with a specified delimiter in between. Syntax is as follows:
                                                'delimiter'.join(iterable)
'''
St = '-'.join(fruits) # fruits is iterable - list of strings
print('join strings: ', St)

# It does not join two individual strings directly in the way you might expect
St = 'Hello'.join("world")
print('join strings: ', St) # returns wHellooHellorHellolHellod - after each letter/character of "world", Hello is joined.
# To join two individual strings with a specific character in between, you can use the join() method in following way:
str1 = "Hello"
str2 = "World"
result = " ".join([str1, str2])

# If iterable is empty, join() returns an empty string even though separator is specified.
L = []
print("If iterable is empty, join() returns an empty string : ", 'abc -'.join(L)) 
print("If iterable is empty, join() returns an empty string : ", '-'.join(L)) 

####### >>>>>>>>>>>>>>>>>>>>> Remove characters from a string
# Strings do not have a pop(), remove(), discard() method. Strings are immutable in Python, meaning their contents cannot be changed 
# after creation. Methods like pop() that modify the object in place are not available for strings. To get a string with a character 
# removed, you would use string slicing or other string manipulation techniques to create a new string. 

####### >>>>>>>>>>>>>>>>>>>>> String Repetition: You can repeat a string multiple times using the * operator.
St = 'Hello! ' * 3
print(St)        
St = '-' * 20
print(St)

####### >>>>>>>>>>>>>>>>>>>>> String Length
St = 'Hello, World!'
print(len(St))   

####### >>>>>>>>>>>>>>>>>>>>> String Case Conversion
'''Python provides five methods to perform case conversion on the target string viz. lower(), upper(), capitalize(), swapcase() and 
# title()'''
S = 'Hello, World!'
print(S.lower())       # Convert to lowercase
print(S.upper())       # Convert to uppercase
print(S.capitalize())  # Capitalize first character
print(S.swapcase())    # Swap case
print(S.title())       # Title case     

####### >>>>>>>>>>>>>>>>>>>>> Check if Substring Contains in a String
''' To check if a specific text is present in a string, use in operator. The in is a boolean operator, which takes two strings 
and returns True if the first appears as a substring in the second. '''
S = 'Hello, World!'
## ------ Check for presence
if 'World' in S:
    print('yes')

## ------ Check for absence
if 'Universe' not in S:
    print('yes')

## ------ Check for Empty String
'''The most "Pythonic" and common way to check if a string is empty is by leveraging its "falsy" nature in a boolean context. An empty 
string evaluates to False in a boolean expression, while a non-empty string evaluates to True.  '''
S = ''
if not S: # A more concise, Pythonic way for most use cases:
    print("String is empty")    

## ------ Check for None or Empty String
''' Important Distinction of Empty String vs. None - In Python, an empty string ("") is a valid string object with zero characters, 
whereas None is a special constant representing a null value or the absence of a value. '''
s = None
if s is None or s == "":
    print("Variable is None or empty string")

####### >>>>>>>>>>>>>>>>>>>>> Iterate Through a String  
S = 'Hello, World!'
## ------ Loop through value 
for val in S:
    print("Loop through value: ", val)   

## ------ Loop through index
for index in range(len(S)):
    print("Loop through index: ", index) 

## ------ Loop through index and value together
for index, val in enumerate(S):
    print("Loop through index and value together: ", index, val)

####### >>>>>>>>>>>>>>>>>>>>> Python Escape Sequence
''' You can use quotes inside a string, as long as they don't match the quotes surrounding the string. '''
S = 'It\'s a beautiful day!'
print(S)
S = "He said, \"Hello!\""
print(S)    
S = "We're open"		# Escape single quote
S = "I said 'Wow!'"		# Escape single quotes
S = 'I said "Wow!"'		# Escape double quotes
''' This is fine for most of the time but what if you want to declare a string with both single and double quotes like:
Python will raise a SyntaxError, because both quotation marks are special characters. The solution to avoid this problem is to use the 
backslash escape character \. Prefixing a special character with \ turns it into an ordinary character. This is called escaping.'''
S = "Bob told me, \"Sam said, 'This won't work.'\""
print(S)

# Backslash escape character is used in representing certain special characters like: \n is a newline, \t is a tab. These are known as 
# escape sequences.
S = str('First line.\n\tSecond line.')
print(S)

####### >>>>>>>>>>>>>>>>>>>>> Raw String: 
# Sometimes you may want to ignore escape sequences in a string. You can do this by prefixing 
# the string with the letter r or R to create a raw string. Suppose you have stored a file path inside a string. When you execute it, 
# you will get a result like this:
file_path = "C:\new_folder\test.txt"
print(file_path)  # Output may not be as expected due to escape sequences
# To avoid this, you can use a raw string:
file_path = r"C:\new_folder\test.txt"
print(file_path)  # Output will be as expected
# Here, \n is interpreted as newline and \t as tab.
# If you don’t want characters prefaced by \ to be interpreted as special characters, you can declare the string as a raw string, by 
# adding an r before the first quote.


''' Python String Methods
capitalize()	Capitalizes first character of the string
casefold()	Returns a casefolded string
center()	Returns center-aligned string
count()	Counts occurrences of a substring in a string
encode()	Return an encoded version of the string as a bytes object
endswith()	Determines whether the string ends with a given suffix
expandtabs()	Replaces tabs with spaces
format()	Perform a string formatting operation
format_map()	Perform a string formatting operation
isalnum()	Determines whether the string contains alphanumeric characters
isalpha()	Determines whether the string contains alphabetic characters
isdecimal()	Determines whether the string contains decimal characters
isdigit()	Determines whether the string contains digits
isidentifier()	Determines whether the string is a valid Python identifier
islower()	Determines whether string contains lowercase characters
isnumeric()	Determines whether the string contains numeric characters
isprintable()	Determines whether string contains printable characters
isspace()	Determines whether the string contains only whitespace characters
istitle()	Determines whether the string is a titlecased string
isupper()	Determines whether string contains uppercase characters

ljust()	Returns left-aligned string
lstrip()	Strips characters from the left end of a string
maketrans()	Returns a translation table to be used in translations
partition()	Divides a string based on a separator
replace()	Replaces occurrences of a substring within a string
rfind()	Searches the string for a given substring
rindex()	Searches the string for a given substring
rjust()	Returns right-aligned string
rpartition()	Divides a string based on a separator
rsplit()	Splits a string into a list of substrings
rstrip()	Strips characters from the right end of a string
split()	Splits a string into a list of substrings
splitlines()	Splits the string at line breaks
startswith()	Determines whether the string starts with a given substring
strip()	Strips leading and trailing characters
swapcase()	Swaps case of all characters in a string
title()	Converts string to “Title Case”
translate()	Returns a translated string

zfill()	Pads a string on the le with zeros
'''

###################################################################
########### >>>>>>>>>>>>>>>>>> DICTIONARY >>>>>>>>>>>>>>>> ######
###################################################################
print(" Dictionary Function begins", "*"*80)

''' A dictionary is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that 
hold
only a single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.
You can think of a dictionary as a mapping between a set of indexes (known as keys) and a set of values. Each key maps to a value. The
association of a key and a value is called a key:value pair or sometimes an item.

PTBN - Keys must be unique: A key can appear in a dictionary only once. Even if you specify a key more than once during the creation of 
a dictionary, the last value for that key becomes the associated value i.e., the first occurrence of ‘name’ is replaced by the second 
one.

Key must be immutable type: You can use any object of immutable type as dictionary keys – such as numbers, strings, booleans or tuples.
An exception is raised when mutable object is used as a key (TypeError).

Value can be of any type: There are no restrictions on dictionary values. A dictionary value can be any type of object and can appear 
in a dictionary multiple times.

The order of key:value pairs is not always the same. In fact, if you write the same example on another PC, you may get a different 
result. In general, the order of items in a dictionary is unpredictable. But this is not a problem because the items of a dictionary 
are not indexed with integer indices.
'''

####### >>>>>>>>>>>>>>>>>>>>> Create a Dict
## ------ Using curly Braces {}
D = {'name': 'Neslihan',
     'age': 25,
     'job': 'Dev',
     'city': 'New York',
     'email': 'Neslihan@web.com'}
print(" Create Dictionary using curly braces: ", D)

## ------ Using Dict constructors
D = [('name', 'Sevgi'), ('age', 30), ('job', 'Data_Scientist')]
print(" Create Dictionary using constructor: ",dict(D))

## ------ An empty Dict
D = {}
print(" Create an empty Dictionary: ", D)

####### >>>>>>>>>>>>>>>>>>>>> Dict constructors
## ------ When the keys are simple strings, it is sometimes easier to specify key:value pairs using keyword arguments.
D = dict(name = 'Neslihan', age = 30, job = 'Developer')
print("When the keys are simple strings: ", D)

## ------ Tuple to a Dict
D = (['name', 'Sevgi'], ['age', 30], ['job', 'Data_Scientist'])
print("Tuple to a Dict: ", dict(D))

## ------ List to a Dict: using zip function - This is used to combine separate lists of keys and values obtained dynamically at runtime.
keys = ['name', 'age', 'job']
values = ['Neslihan', 30, 'Developer']
print("List to a Dict using zip function: ", dict(zip(keys, values)))

## ------ create a dictionary with default values for each key - use fromkeys() method
keys = ['name', 'age', 'job']
defaultValue = 0
print("Create dict with default values: ", dict.fromkeys(keys,defaultValue) )

####### >>>>>>>>>>>>>>>>>>>>> Access Dictionary by Items/values
## ------ Access by keys
# →  Access all keys - use keys() method
D = dict(name = 'Neslihan', age = 30, job = 'Developer')
print("Access Keys: ", list(D.keys())) # returns ['name', 'age', 'job']
print("Access Keys: ", D.keys()) # returns dict_keys(['name', 'age', 'job'])
# print("Access Keys: ", D.keys('name')) # TypeError: dict.keys() takes no arguments (1 given)

# →  Access particular key - use  square brackets []
print(" Access by particular key - single key: ", D['name'])
# print("Access by keys: ", D['name', 'age']) # KeyError: ('name', 'age')
print(" Access by particular key - multiple key: ", D['name'], D['age'])

# →  Access particular key - use get() method
''' NOTE - If you refer to a key that is not in the dictionary, you'll get an exception Eg: print(D['salary']) - Triggers KeyError: 
'salary'. To avoid such exception, you can use the special dictionary get() method. This method returns the value for key if key is in 
the dictionary, else None, so that this method never raises a KeyError. '''
print(" Access particular key - single key: ", D.get('name'))
print(" Access particular key - single key: ", D.get('salary')) # Prints None
# You can also specify a default return value other than None, by providing a second argument to the get() method.
print(" Access particular key - single key: ", D.get('salary', 'Not Found')) # Prints Not Found
# get() method cannot be used to fetch multiple values simultaneously
print(" Access particular key - single key: ", D.get(('name','age'))) # Prints None

# →  Access multiple keys
'''To fetch multiple values from a Python dictionary simultaneously using a list of keys, the most common and Pythonic approaches 
involve list comprehensions or using the map() function with dict.get(). There is no single built-in dictionary method specifically for 
this task. '''

## ------ Access values
print("Access values: ", list(D.values()))

## ------ Access Key:Value pairs
print("Access Key:Value pairs: ", list(D.items()))

####### >>>>>>>>>>>>>>>>>>>>> Modify Dictionary Items
## ------ Inset/add/update/ replace keys and value pairs
''' Refer to the item by its key and assign a value. If the key is already present in the dictionary, its value is replaced by the new 
one. If not present then it will add new key:value pair to the dictionary. In Python, you cannot add multiple key-value pairs 
simultaneously using only the square brackets ([]) notation. The square bracket notation with assignment (dict[key] = value) is used 
for adding or updating a single key-value pair at a time. '''
D['name'] = 'Neria'
print("Update Dictionary Items: ", D)

D['city'] = 'Baba Kale'
print("Add Dictionary Items: ", D)

## ------ Merge Two Dictionaries
'''built-in update() method to merge the keys and values of one dictionary into another. Note that this method blindly overwrites 
values of the same key if there's a clash.'''
D1 = D
D2 = {'age': 30, 'city': 'Ibiza', 'email': 'neria_ally@web.com'}
D1.update(D2)
print(" Merge Two Dictionaries: ", D1)

# The update() method accepts another dictionary or an iterable of key-value pairs (like a list of tuples) as an argument and adds 
# them to the existing dictionary
D2 = [('c', 3), ('d', 4), ('e', 5)]
D.update(D2)
print("update() method with another iterable (tuple) :", D)

# For Python 3.9 and later, you can use the dictionary merge (|) operator to create a new dictionary with combined key-value pairs. 
# print(D1 | D2) # Its not supported in this version of python
from collections import defaultdict
dic = defaultdict(list)
lst = ['A', "zyz", 'lpq', 'ryt']
for i in lst:
    dic[i].append(i)
print("test:" , dic)
breakpoint()
####### >>>>>>>>>>>>>>>>>>>>> Remove Item 
## ------ Remove by Key
# →  pop method
'''in dict pop() takes a required argument, which is the key of the item to be removed and returned. An optional second argument can be 
provided as a default value to be returned if the specified key is not found (instead of raising a KeyError). If no default is 
provided and the key is missing, it raises a KeyError.'''
x = D.pop('email')
print("Remove an Item by Key using pop method: ", D)
print("Get removed value: ", x) 

# → del statement
del D['age']
print("Remove an Item by Key using del statement: ", D)

# →  Remove Last Inserted Item - popitem() method removes and returns the last inserted item.
x = D.popitem()
print("Remove Last Inserted Item by popitem() method :", D)
print("Get removed pair", x)

## ------ Remove by value
# Python, dictionaries do not have a built-in method to remove a key-value pair directly by its value. Instead, you need to iterate 
# through the dictionary to find the corresponding key(s) and then use a method like pop()

## ------ Remove all Items- delete all keys and values from a dictionary, use clear() method
D.clear()
print("Remove all Items: ", D)

####### >>>>>>>>>>>>>>>>>>>>> Iterate Through a dictionary
D = dict(name = 'Neslihan', age = 30, job = 'Developer')

## ------ Loop through keys
for key in D:
    print("Loop through keys - first way: ", key) 
for key in D.keys():
    print("Loop through keys - second way: ", key) 

## ------ Loop through value
for val in D.values():
    print("Loop through value - first way: ", val) 
for key in D:
    print("Loop through value - second way: ", D[key])

## ------ Loop through key and index of keys together
for key, val in enumerate(D): # keys index and value it loops through
    print("Loop through index and value together - first way: ", key, val)    
print("")
for key, val in D.items():
    print("Loop through index and value together - first way: ", key, val)

####### >>>>>>>>>>>>>>>>>>>>> Check if a Key or Value Exists
## ------ Check if a Key Exists
print("Check if a Key or Value Exists: ", 'name' in D)
print("Check if a Key or Value Exists: ", 'salary' in D)

## ------ Check if a value Exists
print("To check if a certain value exists in a dictionary: ", 'Defne' in D.values())
print("To check if a certain value exists in a dictionary: ", 'Neria' in D.values())

## ------ in Operator on List vs Dictionary
''' The in operator uses different algorithms for lists and dictionaries. For lists, it uses a search algorithm. As the list gets 
longer, the search time gets longer. For dictionaries, Python uses a different algorithm called Hash Table, which has a remarkable 
property: the operator takes the same amount of time, regardless of how many items are in the dictionary.'''

####### >>>>>>>>>>>>>>>>>>>>> Dict Length
print("Dict Length: ", len(D))

####### >>>>>>>>>>>>>>>>>>>>> Dictionary Comprehension
''' Dictionary comprehensions follow the same pattern as list comprehensions, but create dictionaries instead of lists. It saves you 
having to write several lines of code, and keeps the readability of your code neat. Syntax is as follows:: 
                            {key_expression : value_expression for item in iterable if conditional_expression}

eg: Suppose you want to create a dictionary of numbers & squares '''
## ------ By inserting one item at a time into an empty dictionary
D = {}
D[0] = 0
D[1] = 1
D[2] = 4
D[3] = 9
D[4] = 16
print("By inserting one item at a time into an empty dictionary: ", D)

## ------ using for loop
D = {}
for x in range(5):
    D[x] = x**2
print("using for loop: ", D)

## ------  Dict comprehension
D = {x: x**2 for x in range(5)}
print(" Dict comprehension: ", D)
'''dictionary comprehension has two parts:
1. The first part collects the key/value results of expressions on each iteration and uses them to fill out a new dictionary.
2. The second part is exactly the same as the for loop, where you tell Python which iterable to work on. Every time the loop goes over 
the iterable, Python will assign each individual element to a variable x.'''
breakpoint()
# Eg2:
# Dictionary comprehensions can iterate over any type of iterable such as lists, strings, files, ranges, and anything else that supports 
# the iteration protocol.
D = {c: c * 3 for c in 'RED'}
print(D)

# Eg3:
L = ['ReD', 'GrEeN', 'BlUe']
D = {c.lower(): c.upper() for c in L}
print(D)

####### >>>>>>>>>>>>>>>>>>>>> Extracting a Subset of a Dictionary
D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selectedKeys = [0, 2, 5]
X = {k: D[k] for k in selectedKeys}
print(X)

####### >>>>>>>>>>>>>>>>>>>>>  Filter Dictionary Contents
# you want to make a new dictionary with selected keys removed
D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
removeKeys = [0, 2, 5]

X = {k: D[k] for k in D.keys() - removeKeys}
print(X)


####### >>>>>>>>>>>>>>>>>>>>>  Invert Mapping / Reverse lookup
# Given a dictionary d and a key k, it is easy to find the corresponding value v = d[k]. This operation is called a lookup. But what if 
# you want to retrieve a key k using a value v in a dictionary? You have to do reverse lookup. This is where dictionary comprehension 
# comes handy.
D = {0: 'red', 1: 'green', 2: 'blue'}
R = {v: k for k,v in D.items()}
print(R)

# Dictionary Comprehension with Enumerate
'''Sometimes you want to create a dictionary from the list with list index number as key and list element as value. To achieve this wrap 
the list in enumerate() function and pass it as an iterable to the dict comprehension.'''
L = ['red', 'green', 'blue']
D = {k:v for k,v in enumerate(L)}
print(D)
'''Such dictionaries with element index are often useful in a variety of scenarios such as reading a file by lines.'''
D = {ix: line for ix, line in enumerate(open('myFile.txt'))}
print(D)

####### >>>>>>>>>>>>>>>>>>>>> Initialize Dictionary with Comprehension
'''Dictionary comprehensions are also useful for initializing dictionaries from keys lists, in much the same way as the fromkeys()
 method. Following example Initializes a dictionary with default value ‘0’ for each key.'''
keys = ['red', 'green', 'blue']
D = {k: 0 for k in keys}
print(D)

# equivalent to using fromkeys() method
D = dict.fromkeys(keys, 0)
print(D)
# PTBN - A standard way to dynamically initialize a dictionary is to combine its keys and values with zip, and pass the result to the 
# dict() function. However, you can achieve the same result with a dictionary comprehension.
keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Dev']
D = {k: v for (k, v) in zip(keys, values)}
print(D)

# equivalent to using dict() on zipped keys/values
D = dict(zip(keys, values))
print(D)

####### >>>>>>>>>>>>>>>>>>>>> Dictionary Comprehension with if Clause
# A dictionary comprehension may have an optional associated if clause to filter items out of the result.
# Iterable’s items are skipped for which the if clause is not true.
# The following example collects squares of even items (i.e. items having no remainder for division by 2) in a range.
D = {x: x**2 for x in range(6) if x % 2 == 0}
print(D)

# This dictionary comprehension is the same as a for loop that contains an if statement:
D = {}
for x in range(5):
    if x % 2 == 0:
        D[x] = x**2

print(D)

####### >>>>>>>>>>>>>>>>>>>>> Nested Dictionary Comprehension
'''The initial value in a dictionary comprehension can be any expression, including another dictionary comprehension.
Syntax:                             {key_expression : {dict comprehension} for item in iterable}
'''

D = {(k,v): k+v for k in range(2) for v in range(2)}
print(D)
# Prints {(0, 1): 1, (1, 0): 1, (0, 0): 0, (1, 1): 2}

# is equivalent to
D = {}
for k in range(2):
    for v in range(2):
        D[(k,v)] = k+v
print(D)   


# k %= len(lst) means k = k % len(lst) where the modulo operator gives the remainder after division. 
# It normalizes k so it lies within the valid rotation range [0, len(lst) - 1] i.e., Remove all full rotations and keep only the part 
# that actually changes the list. Eg: k = 7, k % 5 = 2 so, rotate by 5 → full cycle (no change) and rotate by 2 → actual effect
# In python %= is an augmented assignment operator which means k = k % n






###################################################################
########### >>>>>>>>>>>>>>>>>> PACKING AND UNPACKING >>>>>>>>>>>>>>>> ###########
###################################################################


####### >>>>>>>>>>>>>>>>>>>>> Tuple Packing & Unpacking
## ------ Tuple Packing - You can pack a tuple by simply placing a comma-separated sequence of values into a variable.
# When a tuple is created, the items in the tuple are packed together into the object.
T = ('red', 'green', 'blue', 'cyan')
print("Tuple Packing : ", T) # the values ‘red’, ‘green’, ‘blue’ and ‘cyan’ are packed together in a tuple T

## ------ Tuple Unpacking - When a packed tuple is assigned to a new tuple, the individual items are unpacked (assigned to the items of 
# a new tuple).
T = ('red', 'green', 'blue', 'cyan')
(color1, color2, color3, color4) = T
print("Tuple Unpacking : ", color1)
print("Tuple Unpacking : ", color2)
print("Tuple Unpacking : ", color3)
print("Tuple Unpacking : ", color4)
''' NOTE: 
1. You can also use asterisk * to unpack remaining items as a list
T = ('red', 'green', 'blue', 'cyan', 'yellow', 'orange')
(color1, color2, *other_colors) = T
print(color1)
print(color2)
print(other_colors) # other_colors is a list containing the remaining items
2. The number of variables on the left side must match the number of items in the tuple, unless using * to capture remaining items. 
Python will raise a ValueError if they don’t match. '''

## ------ Usage/ Use case of unpacking: Tuple unpacking comes handy when you want to swap values of two variables without using a 
# temporary variable. Eg: Swap values of 'a' and 'b' as shown below:
a = 1
b = 99
a, b = b, a
print(" Usage/ Use case of unpacking: ", a)
print(" Usage/ Use case of unpacking: ", b)

## ------ In Python, the right side of an unpacking assignment can be any type of sequence (more generally, any iterable object), as 
# long as the number of elements in the sequence matches the number of variables on the left side (unless using the star * operator for 
# extended unpacking). 

# -- Unpacking a tuple: shown above

# -- Unpacking a list
L = [1, 2, 3]
(x, y, z) = L
print(" Unpacking a list: ", x)
print(" Unpacking a list: ", y)
print(" Unpacking a list: ", z)

# -- Unpacking a string
S = 'abc'
(a, b, c) = S
print(" Unpacking a string: ", a)
print(" Unpacking a string: ", b)
print(" Unpacking a string: ", c)    

# -- Unpacking a set
S = {'red', 'green', 'blue'}
(a, b, c) = S
print(" Unpacking a set: ", a)
print(" Unpacking a set: ", b)
print(" Unpacking a set: ", c)    

# -- Unpacking a dictionary - When unpacking a dictionary, by default, only the keys are
# unpacked. To unpack both keys and values, you can use the items() method.
D = {'name': 'Alice', 'age': 30}
# Unpacking keys
(key1, key2) = D
print(" Unpacking a dictionary: ", key1)
print(" Unpacking a dictionary: ", key2)

# -- Unpacking range object
r = range(1, 4)
i, j, k = r
print(" Unpacking range object: ", i, j, k)
