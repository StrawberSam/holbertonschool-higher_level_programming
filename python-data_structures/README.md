## Resources

**Read or watch**:

*   [3.1.3. Lists](/rltoken/UCQlbIrhZJVRfxndAcskkw "3.1.3. Lists")
*   [Data structures](/rltoken/89W42byWTSM4e25VSPKMRg "Data structures") (_until `5.3. Tuples and Sequences` included_)
*   [Learn to Program 6 : Lists](/rltoken/JNLdadDW7IWjwW9dbcEyhg "Learn to Program 6 : Lists")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/EKmHTirCHjvH-IXbBEzi8g "explain to anyone"), **without the help of Google**:

### General

*   What are lists and how to use them
*   What are the differences and similarities between strings and lists
*   What are the most common methods of lists and how to use them
*   How to use lists as stacks and queues
*   What are list comprehensions and how to use them
*   What are tuples and how to use them
*   When to use tuples versus lists
*   What is a sequence
*   What is tuple packing
*   What is sequence unpacking
*   What is the `del` statement and how to use it

## Requirements

### Python Scripts

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

Write a function that prints all integers of a list.

*   Prototype: `def print_list_integer(my_list=[]):`
*   Format: one integer per line. See example
*   You are not allowed to import any module
*   You can assume that the list only contains integers
*   You are not allowed to cast integers into strings
*   You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
print\_list\_integer = \_\_import\_\_('0-print\_list\_integer').print\_list\_integer

my\_list = \[1, 2, 3, 4, 5\]
print\_list\_integer(my\_list)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/$
```


### 2.

Write a function that retrieves an element from a list.

*   Prototype: `def element_at(my_list, idx):`
*   If `idx` is negative, the function should return `None`
*   If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
*   You are not allowed to import any module
*   You are not allowed to use `try/except`
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
element\_at = \_\_import\_\_('1-element\_at').element\_at

my\_list = \[1, 2, 3, 4, 5\]
idx = 3
print("Element at index {:d} is {}".format(idx, element\_at(my\_list, idx)))

guillaume@ubuntu:~/$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/$
```


### 3.

Write a function that replaces an element of a list at a specific position.

*   Prototype: `def replace_in_list(my_list, idx, element):`
*   If `idx` is negative, the function should not modify anything, and returns the original list
*   If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
*   You are not allowed to import any module
*   You are not allowed to use `try/except`
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
replace\_in\_list = \_\_import\_\_('2-replace\_in\_list').replace\_in\_list

my\_list = \[1, 2, 3, 4, 5\]
idx = 3
new\_element = 9
new\_list = replace\_in\_list(my\_list, idx, new\_element)

print(new\_list)
print(my\_list)

guillaume@ubuntu:~/$ ./2-main.py
\[1, 2, 3, 9, 5\]
\[1, 2, 3, 9, 5\]
guillaume@ubuntu:~/$
```


### 4.

Write a function that prints all integers of a list, in reverse order.

*   Prototype: `def print_reversed_list_integer(my_list=[]):`
*   Format: one integer per line. See example
*   You are not allowed to import any module
*   You can assume that the list only contains integers
*   You are not allowed to cast integers into strings
*   You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
print\_reversed\_list\_integer = \_\_import\_\_('3-print\_reversed\_list\_integer').print\_reversed\_list\_integer

my\_list = \[1, 2, 3, 4, 5\]
print\_reversed\_list\_integer(my\_list)

guillaume@ubuntu:~/$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/$
```


### 5.

Write a function that replaces an element in a list at a specific position without modifying the original list.

*   Prototype: `def new_in_list(my_list, idx, element):`
*   If `idx` is negative, the function should return a copy of the original `list`
*   If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
*   You are not allowed to import any module
*   You are not allowed to use `try/except`
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
new\_in\_list = \_\_import\_\_('4-new\_in\_list').new\_in\_list

my\_list = \[1, 2, 3, 4, 5\]
idx = 3
new\_element = 9
new\_list = new\_in\_list(my\_list, idx, new\_element)

print(new\_list)
print(my\_list)

