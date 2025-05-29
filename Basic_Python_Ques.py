# ###################################
# BASIC THINGS TO REMEMBER
# ##################################

# ------ Access list values and index --------------------------------------------
print("Access list values and index", "-"*50)
lists = [45,32,54, 54, 45,32, 56, 44]
print(lists[4])
print(lists.index(32))  # gives index of first occurence

print("Loop through list", "*"*50)
print("Loop through index and value together")
for index, val in enumerate(lists):
    print(index, val)
print("Loop through index ")
for index in range(len(lists)):
    print(index)
print("Loop through value ")
for val in lists:
    print(val) 

# ------ Access string values and index --------------------------------------------
print("Access string values and index", "-"*50)
strings = "rettggjfiggfhijfo"
print(strings[4])
print(strings.index('hi')) 
print(strings.index('gg')) # gives index of first occurence

print("Loop through string", "*"*50)
print("Loop through index and value together")
for index, val in enumerate(strings):
    print(index, val)
print("Loop through index ")
for index in range(len(strings)):
    print(index)
print("Loop through value ")
for val in strings:
    print(val)     

# ------ Access dict values and index --------------------------------------------
print("Access dict values and index", "-"*50)
dicts ={"A":[4,5,65], "B":[43,54,1,3], "C":[12, 45, 657, 76,65]}
print(dicts["A"])
# print(dicts.keys()[dicts.values().index([4,5,65])]) # does not exists

print("Loop through dict", "*"*50)
print("Loop through key and index of keys together ")
for index, val in enumerate(dicts): # keys index and value it loops through
    print(index, val)    
print("Loop through index and value together")
for index, val in dicts.items():
    print(index, val)
print("Loop through index ")
for index in range(len(dicts)):
    print(index)
print("Loop through keys ")
for val in dicts:
    print(val) 
for val in dicts.keys():
    print(val) 
print("Loop through value ")
for val in dicts.values():
    print(val) 

# ###################################
# Python Question for Coding Practice 
# ##################################

# 1. Write a Python program to reverse a string without slicing
print("Q1", ">"*50)
def reverse_str(user_str):
    if isinstance(user_str, str):
        reversed_str = ""
        for char in user_str:
            reversed_str = char + reversed_str
        return reversed_str
    else:
        return "This function works only for strings"
    
print("Reversed String: ", reverse_str("Hello World"))
print("Reversed String: ", reverse_str("4564576"))
print("Reversed String: ", reverse_str(4564576))

# 2. Write a Python program to check if a string is a palindrome
# NOTE - A palindrome is a word, sentence, verse, or even number that reads the same backward or forward
print("Q2", ">"*50)
# ---- Method 1 - with slicing
def is_palindrome(user_str):
    if isinstance(user_str, str):
        user_str = user_str.lower() #if this line not written, capital letters have impact on the result as == is case sensitive
        if user_str == user_str[::-1]:
            return "Yes! Its palindrome"
        else:
            return "No! Its not palindrome"
    else:
        return "This function works only for strings"
    
print("Hello World -", is_palindrome("Hello World"))
print("Madam - ", is_palindrome("Madam"))
print("4564576- ", is_palindrome("4564576"))
print("4564576- ", is_palindrome(4564576))

# ---- Method2 - without slicing
def is_palindrome2(user_str):
    if isinstance(user_str, str):    
        user_str = user_str.lower() #if this line not written, capital letters have impact on the result as == is case sensitive
        reverse_str = ""
        for char in user_str:
            reverse_str = char + reverse_str
            
        if user_str == reverse_str:
            return "Yes! Its palindrome"
        else:
            return "No! Its not palindrome"
    else:
        return "This function works only for strings" 
       
print("Hello World -", is_palindrome2("Hello World"))
print("Madam - ", is_palindrome2("Madam"))
print("4564576- ", is_palindrome2("4564576"))
print("4564576- ", is_palindrome2(4564576))

# 3. Write a Python program to find the largest/ maximum element in a list
print("Q3", ">"*50)
def find_large_no(user_list):
    if isinstance(user_list, list):       
        largest_ele = user_list[0]
        for ele in user_list:
            if ele > largest_ele:
                largest_ele = ele
        return largest_ele
    elif isinstance(user_list, str):
        user_list = user_list.lower()
        largest_ele = user_list[0]
        for ele in user_list:
            if ele > largest_ele:
                largest_ele = ele
        return largest_ele
    else:
        return "This function works only for list and strings" 
# NOTE - The code under if statement works well with the string but added in elif to consider case sensitivenesss of strings. Also, in case of strings, this function return the letter which comes later.

print("Largest Element of the list is ", find_large_no([4,1,5,10,6]))
print("Largest Element of the list is ", find_large_no(['a', 'd', 'z', 'q']))
print("Largest Element of the list is ", find_large_no("hello world"))
print("Largest Element of the list is ", find_large_no(43545))

