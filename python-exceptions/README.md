## Resources

**Read or watch**:

*   [Errors and Exceptions](/rltoken/WxV68L6c_WRMEzZt8P7oIA "Errors and Exceptions")
*   [Learn to Program 11 Static & Exception Handling](/rltoken/OTYmJ8UpJotqIVyrVgSL4A "Learn to Program 11 Static & Exception Handling") (_starting at minute 7_)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/TnecOG_n964IZ9aQvErdtQ "explain to anyone"), **without the help of Google**:

### General

*   Why Python programming is awesome
*   What’s the difference between errors and exceptions
*   What are exceptions and how to use them
*   When do we need to use exceptions
*   How to correctly handle an exception
*   What’s the purpose of catching exceptions
*   How to raise a builtin exception
*   When do we need to implement a clean-up action after an exception

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

Write a function that prints `x` elements of a list.

*   Prototype: `def safe_print_list(my_list=[], x=0):`
*   `my_list` can contain any type (integer, string, etc.)
*   All elements must be printed on the same line followed by a new line.
*   `x` represents the number of elements to print
*   `x` can be bigger than the length of `my_list`
*   Returns the real number of elements printed
*   You have to use `try: / except:`
*   You are not allowed to import any module
*   You are not allowed to use `len()`
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
safe\_print\_list = \_\_import\_\_('0-safe\_print\_list').safe\_print\_list

my\_list = \[1, 2, 3, 4, 5\]

nb\_print = safe\_print\_list(my\_list, 2)
print("nb\_print: {:d}".format(nb\_print))
nb\_print = safe\_print\_list(my\_list, len(my\_list))
print("nb\_print: {:d}".format(nb\_print))
nb\_print = safe\_print\_list(my\_list, len(my\_list) + 2)
print("nb\_print: {:d}".format(nb\_print))

guillaume@ubuntu:~/$ ./0-main.py
12
nb\_print: 2
12345
nb\_print: 5
12345
nb\_print: 5
guillaume@ubuntu:~/$
```


### 2.

Write a function that prints an integer with `"{:d}".format()`.

*   Prototype: `def safe_print_integer(value):`
*   `value` can be any type (integer, string, etc.)
*   The integer should be printed followed by a new line
*   Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
*   Otherwise, returns `False`
*   You have to use `try: / except:`
*   You have to use `"{:d}".format()` to print as integer
*   You are not allowed to import any module
*   You are not allowed to use `type()`
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
safe\_print\_integer = \_\_import\_\_('1-safe\_print\_integer').safe\_print\_integer

value = 89
has\_been\_print = safe\_print\_integer(value)
if not has\_been\_print:
    print("{} is not an integer".format(value))

value = -89
has\_been\_print = safe\_print\_integer(value)
if not has\_been\_print:
    print("{} is not an integer".format(value))

value = "School"
has\_been\_print = safe\_print\_integer(value)
if not has\_been\_print:
    print("{} is not an integer".format(value))

guillaume@ubuntu:~/$ ./1-main.py
89
-89
School is not an integer
guillaume@ubuntu:~/$
```


### 3.

Write a function that prints the first `x` elements of a list and only integers.

*   Prototype: `def safe_print_list_integers(my_list=[], x=0):`
*   `my_list` can contain any type (integer, string, etc.)
*   All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
*   `x` represents the number of elements to access in `my_list`
*   `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
*   Returns the real number of integers printed
*   You have to use `try: / except:`
*   You have to use `"{:d}".format()` to print an integer
*   You are not allowed to import any module
*   You are not allowed to use `len()`
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
safe\_print\_list\_integers = \\
    \_\_import\_\_('2-safe\_print\_list\_integers').safe\_print\_list\_integers

my\_list = \[1, 2, 3, 4, 5\]

nb\_print = safe\_print\_list\_integers(my\_list, 2)
print("nb\_print: {:d}".format(nb\_print))

my\_list = \[1, 2, 3, "School", 4, 5, \[1, 2, 3\]\]
nb\_print = safe\_print\_list\_integers(my\_list, len(my\_list))
print("nb\_print: {:d}".format(nb\_print))

nb\_print = safe\_print\_list\_integers(my\_list, len(my\_list) + 2)
print("nb\_print: {:d}".format(nb\_print))

guillaume@ubuntu:~/$ ./2-main.py
12
nb\_print: 2
12345
nb\_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb\_print = safe\_print\_list\_integers(my\_list, len(my\_list) + 2)
  File "//2-safe\_print\_list\_integers.py", line 7, in safe\_print\_list\_integers
    print("{:d}".format(my\_list\[i\]), end="")
IndexError: list index out of range
guillaume@ubuntu:~/$
```


### 4.

Write a function that divides 2 integers and prints the result.

*   Prototype: `def safe_print_division(a, b):`
*   You can assume that `a` and `b` are integers
*   The result of the division should print on the `finally:` section preceded by `Inside result:`
*   Returns the value of the division, otherwise: `None`
*   You have to use `try: / except: / finally:`
*   You have to use `"{}".format()` to print the result
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
safe\_print\_division = \_\_import\_\_('3-safe\_print\_division').safe\_print\_division

a = 12
b = 2
result = safe\_print\_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe\_print\_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

guillaume@ubuntu:~/$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/$
```


### 5.

Write a function that divides element by element 2 lists.

*   Prototype: `def list_division(my_list_1, my_list_2, list_length):`
*   `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
*   `list_length` can be bigger than the length of both lists
*   Returns a new list (length = `list_length`) with all divisions
*   If 2 elements can’t be divided, the division result should be equal to `0`
*   If an element is not an integer or float:
    *   print: `wrong type`
*   If the division can’t be done (`/0`):
    *   print: `division by 0`
*   If `my_list_1` or `my_list_2` is too short
    *   print: `out of range`
*   You have to use `try: / except: / finally:`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
list\_division = \_\_import\_\_('4-list\_division').list\_division

my\_l\_1 = \[10, 8, 4\]
my\_l\_2 = \[2, 4, 4\]
result = list\_division(my\_l\_1, my\_l\_2, max(len(my\_l\_1), len(my\_l\_2)))
print(result)

print("--")

my\_l\_1 = \[10, 8, 4, 4\]
my\_l\_2 = \[2, 0, "H", 2, 7\]
result = list\_division(my\_l\_1, my\_l\_2, max(len(my\_l\_1), len(my\_l\_2)))
print(result)

guillaume@ubuntu:~/$ ./4-main.py
\[5.0, 2.0, 1.0\]
--
division by 0
wrong type
out of range
\[5.0, 0, 0, 2.0, 0\]
guillaume@ubuntu:~/$
```


### 6.

Write a function that raises a type exception.

*   Prototype: `def raise_exception():`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
raise\_exception = \_\_import\_\_('5-raise\_exception').raise\_exception

try:
    raise\_exception()
except TypeError as te:
    print("Exception raised")

guillaume@ubuntu:~/$ ./5-main.py
Exception raised
guillaume@ubuntu:~/$
```


### 7.

Write a function that raises a name exception with a message.

*   Prototype: `def raise_exception_msg(message=""):`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
raise\_exception\_msg = \_\_import\_\_('6-raise\_exception\_msg').raise\_exception\_msg

try:
    raise\_exception\_msg("C is fun")
except NameError as ne:
    print(ne)

guillaume@ubuntu:~/$ ./6-main.py
C is fun
guillaume@ubuntu:~/$
```
