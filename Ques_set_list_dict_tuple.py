

L = [1, 2, 2, 3, 4, 4, 5]
# uniq_list = L[0]
# print(type(uniq_list)) # <class 'int'>
uniq_list = [L[0]]
print(uniq_list)
print([uniq_list.append(item) for item in L if item not in uniq_list])
breakpoint()
def remove_duplicates(input_list: list) -> list:
    uniq_list = [input_list[0]]
    for item in input_list:
        if item not in uniq_list:
            uniq_list.append(item)
    return uniq_list
print("List after removing duplicates: ", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
# Q1. Remove duplicates from a list
def remove_duplicates(input_list: list) -> list:
# def remove_duplicates(input_list): -> list
    unique_set = set(input_list) # Convert the list to a set to remove duplicates
    unique_list = list(unique_set) # Convert the set back to a list
    return unique_list
# Order will not be preserved in this method. Use below method if order matters.
def remove_duplicates(input_list):
    unique_list = list(dict.fromkeys(input_list))
    return unique_list
# Example usage
print("List after removing duplicates: ", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# Q2. Check if two lists have any common elements
a = [1, 2, 3]
b = [4, 5, 3]
print("Check if two lists have any common elements: ", bool(set(a) & set(b)))

# Q3. Find common elements between two lists
def common_elements(list1, list2):
    return list(set(list1) & set(list2))
# Example usage 
print("Common elements:", common_elements([1, 2, 3, 4], [3, 4, 5, 6]))

# Q4. Find elements in list1 that are not in list2
def difference_elements(list1, list2):
    return list(set(list1) - set(list2)) 
# Example usage 
print("Elements in list1 not in list2:", difference_elements([1, 2, 3, 4], [3, 4, 5, 6]))

# Q5. Count unique values in a column-like list
def count_unique_values(input_list):
    return len(set(input_list))
# Example usage
print("Count of unique values:", count_unique_values([1, 2, 2, 3, 4, 4, 5]))

# Q6. Check if all elements in a list are unique
def are_all_elements_unique(input_list):
    return len(input_list) == len(set(input_list))
# Example usage
print("Are all elements unique? ", are_all_elements_unique([1, 2, 3, 4, 5]))

# Q7. Find duplicate elements in a list
def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5]
print("Duplicate elements: ", find_duplicates(input_list))

# Another way to find duplicates
def find_duplicates(input_list):
    # return list(set([x for x in input_list if input_list.count(x) > 1]))
    return set([x for x in input_list if input_list.count(x) > 1])

#  we can not do this using set operations list(set(main_list) - duplicates) because it will remove all occurrences of duplicates. 
# Code cannot be written without set(main_list) as it will remove duplicates from main_list itself.

# Q8. Perform union of multiple lists where any number of lists can be passed
def union_of_lists(*lists): # *lists to accept multiple number of lists 
    result_set = set()
    for lst in lists:
        result_set.update(lst)
    return list(result_set)

''' *lists allows a function to accept any number of positional arguments, which Python automatically collects into a tuple named lists.
With *lists, Python says accept ANY number of positional arguments and bundle them together. 
def demo(*lists):
    print(lists) # output is ([1, 2], [3, 4], [5])
    print(type(lists)) # output is <class 'tuple'>
demo([1, 2], [3, 4], [5])

Why is it a tuple and not a list?
Because function arguments should be immutable i.e., You’re not supposed to modify the argument container itself

Why *lists is called “variable-length arguments”
Because number of arguments is not fixed and Python collects them automatically
This is also called *args (most common name). *lists (your custom, meaningful name). 👉 args is just a convention, not a keyword.

def f(*args) --> Packing arguments into a tuple
f(*my_list)	--> Unpacking elements
eg for unpacking: 
nums = [1, 2, 3]
print(*nums)   # same as print(1, 2, 3)
'''
# Example usage
print("Union of lists - First way:", union_of_lists([1, 2, 3], [3, 4, 5], [5, 6, 7]))

list_of_sets = [{1, 2, 3, 4}, {3, 4, 5, 6}, {5, 6, 7, 8}] # Unpack the list into arguments for the union method
print("Union of lists - second way:", set().union(*list_of_sets)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Q9. Find the intersection of multiple lists
def intersection_of_sets(*lists): # *lists to accept multiple number of lists 

    result_set = set()
    for idx in range(len(lists)):
        comm_ele = lists[idx-1].intersection(lists[idx])
        result_set.update(comm_ele)
    return list(result_set)

# def intersection_of_sets(set1, set2):
#     return set1.intersection(set2)
# Example usage
print("Intersection of sets:", intersection_of_sets([1, 2, 3, 4], [3, 4, 5, 6]))
breakpoint()
lists = [[1,2,3], [2,3,4], [2,5]]
result = set(lists[0]).intersection(*lists[1:])
print(result)
''' NOTE - A nested list is a single object, but using * unpacking converts its elements into multiple positional arguments. Functions 
like set. intersection() are designed to accept any number of iterables, so unpacking allows nested lists and multiple-list arguments to
be handled uniformly.'''
# Q10. Check if a set is a subset of another set
def is_subset(set1, set2):
    return set1.issubset(set2)
# Example usage
print("Is set1 a subset of set2?", is_subset({1, 2}, {1, 2, 3, 4}))

# Q11. Prove that the set membership testing is faster than list membership testing
# This question tests the large-scale performance trap
large_set = set(range(1000000))
large_list = list(range(1000000))  

import time
start = time.time()
999999 in large_set
end = time.time()
print("Set membership test time:", end - start) 

start = time.time()
999999 in large_list
end = time.time()
print("List membership test time:", end - start)
print("Testing membership performance between set and list: 1.9073486328125e-06 < 0.005065202713012695  # True ")

# Q12. Create an empty set
empty_set = set() # dont use {} as it creates an empty dictionary
print("Empty set:", empty_set)

# Q13. Find customers common across 3 campaigns: c1 = [101,102,103], c2 = [102,103,104] and c3 = [103,105]
# This question tests intersection of multiple sets
c1 = [101,102,103]
c2 = [102,103,104]
c3 = [103,105]
print("Common customers across 3 campaigns -- method 1:", set(c1).intersection(set(c2), set(c3)))
print("Common customers across 3 campaigns -- method 2:", set(c1) & set(c2) & set(c3)) 
# --- other ways ?????????????
# Q14. Find customers who participated in at least one campaign
all_customers = set(c1).union(c2, c3)
print("Customers in at least one campaign:", all_customers)

# Q15. Find customers who participated in exactly one campaign
only_c1 = set(c1) - set(c2) - set(c3)
only_c2 = set(c2) - set(c1) - set(c3)
only_c3 = set(c3) - set(c1) - set(c2)
exactly_one_campaign = only_c1.union(only_c2).union(only_c3)
print("Customers in exactly one campaign:", exactly_one_campaign)
print("Customers in exactly one campaign2:", only_c1 | only_c2 | only_c3)
# NOTE: Another way using symmetric difference set(c1).symmetric_difference(set(c2)).symmetric_difference(set(c3)) but this wont work as it gives customers in odd 
# number of campaigns along with common to all 3 campaign.

# Q16. What is the output of S = {1, 1.0, True, 'True'}?
S = {1, 1.0, True, 'True'}
print("Set with True, 1, 1.0:", S) # Output will be {1, 'True'} because True, 1, and 1.0 are considered equal in Python sets.
# Why?True == 1 == 1.0 So Same hash value.

# Q17. Find the length of the set after adding duplicate elements
S = {1, 2, 3}
S.add(2)
S.add(3)
print("Length of set after adding duplicates:", len(S)) # Output will be 3 because duplicates are not added to the set. 

# Q18. What is the output of {math.nan, math.nan, 1, 2} and {float('nan'), float('nan'), 1, 2}?
import math
S = {math.nan, math.nan, 1, 2}
print("Set with NaN values1:", S) # Output will be {nan, 1, 2}.
S = {float('nan'), float('nan'), 1, 2}
print("Set with NaN values2:", S)  # Output will be {nan, nan, 1, 2} Because NaN is not equal to itself, both NaN values are treated as distinct elements in the set.
'''Why? In python : nan != nan -- true, math.nan is math.nan -- True but float('nan') is float('nan') -- False
So, math.nan has same identity and hash value → only one gets stored'''

# Q19. Use remove function for emptying whole set
s = {1, 2, 3}
# for x in s:
#     s.remove(x)  # wrong approach, raises RuntimeError: Set changed size during iteration
for x in s.copy(): # correct approach
    s.remove(x)
print("Modifying a set while iterating: ",s)  # Output: set()

# Q20. Create nested sets using frozenset
s = {frozenset([1, 2]), frozenset([2, 3])}
s = {frozenset([1, 2]), 5, 6}
print("Creating nested sets: ",s)  

# Q21. What is the output of A-B and B-A where A = {1, 2, 3} and B = {3, 4} 
A = {1, 2, 3}
B = {3, 4}
print("Present only in set A: ", A - B)  # Output: {1, 2}
print("Present only in set B: ", B - A)  # Output: {4}
# Interviewers love to check directionality ie., Set difference is NOT symmetric

# Q22. Create dictionary with frozen set as key  
print({frozenset([1,2]): "A"})  # Frozen sets can be dictionary keys but normal sets cannot.

# Q23. What is the output of {1, 2} == [1, 2] ?
print({1, 2} == [1, 2]) # Output: False because they are different types/ data structures.

# Q24. What is the output of {1, 2} < {1, 2, 3} and {1, 2} <= {1, 2} ?
{1, 2} < {1, 2, 3}   # True
{1, 2} <= {1, 2}    # True # '<' means proper subset, '<=' means subset (can be equal)

# Q25. What is the output of A & B and A and B where A = {1, 2} and B = {2, 3}?
A = {1, 2}
B = {2, 3}
print(A & B)     # {2}
print(A and B)   # {2, 3}
# Why this? and is boolean logic, not set logic.
# The '&' operator performs set intersection, while 'and' evaluates the truthiness of both sets and returns the second set if both are non-empty.

# Q26. what happends when there is an intersection of a set with an empty set as well as no argument?
s = {1, 2, 3}
empty = set()
print(s.intersection(empty))  # Output: set()

A.intersection()  # {1, 2} # No argument = identity so it returns the set itself

# Q27. what happens when we update sets by assigning it to the original variable?
s = {1, 2}
s = s.add(3) # s is now None
print(s)  # Output: None

s.add(3) # correct way
print(s)  # Output: {1, 2, 3}

# Q28. Set comprehension vs generator
s_comp = {x*x for x in range(5)}  # Set comprehension
g_exp = (x*x for x in range(5))    # Generator expression  
print(s_comp)  # Output: {0, 1, 4, 9, 16}
print(list(g_exp))  # Output: [0, 1, 4, 9, 16]
# Set comprehension creates a set, while generator expression creates an iterator that generates values on-the-fly.
{x*x for x in range(3)}   # set
(x*x for x in range(3))   # generator

# Q29. Real DS trap: float precision
s = {0.1, 0.2, 0.3}
print(0.1 + 0.2 in s)  # Output: False due to floating-point precision issues.
# 0.1 + 0.2 results in 0.30000000000000004, which is not exactly equal to 0.3.
# Use round() or Decimal for precise comparisons. 
round(0.1 + 0.2, 1) in {0.1, 0.2, 0.3}  # True

s = {0.1 + 0.2, 0.3}
print(s)  # Output: {0.30000000000000004, 0.3}
# Two different values may exist due to precision.

# Q30. Remove multiple item from list by value using list comprehension
original_list = [10, 3, 12, 15, 5, 8, 10, 5]
values_to_remove = [10, 5]
filtered_list = list(filter(lambda item: item not in values_to_remove, original_list))

print(filtered_list) # Output: [3, 12, 15, 8]


# Q31. 
# Q32. 



# Q33. 

# Q34. 
# Q35. 