# ------ find the lowest/ minimum element in a list
def find_min_no(user_list):
    if isinstance(user_list, list):       
        min_ele = user_list[0]
        for ele in user_list:
            if ele < min_ele:
                min_ele = ele
        return min_ele
    elif isinstance(user_list, str):
        user_list = user_list.lower()
        min_ele = user_list[0]
        for ele in user_list:
            if ele < min_ele:
                min_ele = ele
        return min_ele
    else:
        return "This function works only for list and strings" 
# NOTE - The code under if statement works well with the string but added in elif to consider case sensitivenesss of strings. Also, in case of strings, this function return the letter which comes later.

print("Largest Element of the list is ", find_min_no([4,1,5,10,6]))
print("Largest Element of the list is ", find_min_no(['a', 'd', 'z', 'q']))
print("Largest Element of the list is ", find_min_no("hello world")) # whitespace is the minimum element in a string
print("Largest Element of the list is ", find_min_no(43545))

# 4. Write a Python program to count the frequency of each element in a list
print("Q4", ">"*50)
def freq_count(user_list):
    if isinstance(user_list, list):  
        dict_freq = {}
        for ele in user_list:
            if ele in dict_freq:
                dict_freq[ele] += 1
            else:
                dict_freq[ele] = 1
        return dict_freq
    elif isinstance(user_list, str):
        user_list = user_list.lower()
        dict_freq = {}
        for ele in user_list:
            if ele in dict_freq:
                dict_freq[ele] += 1
            else:
                dict_freq[ele] = 1
        return dict_freq
    else:
        return "This function works only for list and strings" 
''' NOTE - 1. This function works well for strings. Numbers are creating issue as it cannot be looped.
            2. If using try and except then capital and small letters will be treated differently
'''

print("Frequemcy Count of [2,5,6,1,2,5,5,10,2,2]: ", freq_count([2,5,6,1,2,5,5,10,2,2]))
print("Frequemcy Count of ['a', 'd', 'z', 'q', 'a', 'a', 'z', 'c']: ", freq_count(['a', 'd', 'z', 'q', 'a', 'a', 'z', 'c']))
print("Frequemcy Count of 'hello world': ", freq_count("hello world"))
print("Frequemcy Count of 335432454 : ", freq_count(335432454))
print("Frequemcy Count of 'hello world': ", freq_count("hello worLd"))

#  5. Write a Python program to find the common elements between two lists
print("Q5", ">"*50)
def common_lis_ele(list1, list2):
   if (isinstance(list1, list)) &  (isinstance(list2, list)) :  
        common_ele = []
        for ele in list1:
            if ele in list2 and ele not in common_ele: # 2nd condition added to avoid duplicates
                common_ele.append(ele)
        return common_ele
   elif (isinstance(list1, str)) &  (isinstance(list2, str)) :  
        list1 = list1.lower()
        list2 = list2.lower()
        common_ele = []
        for ele in list1:
            if ele in list2 and ele not in common_ele: # 2nd condition added to avoid duplicates
                common_ele.append(ele)
        return common_ele   
   else:
        return "This function works only for list and strings" 
''' NOTE - 1. This function works well for strings. Numbers are creating issue as it cannot be looped.
            2. If using try and except then capital and small letters will be treated differently
'''

print("Common Element in 2 list: ", common_lis_ele([2,5,6,1,2,5,5,10,2,2], [100,2,5,31]))
print("Common Element in 2 list: ", common_lis_ele(['a', 'd', 'z', 'q', 'a', 'a', 'z', 'c'], ['p', 's', 'z', 'q']))
print("Common Element in 2 strings: ", common_lis_ele( "hello world", "dfgfgwweetll"))
print("Common Element in 2 numbers: ", common_lis_ele( 335432454, 89099542233))
print("Common Element in 2 strings: ", common_lis_ele( "hello world", "dfgfgWeetL"))

# 6. Write a Python program to find the second largest number in a list
print("Q6", ">"*50)
def sec_largest_ele(user_list):
    if isinstance(user_list, list):  
        largest_ele = user_list[0]
        sec_large = user_list[0]
        for ele in user_list:
            if ele > largest_ele:
                sec_large = largest_ele
                largest_ele = ele
            elif ele > sec_large and ele != largest_ele:
                sec_large = ele
        return sec_large
    elif isinstance(user_list, str):
        user_list = user_list.lower()        
        largest_ele = user_list[0]
        sec_large = user_list[0]
        for ele in user_list:
            if ele > largest_ele:
                sec_large = largest_ele
                largest_ele = ele
            elif ele > sec_large and ele != largest_ele:
                sec_large = ele
        return sec_large        
    else:
        return "This function works only for list and strings" 
