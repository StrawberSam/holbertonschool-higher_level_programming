## Resources

**Read or watch**:

*   [Object Oriented Programming](/rltoken/5envVBirO286MdSZgZ4DoQ "Object Oriented Programming") (_Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod` and `staticmethod` yet_)
*   [Object-Oriented Programming](/rltoken/sCdUrEsHLFH2NpUzI5Xx8w "Object-Oriented Programming") (_Please \*_be careful\*_: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The `__init__` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”_)
*   [Properties vs. Getters and Setters](/rltoken/3B0RWILA_kSjK5udEbFt-A "Properties vs. Getters and Setters")
*   [Learn to Program 9 : Object Oriented Programming](/rltoken/5u8UhnaTWX2A-G7LICKCDw "Learn to Program 9 : Object Oriented Programming")
*   [Python Classes and Objects](/rltoken/cwqg7Ud04LTDsatPT17CaQ "Python Classes and Objects")
*   [Object Oriented Programming](/rltoken/6cZhWLe083CJERYLjAM0BQ "Object Oriented Programming")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/gwuqSZXS7ElRbiObQzDcTg "explain to anyone"), **without the help of Google**:

### General

*   What is OOP
*   “first-class everything”
*   What is a class
*   What is an object and an instance
*   What is the difference between a class and an object or instance
*   What is an attribute
*   What are and how to use public, protected and private attributes
*   What is `self`
*   What is a method
*   What is the special `__init__` method and how to use it
*   What is Data Abstraction, Data Encapsulation, and Information Hiding
*   What is a property
*   What is the difference between an attribute and a property in Python
*   What is the Pythonic way to write getters and setters in Python
*   How to dynamically create arbitrary new attributes for existing instances of a class
*   How to bind attributes to object and classes
*   What is the `__dict__` of a class and/or instance of a class and what does it contain
*   How does Python find the attributes of an object or class
*   How to use the `getattr` function

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
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

### 1.

Write an empty class `Square` that defines a square:

*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = \_\_import\_\_('0-square').Square

my\_square = Square()
print(type(my\_square))
print(my\_square.\_\_dict\_\_)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/$
```


### 2.

Write a class `Square` that defines a square by: (based on `0-square.py`)

*   Private instance attribute: `size`
*   Instantiation with `size` (no type/value verification)
*   You are not allowed to import any module

**Why?**

_Why `size` is private attribute?_

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Square = \_\_import\_\_('1-square').Square

my\_square = Square(3)
print(type(my\_square))
print(my\_square.\_\_dict\_\_)

try:
    print(my\_square.size)
except Exception as e:
    print(e)

try:
    print(my\_square.\_\_size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./1-main.py
<class '1-square.Square'>
{'\_Square\_\_size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '\_\_size'
guillaume@ubuntu:~/$
```


### 3.

Write a class `Square` that defines a square by: (based on `1-square.py`)

*   Private instance attribute: `size`
*   Instantiation with optional `size`: `def __init__(self, size=0):`
    *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`

    *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Square = \_\_import\_\_('2-square').Square

my\_square\_1 = Square(3)
print(type(my\_square\_1))
print(my\_square\_1.\_\_dict\_\_)

my\_square\_2 = Square()
print(type(my\_square\_2))
print(my\_square\_2.\_\_dict\_\_)

try:
    print(my\_square\_1.size)
except Exception as e:
    print(e)

try:
    print(my\_square\_1.\_\_size)
except Exception as e:
    print(e)

try:
    my\_square\_3 = Square("3")
    print(type(my\_square\_3))
    print(my\_square\_3.\_\_dict\_\_)
except Exception as e:
    print(e)

try:
    my\_square\_4 = Square(-89)
    print(type(my\_square\_4))
    print(my\_square\_4.\_\_dict\_\_)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./2-main.py
<class '2-square.Square'>
{'\_Square\_\_size': 3}
<class '2-square.Square'>
{'\_Square\_\_size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '\_\_size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/$
```


### 4.

Write a class `Square` that defines a square by: (based on `2-square.py`)

*   Private instance attribute: `size`
*   Instantiation with optional `size`: `def __init__(self, size=0):`
    *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`

    *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
*   Public instance method: `def area(self):` that returns the current square area
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Square = \_\_import\_\_('3-square').Square

my\_square\_1 = Square(3)
print("Area: {}".format(my\_square\_1.area()))

try:
    print(my\_square\_1.size)
except Exception as e:
    print(e)

try:
    print(my\_square\_1.\_\_size)
except Exception as e:
    print(e)

my\_square\_2 = Square(5)
print("Area: {}".format(my\_square\_2.area()))

guillaume@ubuntu:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '\_\_size'
Area: 25
guillaume@ubuntu:~/$
```


### 5.

Write a class `Square` that defines a square by: (based on `3-square.py`)

*   Private instance attribute: `size`:
    *   property `def size(self):` to retrieve it
    *   property setter `def size(self, value):` to set it:
        *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`

        *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
*   Instantiation with optional `size`: `def __init__(self, size=0):`
*   Public instance method: `def area(self):` that returns the current square area
*   You are not allowed to import any module

**Why?**

_Why a getter and setter?_

Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Square = \_\_import\_\_('4-square').Square

my\_square = Square(89)
print("Area: {} for size: {}".format(my\_square.area(), my\_square.size))

my\_square.size = 3
print("Area: {} for size: {}".format(my\_square.area(), my\_square.size))

try:
    my\_square.size = "5 feet"
    print("Area: {} for size: {}".format(my\_square.area(), my\_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/$
```


### 6.

Write a class `Square` that defines a square by: (based on `4-square.py`)

*   Private instance attribute: `size`:
    *   property `def size(self):` to retrieve it
    *   property setter `def size(self, value):` to set it:
        *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`

        *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
*   Instantiation with optional `size`: `def __init__(self, size=0):`
*   Public instance method: `def area(self):` that returns the current square area
*   Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    *   if `size` is equal to 0, print an empty line
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Square = \_\_import\_\_('5-square').Square

my\_square = Square(3)
my\_square.my\_print()

print("--")

my\_square.size = 10
my\_square.my\_print()

print("--")

my\_square.size = 0
my\_square.my\_print()

print("--")

guillaume@ubuntu:~/$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/$
```


### 7.

Write a class `Square` that defines a square by: (based on `5-square.py`)

*   Private instance attribute: `size`:
    *   property `def size(self):` to retrieve it
    *   property setter `def size(self, value):` to set it:
        *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`

        *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
*   Private instance attribute: `position`:
    *   property `def position(self):` to retrieve it
    *   property setter `def position(self, value):` to set it:
        *   `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`

*   Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
*   Public instance method: `def area(self):` that returns the current square area
*   Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    *   if `size` is equal to 0, print an empty line
    *   `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Square = \_\_import\_\_('6-square').Square

my\_square\_1 = Square(3)
my\_square\_1.my\_print()

print("--")

my\_square\_2 = Square(3, (1, 1))
my\_square\_2.my\_print()

print("--")

my\_square\_3 = Square(3, (3, 0))
my\_square\_3.my\_print()

print("--")

guillaume@ubuntu:~/$ ./6-main.py | tr " " "\_" | cat -e
###$
###$
###$
--$
$
\_###$
\_###$
\_###$
--$
\_\_\_###$
\_\_\_###$
\_\_\_###$
--$
guillaume@ubuntu:~/$
```