guillaume@ubuntu:~/$ ./4-main.py
\[1, 2, 3, 9, 5\]
\[1, 2, 3, 4, 5\]
guillaume@ubuntu:~/$
```


### 6.

Write a function that removes all characters `c` and `C` from a string.

*   Prototype: `def no_c(my_string):`
*   The function should return the new string
*   You are not allowed to import any module
*   You are not allowed to use `str.replace()`
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
no\_c = \_\_import\_\_('5-no\_c').no\_c

print(no\_c("Best School"))
print(no\_c("Chicago"))
print(no\_c("C is fun!"))

guillaume@ubuntu:~/$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/$
```


### 7.

Write a function that prints a matrix of integers.

*   Prototype: `def print_matrix_integer(matrix=[[]]):`
*   Format: see example
*   You are not allowed to import any module
*   You can assume that the list only contains integers
*   You are not allowed to cast integers into strings
*   You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print\_matrix\_integer = \_\_import\_\_('6-print\_matrix\_integer').print\_matrix\_integer

matrix = \[
    \[1, 2, 3\],
    \[4, 5, 6\],
    \[7, 8, 9\]
\]

print\_matrix\_integer(matrix)
print("--")
print\_matrix\_integer()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/$
```


### 8.

Write a function that adds 2 tuples.

*   Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
*   Returns a tuple with 2 integers:
    *   The first element should be the addition of the first element of each argument
    *   The second element should be the addition of the second element of each argument
*   You are not allowed to import any module
*   You can assume that the two tuples will only contain integers
*   If a tuple is smaller than 2, use the value `0` for each missing integer
*   If a tuple is bigger than 2, use only the first 2 integers
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
add\_tuple = \_\_import\_\_('7-add\_tuple').add\_tuple

tuple\_a = (1, 89)
tuple\_b = (88, 11)
new\_tuple = add\_tuple(tuple\_a, tuple\_b)
print(new\_tuple)

print(add\_tuple(tuple\_a, (1, )))
print(add\_tuple(tuple\_a, ()))

guillaume@ubuntu:~/$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/$
```


### 9.

Write a function that returns a tuple with the length of a string and its first character.

*   Prototype: `def multiple_returns(sentence):`
*   If the sentence is empty, the first character should be equal to `None`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
multiple\_returns = \_\_import\_\_('8-multiple\_returns').multiple\_returns

sentence = "At school, I learnt C!"
length, first = multiple\_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/$
```


### 10.

Write a function that finds the biggest integer of a list.

*   Prototype: `def max_integer(my_list=[]):`
*   If the list is empty, return `None`
*   You can assume that the list only contains integers
*   You are not allowed to import any module
*   You are not allowed to use the builtin `max()`
```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
max\_integer = \_\_import\_\_('9-max\_integer').max\_integer

my\_list = \[1, 90, 2, 13, 34, 5, -13, 3\]
max\_value = max\_integer(my\_list)
print("Max: {}".format(max\_value))

guillaume@ubuntu:~/$ ./9-main.py
Max: 90
guillaume@ubuntu:~/$
```


### 11.

Write a function that finds all multiples of 2 in a list.

*   Prototype: `def divisible_by_2(my_list=[]):`
*   Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
*   The new list should have the same size as the original list
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
divisible\_by\_2 = \_\_import\_\_('10-divisible\_by\_2').divisible\_by\_2

my\_list = \[0, 1, 2, 3, 4, 5, 6\]
list\_result = divisible\_by\_2(my\_list)

i = 0
while i < len(list\_result):
    print("{:d} {:s} divisible by 2".format(my\_list\[i\], "is" if list\_result\[i\] else "is not"))
    i += 1

guillaume@ubuntu:~/$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/$
```


### 12.

Write a function that deletes the item at a specific position in a list.

*   Prototype: `def delete_at(my_list=[], idx=0):`
*   If `idx` is negative or out of range, nothing change (returns the same list)
*   You are not allowed to use `pop()`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
delete\_at = \_\_import\_\_('11-delete\_at').delete\_at

my\_list = \[1, 2, 3, 4, 5\]
idx = 3
new\_list = delete\_at(my\_list, idx)
print(new\_list)
print(my\_list)

guillaume@ubuntu:~/$ ./11-main.py
\[1, 2, 3, 5\]
\[1, 2, 3, 5\]
guillaume@ubuntu:~/$
```


### 13.

Complete the source code in order to switch value of `a` and `b`

*   You can find the source code [here](/rltoken/9viUCbnIwdfsOPV_UrvIRA "here")
*   Your code should be inserted where the comment is (line 4)
*   Your program should be exactly 5 lines long
```
guillaume@ubuntu:~/py/$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/$
```