''' NOTE - 1. This function works well for strings. Numbers are creating issue as it cannot be looped.
            2. If using try and except then capital and small letters will be treated differently
'''
 
print("Second largest Element of the list is ", sec_largest_ele([4,1,5,10,6]))
print("Second largest Element of the list is ", sec_largest_ele(['a', 'd', 'z', 'q']))
print("Second largest Element of the list is ", sec_largest_ele("hello world"))
print("Second largest Element of the list is ", sec_largest_ele(43545))
print("Second largest Element of the list is ", sec_largest_ele("helLo worRldS"))

# 7. Write a Python program to remove duplicates from a list
print("Q7", ">"*50)
def unique(user_list):
    if isinstance(user_list, list):  
        remove_dupl = [(user_list[0])]
        for ele in user_list:
            if ele not in remove_dupl:
                remove_dupl.append(ele)
        return remove_dupl        
    # Above code works for both list and strings. However, with above code strings are converted into list which needs to be converted back to string. Therefore, elif statement
    elif isinstance(user_list, str):
        user_list = user_list.lower()          
        remove_dupl = [(user_list[0])]
        for ele in user_list:
            if ele not in remove_dupl:
                remove_dupl.append(ele)            
        remove_dupl_str = ''.join(remove_dupl)
        return remove_dupl_str
    else:
           return "This function works only for list and strings" 
        
''' NOTE - 1. This function works well for strings. Numbers are creating issue as it cannot be looped.
            2. If using try and except then capital and small letters will be treated differently
'''

print("Unique of [2,5,6,1,2,5,5,10,2,2]: ", unique([2,5,6,1,2,5,5,10,2,2]))
print("Unique of ['a', 'd', 'z', 'q', 'a', 'a', 'z', 'c']: ", unique(['a', 'd', 'z', 'q', 'a', 'a', 'z', 'c']))
print("Unique of 'ABABRT': ", unique("ABABRT"))
print("Unique of  43545", unique(43545))
print("Unique of 'ABABRT': ", unique("ABABRTabyzq")) 

# 8. Write a Python program to find the factorial of a number
print("Q8", ">"*50)
# ---- Method 1 
def factorial(num): 
    try:
        if num == 0:
            return 1
        elif num < 0:
            return "No factorial for negative numbers"
        else:
            return num * factorial(num-1)
    except:
        return "This function works only for numbers"
# NOTE - this is recurrsive function

print("Factorial of 5 - Method 1 : ", factorial(5))
print("Factorial of 5 - Method 1 : ", factorial("ABABRT"))

# ---- Method 2
func = lambda num: 1 if num ==0 else num*func(num-1)
print("Factorial of 5 - Method 2 : ", func(5))

# 9. Write a Python program to check if a number is prime
print("Q9", ">"*50)
def is_prime(num):
    try:
        if num < 2:
            return "There is no prime number below 2"
        else:
            for ints in range(2, int(num**0.5)+1): # + 1 as range excludes the last number
                if num % ints == 0: # As soon as number becomes visible then its not a prime so code stops here
                    return "Number is not a prime number"
                else:
                    return "Number is a prime number"
    except:
        return "This function works only for numbers"            
print("check if a number is prime: ", is_prime(5))
print("check if a number is prime: ", is_prime(10))
print("check if a number is prime: ", is_prime("ABABRT"))

# 10. Write a Python program to sort a list of elements using the bubble sort algorithm. ----?
print("Q10", ">"*50)

# 11. Write python program to Count Vowels in a string
print("Q11", ">"*50)
def count_vowel(user_str):
    try:    
        vowels = "aeiou"
        user_str = user_str.lower() # This is used otherwise capital and small letters will be treated differently
        counter = 0
        for char in user_str:
            if char in vowels:
                counter += 1
        return counter
    except:
        return "This function works only for strings"  
# NOTE - whitespaces are counted as 1 element which is part of non vowel elements
print("Count Vowels in 'Hello World': ", count_vowel("Hello World"))
print("Count Vowels in 43545", count_vowel(43545))

# ---- Counting non vowels  in a string
def count_nonvowel(user_str):
    try:    
        vowels = "aeiou"
        user_str = user_str.lower() # This is used otherwise capital and small letters will be treated differently
        counter = 0
        for char in user_str:
            if char not in vowels:
                counter += 1
        return counter
    except:
        return "This function works only for strings"  
print("Count Non Vowels in 'Hello World': ", count_nonvowel("Hello World"))
print("Count Non Vowels in 43545", count_nonvowel(43545))

# 12. Write python program to calculate the Sum of Digits in a Number
print("Q12", ">"*50)
def sum_digits(num):
    num = str(num) # we cannot iter over number but can iter over strings
    if num.isdigit():
        summed_digits = 0
        for digits in num:
            summed_digits += int(digits)
        return summed_digits
    else:
        return "This function works only for numbers"   
