## Resources

**Read or watch**:

*   [Data structures](/rltoken/K8JSw_eMWjw6EzmAL1S8bQ "Data structures")
*   [Lambda, filter, reduce and map](/rltoken/JMc02-iMawLlxGCsnEalXA "Lambda, filter, reduce and map")
*   [Learn to Program 12 Lambda Map Filter Reduce](/rltoken/NnWm29rFmdDcjcdRQX1tEw "Learn to Program 12 Lambda Map Filter Reduce")

**man or help**:

*   `python3`

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/XpnbqLab-uqqsit6p5ifxA "explain to anyone"), **without the help of Google**:

### General

*   Why Python programming is awesome
*   What are sets and how to use them
*   What are the most common methods of set and how to use them
*   When to use sets versus lists
*   How to iterate into a set
*   What are dictionaries and how to use them
*   When to use dictionaries versus lists or sets
*   What is a key in a dictionary
*   How to iterate over a dictionary
*   What is a lambda function
*   What are the map, reduce and filter functions

## Requirements

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version 2.7.\*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

## Tasks

### 1.

Write a function that computes the square value of all integers of a matrix.

*   Prototype: `def square_matrix_simple(matrix=[]):`
*   `matrix` is a 2 dimensional array
*   Returns a new matrix:
    *   Same size as `matrix`
    *   Each value should be the square of the value of the input
*   Initial matrix should not be modified
*   You are not allowed to import any module
*   You are allowed to use regular loops, `map`, etc.
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
square\_matrix\_simple = \_\_import\_\_('0-square\_matrix\_simple').square\_matrix\_simple

matrix = \[
    \[1, 2, 3\],
    \[4, 5, 6\],
    \[7, 8, 9\]
\]

new\_matrix = square\_matrix\_simple(matrix)
print(new\_matrix)
print(matrix)

guillaume@ubuntu:~/$ ./0-main.py
\[\[1, 4, 9\], \[16, 25, 36\], \[49, 64, 81\]\]
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]
guillaume@ubuntu:~/$
```


### 2.

Write a function that replaces all occurrences of an element by another in a new list.

*   Prototype: `def search_replace(my_list, search, replace):`
*   `my_list` is the initial list
*   `search` is the element to replace in the list
*   `replace` is the new element
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
search\_replace = \_\_import\_\_('1-search\_replace').search\_replace

my\_list = \[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89\]
new\_list = search\_replace(my\_list, 2, 89)

print(new\_list)
print(my\_list)

guillaume@ubuntu:~/$ ./1-main.py
\[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89\]
\[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89\]
guillaume@ubuntu:~/$
```


### 3.

Write a function that adds all unique integers in a list (only once for each integer).

*   Prototype: `def uniq_add(my_list=[]):`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
uniq\_add = \_\_import\_\_('2-uniq\_add').uniq\_add

my\_list = \[1, 2, 3, 1, 4, 2, 5\]
result = uniq\_add(my\_list)
print("Result: {:d}".format(result))

guillaume@ubuntu:~/$ ./2-main.py
Result: 15
guillaume@ubuntu:~/$
```


### 4.

Write a function that returns a set of common elements in two sets.

*   Prototype: `def common_elements(set_1, set_2):`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
common\_elements = \_\_import\_\_('3-common\_elements').common\_elements

set\_1 = { "Python", "C", "Javascript" }
set\_2 = { "Bash", "C", "Ruby", "Perl" }
c\_set = common\_elements(set\_1, set\_2)
print(sorted(list(c\_set)))

guillaume@ubuntu:~/$ ./3-main.py
\['C'\]
guillaume@ubuntu:~/$
```


### 5.

Write a function that returns a set of all elements present in only one set.

*   Prototype: `def only_diff_elements(set_1, set_2):`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
only\_diff\_elements = \_\_import\_\_('4-only\_diff\_elements').only\_diff\_elements

set\_1 = { "Python", "C", "Javascript" }
set\_2 = { "Bash", "C", "Ruby", "Perl" }
od\_set = only\_diff\_elements(set\_1, set\_2)
print(sorted(list(od\_set)))

guillaume@ubuntu:~/$ ./4-main.py
\['Bash', 'Javascript', 'Perl', 'Python', 'Ruby'\]
guillaume@ubuntu:~/$
```


### 6.

Write a function that returns the number of keys in a dictionary.

*   Prototype: `def number_keys(a_dictionary):`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
number\_keys = \_\_import\_\_('5-number\_keys').number\_keys

a\_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb\_keys = number\_keys(a\_dictionary)
print("Number of keys: {:d}".format(nb\_keys))

guillaume@ubuntu:~/$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/$
```


### 7.

Write a function that prints a dictionary by ordered keys.

*   Prototype: `def print_sorted_dictionary(a_dictionary):`
*   You can assume that all keys are strings
*   Keys should be sorted by alphabetic order
*   Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
*   Dictionary values can have any type
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print\_sorted\_dictionary = \_\_import\_\_('6-print\_sorted\_dictionary').print\_sorted\_dictionary

a\_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': \[1, 2, 3\] }
print\_sorted\_dictionary(a\_dictionary)