print("Summed Digits of 525: ", sum_digits(525))
print("Summed Digits of 33343fdfd: ", sum_digits("33343fdfd"))
print("Summed Digits of ['a', 'd', 'z', 'q']: ", sum_digits(['a', 'd', 'z', 'q']))
print("Summed Digits of [2,5,6,1,2,5,5,10,2,2]: ", sum_digits([2,5,6,1,2,5,5,10,2,2]))

# 13. Write python program to merge two lists in 2 ways - one list after another list, first element of 2 list together then second of both list together and so on
print("Q13", ">"*50)
def merge_list(list1, list2):
   if (isinstance(list1, list)) &  (isinstance(list2, list)) :  
        merged_list = list1
        for iter in list2:
            merged_list.append(iter)
        return merged_list
   else:
        return "This function works only for list and strings" 
print("Merge 2 list : ", merge_list([2,5,6,1,2,5,5,10,2,2], ['a', 'd', 'z', 'q']))
print("Merge 2 list : ", merge_list("33343fdfd", "Daruk"))
print("Merge 2 list : ", merge_list("33343fdfd", 34342084))
print("Merge 2 list : ", merge_list("33343fdfd", ['a', 'd', 'z', 'q']))

def merge_list2(list1, list2):
    res_lst = []
    for ele in range(len(list1)):
        res_lst.append(list1[ele])
        res_lst.append(list2[ele])
    return res_lst
print("Merge 2 list : ", merge_list2([2,5,6,1], ['a', 'd', 'z', 'q'])) # For this both list should be of equal size, otherwise use below code

def merge_list3(list1, list2):
    res_lst = []
    for ele in range(len(list1)):
        if (ele >= len(list1)) :
            res_lst.append(list2[ele])
        elif (ele >= len(list2)):
            res_lst.append(list1[ele])
        else:    
            res_lst.append(list1[ele])
            res_lst.append(list2[ele])
    return res_lst
print("Merge 2 list : ", merge_list3([2,5,6,1,2,5,5,10,2,2], ['a', 'd', 'z', 'q'])) # For this both list should be of equal size

# NOTE - Dont use below code
def merge_list1(list1, list2):
    merged_list = list1
    merged_list.append(list2)
    return merged_list
print("Merge 2 list (Dont use this) : ", merge_list1([2,5,6,1,2,5,5,10,2,2], ['a', 'd', 'z', 'q']))

# 14. Write python program to Find the Maximum Difference between Two Elements in a List
print("Q14", ">"*50)
def max_diff(user_list):
    try:
        max_no = max(user_list)
        min_no = min(user_list)
        max_difference = max_no - min_no
        return max_difference
    except:
        return "This function works only for list" 
print("Maximum Difference in [200,5,6,1,2,5,5,10,2,2]: ", max_diff([200,5,6,1,2,5,5,10,2,2]))

# 15. Write python program to Count letters in a sentence
print("Q15", ">"*50)
def count_letter(user_sen):
    try:    
        counter = 0
        for char in user_sen:
            counter += 1
        return counter
    except:
        return "This function works only for strings" 
    
print("Count letters in a Sentence in 'Python is best': ", count_letter('Python is best'))

# 16. Write python program to Count Words in a Sentence
print("Q16", ">"*50)
def count_words(user_sen):
    if isinstance(user_sen, str):
        counter = 0
        splitted_words = user_sen.split(' ') # we cannot use user_sen.split("") or user_sen.split('')
        # splitted_words = user_sen.split() # we can use this also instead of above line
        for char in splitted_words:
            counter += 1
        return counter
    else:
        return "This function works only for strings"  
       
print("Count letters in a Sentence in 'Python is best': ", count_words('Python is best'))

# 17. Write python program to Count letters in a Sentence wthout counting spaces
print("Q17", ">"*50)
def count_wo_space(user_sen):
    if isinstance(user_sen, str):    
        counter = 0
        for char in user_sen:
            if " " not in char:
                counter += 1
        return counter
    else:
        return "This function works only for strings"  
    
print("Count letters in a Sentence in 'Python is best': ", count_wo_space('Python is best'))

# 18 - Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
print("Q18", ">"*50)
def no_n_sq(num):
    if isinstance(num, int):
        num = int(num)
        user_dict = {}
        for ints in range(num+1):
            user_dict[ints] = ints*ints
        return user_dict
    else:
        return "This function only works with numbers"
print("print a dictionary that contains a number (between 1 and n) in the form (x, x*x)': ", no_n_sq(5))

# 19 - Write a Python program to sum all the keys in a dictionary
print("Q19", ">"*50)
# Method 1
sample_dict = {1 : 23, 2 : 45, 3 : -17, 4 : 87}
if all(isinstance(x, (int, float)) for x in sample_dict.keys()): # user_dict.keys() returns list
    print(sum(sample_dict.keys()))
else:
    print("Keys have to be in numbers")
print("Method 2 starts")

# Method 2
# def sum_dict_keys(user_dict):
#     if all(isinstance(x, (int, float)) for x in user_dict.keys()):
#         summed_key = 0
#         for int in user_dict: # difference between is and in: is used with 1 element and in used with series of element
#             summed_key += int
#         return summed_key
#     else:
#         return "Keys have to be in numbers"

# print("sum all the keys in a dictionary1: ", sum_dict_keys({1 : 23, 2 : 45, 3 : -17, 4 : 87}))
# print("sum all the keys in a dictionary2: ", sum_dict_keys({"Name" : "Ram" , "Age" : 23}))

# Q20 - Access dictionary key’s element by index
print("Q20", ">"*50)
def dict_access_index(user_dict, index):
    if isinstance(user_dict, dict):
        dict_keys = list(user_dict.keys()) # if we write [user_dict.keys()], it throws error
        key_by_index = dict_keys[index]
        return key_by_index, user_dict[key_by_index]
    else:
        return  "This function only works with dictionary"
print("Access dictionary key’s element by index: ", dict_access_index({1 : 23, 2 : 45, 3 : -17, 4 : 87}, 3))

# Q21 - Drop empty items or keys from a dictionary
print("Q21", ">"*50)
def filter_non_empty_keys(user_dict):
    if isinstance(user_dict, dict):    
        non_empty_dict = {}
        for k,v in user_dict.items():
            if v is not None: # difference between is and in. Dont use in as value is compared with only 1 value
                # "is" checks if the memory address of this obbject is same or not. Its a hard check so use =
                non_empty_dict[k] = v
        return non_empty_dict
    else:
        return  "This function only works with dictionary"
print("Drop empty Items from a given Dictionary: ", filter_non_empty_keys({ "Gender" : "Female", "City" : "Salem", "Mark" : None}))
# NOTE - Dont use for look + del as shown in below code. It will throw RuntimeError: dictionary changed size during iteration
def dont_use(dict):
    for i, j in dict.items():
        if j is None: 
            del dict[i]
    return dict

# Q22 - Match key and values in two dictionaries and store common keys and value in another dictionary
print("Q22", ">"*50)
def match_keys(dict1, dict2):
    if (isinstance(dict1, dict)) &  (isinstance(dict2, dict)):       
        matched_dict = {}
        for k, v in dict1.items():
            # if v in dict2.values() and k in dict2.keys(): # we dont to check if pairs exists
            if k in dict2.keys() and v is dict2[k]: 
                matched_dict[k] = v
        return matched_dict
    else:
        return  "This function only works with dictionary"
    
dict1 = {'Tamil' : 92, 'English' : 56, 'Maths' : 88, 'Sceince' : 97, 'Social' : 89}
dict2 = {'Tamil' : 78, 'English' : 68, 'Maths' : 88, 'Sceince' : 97, 'Economics' : 56}
print("Match key and values in two dictionaries", match_keys(dict1, dict2))

# Q23 - Write a Python program to count number of list in a dictionary value
print("Q23", ">"*50)
def count_list(user_dict):
    if isinstance(user_dict, dict):       
        counter = 0
        for k, v in user_dict.items(): 
            if isinstance(v, list): # can also use: type(dict[k])== list 
                counter += 1
        return counter
    else:
        return  "This function only works with dictionary"
        
print("Count number of list in a dictionary value", count_list({ 'M1' : [67,79,90,73,36], 'M2' : [89,67,84], 'M3' : [82,57] }))

# Q24 - Write a Python program to count number of items in a dictionary value including each element of list/tuple
print("Q24", ">"*50)
def count_elements(user_dict):
    if isinstance(user_dict, dict):           
        counter = 0
        for k, v in user_dict.items(): 
            if isinstance(v, list) or isinstance(v, tuple): # can also use: type(dict[k])== list 
                counter += len(v)
            else:
                counter +=1
        return counter
    else:
        return  "This function only works with dictionary"
        
print('''Count number of list in a dictionary value including each element of 
      list/tuple''', count_elements({ 'M1' : [67,79,90,73,36], 'M2' : [89,67,84], 'M3' : 82 }))
print('''Count number of list in a dictionary value including each element of 
      list/tuple''', count_elements({ 'M1' : [67,79,90,73,36], 'M2' : [89,67,84], 'M3' : (82,57) }))