guillaume@ubuntu:~/$ ./6-main.py
Number: 89
ids: \[1, 2, 3\]
language: C
track: Low level
guillaume@ubuntu:~/$
```


### 8.

Write a function that replaces or adds key/value in a dictionary.

*   Prototype: `def update_dictionary(a_dictionary, key, value):`
*   `key` argument will be always a string
*   `value` argument will be any type
*   If a key exists in the dictionary, the value will be replaced
*   If a key doesn’t exist in the dictionary, it will be created
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
update\_dictionary = \_\_import\_\_('7-update\_dictionary').update\_dictionary
print\_sorted\_dictionary = \_\_import\_\_('6-print\_sorted\_dictionary').print\_sorted\_dictionary

a\_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new\_dict = update\_dictionary(a\_dictionary, 'language', "Python")
print\_sorted\_dictionary(new\_dict)
print("--")
print\_sorted\_dictionary(a\_dictionary)

print("--")
print("--")

new\_dict = update\_dictionary(a\_dictionary, 'city', "San Francisco")
print\_sorted\_dictionary(new\_dict)
print("--")
print\_sorted\_dictionary(a\_dictionary)

guillaume@ubuntu:~/$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/$
```


### 9.

Write a function that deletes a key in a dictionary.

*   Prototype: `def simple_delete(a_dictionary, key=""):`
*   `key` argument will be always a string
*   If a key doesn’t exist, the dictionary won’t change
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
simple\_delete = \_\_import\_\_('8-simple\_delete').simple\_delete
print\_sorted\_dictionary = \\
    \_\_import\_\_('6-print\_sorted\_dictionary').print\_sorted\_dictionary

a\_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': \[1, 2, 3\] }
new\_dict = simple\_delete(a\_dictionary, 'track')
print\_sorted\_dictionary(a\_dictionary)
print("--")
print\_sorted\_dictionary(new\_dict)

print("--")
print("--")
new\_dict = simple\_delete(a\_dictionary, 'c\_is\_fun')
print\_sorted\_dictionary(a\_dictionary)
print("--")
print\_sorted\_dictionary(new\_dict)

guillaume@ubuntu:~/$ ./8-main.py
Number: 89
ids: \[1, 2, 3\]
language: C
--
Number: 89
ids: \[1, 2, 3\]
language: C
--
--
Number: 89
ids: \[1, 2, 3\]
language: C
--
Number: 89
ids: \[1, 2, 3\]
language: C
guillaume@ubuntu:~/$
```


### 10.

Write a function that returns a new dictionary with all values multiplied by 2

*   Prototype: `def multiply_by_2(a_dictionary):`
*   You can assume that all values are only integers
*   Returns a new dictionary
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
multiply\_by\_2 = \_\_import\_\_('9-multiply\_by\_2').multiply\_by\_2
print\_sorted\_dictionary = \\
    \_\_import\_\_('6-print\_sorted\_dictionary').print\_sorted\_dictionary

a\_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new\_dict = multiply\_by\_2(a\_dictionary)
print\_sorted\_dictionary(a\_dictionary)
print("--")
print\_sorted\_dictionary(new\_dict)

guillaume@ubuntu:~/$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/$
```


### 11.

Write a function that returns a key with the biggest integer value.

*   Prototype: `def best_score(a_dictionary):`
*   You can assume that all values are only integers
*   If no score found, return `None`
*   You can assume all students have a different score
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
best\_score = \_\_import\_\_('10-best\_score').best\_score

a\_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best\_key = best\_score(a\_dictionary)
print("Best score: {}".format(best\_key))

best\_key = best\_score(None)
print("Best score: {}".format(best\_key))

guillaume@ubuntu:~/$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/$
```


### 12.

Write a function that returns a list with all values multiplied by a number without using any loops.

*   Prototype: `def multiply_list_map(my_list=[], number=0):`
*   Returns a new list:
    *   Same length as `my_list`
    *   Each value should be multiplied by `number`
*   Initial list should not be modified
*   You are not allowed to import any module
*   You have to use `map`
*   Your file should be max 3 lines
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
multiply\_list\_map = \_\_import\_\_('11-multiply\_list\_map').multiply\_list\_map

my\_list = \[1, 2, 3, 4, 6\]
new\_list = multiply\_list\_map(my\_list, 4)
print(new\_list)
print(my\_list)

guillaume@ubuntu:~/$ ./11-main.py
\[4, 8, 12, 16, 24\]
\[1, 2, 3, 4, 6\]
guillaume@ubuntu:~/$
```


### 13.

**Technical interview preparation**:

*   You are not allowed to google anything
*   Whiteboard first

Create a function `def roman_to_int(roman_string):` that converts a [Roman numeral](/rltoken/COeilkCPRPmrPvaRSXcPyg "Roman numeral") to an integer.

*   You can assume the number will be between 1 to 3999.
*   `def roman_to_int(roman_string)` must return an integer
*   If the `roman_string` is not a string or `None`, return 0
```
guillaume@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
""" Roman to Integer test file
"""
roman\_to\_int = \_\_import\_\_('12-roman\_to\_int').roman\_to\_int

roman\_number = "X"
print("{} = {}".format(roman\_number, roman\_to\_int(roman\_number)))

roman\_number = "VII"
print("{} = {}".format(roman\_number, roman\_to\_int(roman\_number)))

roman\_number = "IX"
print("{} = {}".format(roman\_number, roman\_to\_int(roman\_number)))

roman\_number = "LXXXVII"
print("{} = {}".format(roman\_number, roman\_to\_int(roman\_number)))

roman\_number = "DCCVII"
print("{} = {}".format(roman\_number, roman\_to\_int(roman\_number)))

guillaume@ubuntu:~/$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
guillaume@ubuntu:~/$
```