# Q25 - Write a Python program to print a dictionary line by line
print("Q25", ">"*50)
dict1 = {'Tamil' : 92, 'English' : 56, 'Maths' : 88, 'Sceince' : 97, 'Social' : 89}
dict1 = { 'M1' : [67,79,90,73,36], 'M2' : [89,67,84], 'M3' : 82 }
for k,v in dict1.items():
    print(k, "::", v) 

# Q26. Write a Python program to Convert two lists into a dictionary
print("Q26", ">"*50)
list1 = [10, 20, 30, 40, 50]
list2 = [1, 2, 3, 4, 5]
print("New Dict:", dict.fromkeys(list1, list2))
print("New Dict:", dict(zip(list1, list2)))
# NOTE - above 2 functions will produce results in different way

# Q27. Write a Python program to find the most frequent character in a string
print("Q27", ">"*50)
def freq_char(user_str):
    if isinstance(user_str, str):     
        user_str = user_str.lower() # Otherwise capital and lower case are treated differently
        freq_count = {}
        for char in user_str:
            if char not in " ":
                if char in freq_count:
                    freq_count[char] += 1
                else:
                    freq_count[char] = 1

        max_value = list(freq_count.values()).index(max(freq_count.values())) # list.index("A") - to get index of A in the list

        return list(freq_count.keys())[max_value]
    else:
        return  "This function only works with string"
print("The most frequent character in a string:", freq_char("Hello World"))
print("The most frequent character in a string:", freq_char("HeLo World"))

# Q28. Write a Python program to check if a string contains only digits
print("Q28", ">"*50)
def is_digit(user_str):
    if isinstance(user_str, str):  
        counter = 0
        for char in user_str:
            if char in "0123456789":
                counter += 1
            if counter == len(user_str):
                return True
            else:
                return False
    else:
        return  "This function only works with string"
# NOTE - Built in function for this is isdigit() 

print("Check if a string contains only digits.:", is_digit("He12"))
print("Check if a string contains only digits.:", is_digit("12"))
print("Check if a string contains only digits.:", is_digit("12@@"))

# Q29. Write a Python program to count the number of occurrences of a specific substring in a string
print("Q29", ">"*50)
def count_substr(user_str, sub_str):
    if (isinstance(user_str, str)) &  (isinstance(sub_str, str)) :  
        user_str =  user_str.lower()
        sub_str = sub_str.lower()
        counter = 0
        if len(sub_str) == 1:
            for char in user_str:
                if char == sub_str:
                    counter += 1
            return counter
        else: # NOTE - if else has been added to tackle cases with single char and word
            words = user_str.split()
            for char in words:
                if char == sub_str:
                    counter += 1
            return counter
    else:
        return  "This function only works with string"
    
print("Count the number of occurrences of a specific substring:", count_substr("Hello World", "l"))
print("Count the number of occurrences of a specific substring:", count_substr("Hello World, Hello", "Hello"))

# Q30. Write a Python program to find the index of the first occurrence of a substring in a string
print("Q30", ">"*50)
def index_str(user_str, sub_str):
    if (isinstance(user_str, str)) &  (isinstance(sub_str, str)) :  
        user_str =  user_str.lower()
        sub_str = sub_str.lower()
        index = 0
        if len(sub_str) == 1:
            for char in user_str:
                index += 1
                if char == sub_str:
                    break
            return index
        else:
            words = user_str.split()
            for char in words:
                index += 1
                if char == sub_str:
                    break
            return index
    else:
        return  "This function only works with string"
    
print("To find the index of the first occurrence of a substring in a string:", index_str("Hello World", "l"))
print("To find the index of the first occurrence of a substring in a string:", index_str("Hello World, Hello", "Hello"))

# Q31. Write a Python program to replace all occurrences of a substring with another substring
print("Q31", ">"*50)
def replace_str(user_str, sub_str, rplc_sub_str):
    if (isinstance(user_str, str)) &  (isinstance(sub_str, str)) &  (isinstance(rplc_sub_str, str)):  
        user_str =  user_str.lower()
        sub_str = sub_str.lower()
        new_str = ""
        for char in user_str:
            if char in sub_str:
                new_str += rplc_sub_str
            else:
                new_str += char
        return new_str
    else:
        return  "This function only works with string"
    
print("To replace all occurrences of a substring with another substring:", replace_str("Hello World", "l", "rst"))
#  make this code working for a group of substring -------??????

# Q32. Write a Python program to find the length of the last word in a sentence
print("Q32", ">"*50)
def len_last_word(user_str):
    if isinstance(user_str, str):  
        words = user_str.split()
        return len(words[-1])
    else:
        return  "This function only works with string"
print("To find the length of the last word in a sentence:", len_last_word("Hello World of Python"))

# Q33. Write a Python program to reverse the order of words in a sentence
def reverse_words(user_str):
    if isinstance(user_str, str):  
        words = user_str.split()
        new_str = ""
        for char in words:
            new_str = " " + char + new_str
        return new_str
    else:
        return  "This function only works with string"
    
print("To reverse the order of words in a sentence:", reverse_words("Hello World of Python"))

# Q34. Write a Python program to check if a string is a valid email address --- ask miku if its ok?
# @ existemce - check - only once
# @ before n after
# regex - write
def is_email(user_str):
    user_str = user_str.lower()
    words = user_str.split('@')
    if words[1][-4:len(words[1])] == ".com" and ((words[1].split('.')[0] == "gmail") or (words[1].split('.')[0] == "yahoo") or (words[1].split('.')[0] == "apple")):
        return "Email ID is valid"
    else:
        return "Email ID is not valid"
print("To rcheck if a string is a valid email address:", is_email("HelloWorld_python@gmail.com"))
print("To rcheck if a string is a valid email address:", is_email("HelloWorld_python@reditt.com"))

# Q35. Write a Python program to check if a string is a valid URL -----??
# Q36. Write a Python program to find the first non-repeated character in a string

# def first_non_rep(user_str):
#     char_first = ''
#     rep_dict = dict.fromkeys(user_str[0], 0)
#     # print(rep_dict)
#     # breakpoint()
#     for ele in user_str:
#         if ele not in rep_dict:
#             char_first = ele
#             print('char_first', char_first)
#         else:
#             rep_dict[ele] += 1
#         if len(char_first) == 1:
#             return char_first
# # print("str function:", first_non_rep("shhweta"))
# print("str function:", first_non_rep("sshhweta"))

def first_non_rep(user_str):
     for ele in user_str:
         upd_str = user_str.replace(ele, '')
         if len(upd_str) ==  len(user_str)-1:
            return ele
print("str function:", first_non_rep("sshhweta"))

def first_non_rep(user_str):
    rep_dict = dict.fromkeys(user_str, 0)
    # print(rep_dict)
    for ele in user_str:
        print("chcek1", ele)
        if ele in rep_dict:
            rep_dict[ele] +=1
            # print('char_first', char_first)
        else:
            print('chcek2', ele)
            return ele
        #     break
        #     rep_dict[ele] += 1
        # if len(char_first) == 1:
        #     return char_first
# print("str function:", first_non_rep("shhweta"))
print("str function:", first_non_rep("sshhweta"))

# Q37. Write a Python program to remove all leading and trailing whitespaces from a string
# Q38. Write a Python program to find the common characters between two strings.
# Q39. Write a Python program to find the second most frequent character in a string.
# Q40. Write a Python program to check if a string contains only unique characters.
# Q41. Write a Python program to find the longest common prefix among a list of strings.
# Q42. Write a Python program to check if a string is a valid IPv4 address. -------?
# Q43. Write a Python program to find the first non-repeated character in a string using OrderedDict.

# Q44. Append elements of lists so that each elements occurs only once
def append_uniq_ele(list1, list2):
    appended_list = []
    appended_list = list(set(list1)) + list(set(list2))
    return appended_list

    
print("Common Element in 2 list: ", append_uniq_ele([2,5,6,1,2,5,5,10,2,2], [100,2,5,31]))
print("Common Element in 2 list: ", append_uniq_ele(['a', 'd', 'z', 'q', 'a', 'a', 'z', 'c'], ['p', 's', 'z', 'q']))

# Q45. Write a Python program to find the second non-repeated character in a string

def sec_non_rep(user_str):
     char_non_rep_sec = ''
     for ele in user_str:
         upd_str = user_str.replace(ele, '')
         if len(upd_str) ==  len(user_str)-1:
            char_non_rep_sec += ele
         if len(char_non_rep_sec) == 2:
            return char_non_rep_sec[1]
print("str function:", sec_non_rep("sshhweta"))
print("str function:", sec_non_rep("shhweta"))

# Q 46. Write a Python program to find elements in list that sum upto the target value
print("Method 1")
def nums_sum1(nums, target):
    sumed = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
                sumed = nums[i] + nums[j]
                if sumed == target:
                    return [i, j]
print(nums_sum1([11, 2,15, 5, 7] , 9))

def find_sum_indices(nums, target):
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(i + 1, nums_len):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

print("Method 2")
def nums_sum2(nums, target):
    for index, num in enumerate(nums):
        other_no = target - num
        if other_no in nums:
            return [index, nums.index(other_no)] # If the value is not in the list, index() will raise a ValueError
                
print(nums_sum2([11, 2,15, 5, 7] , 9))

print("Method 3")
def nums_sum3(nums, target):
    seen = {}  # Stores {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # Found the pair
        seen[num] = i  # Save current number with its index

    return None  # No pair found

print(nums_sum3([11, 2,15, 5, 7] , 9))

# 47. Check keys and values of an empty dictionary
print("Q47", ">"*50)
dict = {}
print(dict.keys())
print(dict.values())

# 48. Convert integer or string with integers into decimal
print("Q48", ">"*50)
# ---- Method 1
print("Method 1", type(float(10)))
print("Method 1", type(float('10')))
# ---- Method 2
import decimal
print("Method 2", type(decimal.Decimal(10)))
print("Method 2", type(decimal.Decimal('10')))

# 49. Find the middle element in a list
print("Q49", ">"*50)
def middle_ele(user_list):
    try:
        mid_idx = int(len(user_list)/2)
        return user_list[mid_idx] 
    except:
        return  "This function only works with list and string"

print("Middle element of [2,5,6,1,2,5,5,10,2,2]: ", middle_ele([2,5,6,1,2,5,5,10,2,2]))
print("Middle element of ['a', 'd', 'z', 'q', 'a', 'a', 'z', 'c']: ", middle_ele(['a', 'd', 'z', 'q', 'a', 'a', 'z', 'c']))
print("Middle element of 'ABABRT': ", middle_ele("ABABR"))
print("Middle element of 'ABABRTabyzq': ", middle_ele("ABABRTabyzq")) 
print("Middle element of  43545", middle_ele(43545))

# 50. Convert a list to string
print("Q50", ">"*50)
print("List to string:", "".join(['a', 'd', 'z', 'q', 'a', 'a', 'z', 'c']))

# 51. Count whitespace in sentence
print("Q51", ">"*50)
# ----- Method 1
print("Countwhitespace in sentence: ", "Python is a beautiful language".count(" "))  
print("Countwhitespace in sentence: ", ("Python  !".count(" ")))  
print("Countwhitespace in sentence: ", ("Python  !".count(' '))) 
# ----- Method 2
def count_space(user_sen):
    if isinstance(user_sen, str):
        counter = 0
        for ele in user_sen:
            if ele == " ":
                counter += 1
    return counter
print("Countwhitespace in sentence: ", count_space("Python is a beautiful language !"))  
print("Countwhitespace in sentence: ", count_space("Python  !"))  

# 52. Count letters, digits and space - RegEx
print("Q52", ">"*50)
def no_le_di_sp(user_sen):
    if isinstance(user_sen, str):
        look_for = '0123456789'

# 53. Count special charaters in a string
print("Q53", ">"*50)
# 54. Remove all whitepspace in a string
print("Q54", ">"*50)
# ------ Method 1
def rem_whitespc(user_sen):
    upd_sen = ""
    for char in user_sen:
        if char != " ":
            upd_sen += char
    return upd_sen
print("Remove all whitespace - Method 1: ", rem_whitespc("p y t h o n") )

# ------ Method 2
print("Remove all whitespace - Method 2: ", ("p y t h o n").replace(" ", "") )

# ------ Method 3
print("Remove all whitespace - Method 3: ", "".join(char for char in "p y t h o n" if char != " " ))

# ------ Method 4
import re
print("Remove all whitespace - Method 4: ", re.sub(re.compile(r'\s+'), "", ("p y t h o n")))

# 55. Implementing a function for calculating average which should consider any number of enteries
print("Q55", ">"*50)
def avg(*t):
    return sum(t)/len(t)

print("Avergae: ", avg(2,4,5,3))
print("Avergae: ", avg(2,4,5,3, 2,4,5,3))

# 56. Addition using lambda function
print("Q56", ">"*50)
print( "Addition :", (lambda x, y: x+y)(3,7))

# 57. Write a python program to sort the elements of a list in ascending order
print("Q57", ">"*50)
# def sorting(user_list):
#     user_list_copy = user_list.copy()
#     upd_lst = []

#     arr_lst = [min(user_list_copy)]
#     min_ele = min(user_list_copy)

#     while len(user_list_copy) > 0:
#         print(min_ele, arr_lst, upd_lst)
#         upd_lst = user_list_copy.remove(min_ele)
#         min_ele = min(upd_lst)
#         arr_lst.append(min_ele)
#     # num = user_list[0]
#     # for ele in user_list:
#     return upd_lst

def sorting(user_list):
    unsorted = user_list.copy()  # avoid modifying original list
    sorted_list = []
    while unsorted: # Keep looping as long as the unsorted list is not empty i.e. while len(unsorted) > 0: 
        min_ele = min(unsorted) # runs, because unsorted list is not empty
        sorted_list.append(min_ele)
        unsorted.remove(min_ele)  # remove one occurrence
    return sorted_list


print("Min try: ", sorting([4, 7, 8,10,2,9]) )
breakpoint()
# print(f"var1 is of type: {check_type(var1)}") - How to write this? understand

print("End")
breakpoint()
