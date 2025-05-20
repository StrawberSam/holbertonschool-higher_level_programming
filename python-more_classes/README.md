## Resources

**Read or watch**:

*   [Object Oriented Programming](/rltoken/NxSyny_ojf0m2yY1FxhvsA "Object Oriented Programming") (_Read everything until the paragraph “Inheritance” (excluded)_)
*   [Object-Oriented Programming](/rltoken/PgSxX0FFvkpyAjNyoU0qcg "Object-Oriented Programming") (_Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The `__init__` Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “`__str__`\- and `__repr__`\-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”_)
*   [Class and Instance Attributes](/rltoken/2Lv-3qPSpQfC1VI52d9LZA "Class and Instance Attributes")
*   [classmethods and staticmethods](/rltoken/18KAvV_Ife9t5o3HYXj9DQ "classmethods and staticmethods")
*   [Properties vs. Getters and Setters](/rltoken/uHYbs5bXkYo6KvTtT6K5Sg "Properties vs. Getters and Setters") (_Mainly the last part “Public instead of Private Attributes”_)
*   [str vs repr](/rltoken/I0LZ2eMDlX6Fc-vrJvY5fA "str vs repr")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/TUamWq6RTFPs75ESaJtOcg "explain to anyone"), **without the help of Google**:

### General

*   Why Python programming is awesome
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
*   What are the special `__str__` and `__repr__` methods and how to use them
*   What is the difference between `__str__` and `__repr__`
*   What is a class attribute
*   What is the difference between a object attribute and a class attribute
*   What is a class method
*   What is a static method
*   How to dynamically create arbitrary new attributes for existing instances of a class
*   How to bind attributes to object and classes
*   What is and what does contain `__dict__` of a class and of an instance of a class
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

## Tasks

### 1.

Write an empty class `Rectangle` that defines a rectangle:

*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('0-rectangle').Rectangle

my\_rectangle = Rectangle()
print(type(my\_rectangle))
print(my\_rectangle.\_\_dict\_\_)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/$
```
**No test cases needed**



### 2.

Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)

*   Private instance attribute: `width`:
    *   property `def width(self):` to retrieve it
    *   property setter `def width(self, value):` to set it:
        *   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`

        *   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
*   Private instance attribute: `height`:
    *   property `def height(self):` to retrieve it
    *   property setter `def height(self, value):` to set it:
        *   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`

        *   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
*   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('1-rectangle').Rectangle

my\_rectangle = Rectangle(2, 4)
print(my\_rectangle.\_\_dict\_\_)

my\_rectangle.width = 10
my\_rectangle.height = 3
print(my\_rectangle.\_\_dict\_\_)

guillaume@ubuntu:~/$ ./1-main.py
{'\_Rectangle\_\_width': 2, '\_Rectangle\_\_height': 4}
{'\_Rectangle\_\_width': 10, '\_Rectangle\_\_height': 3}
guillaume@ubuntu:~/$
```
**No test cases needed**



### 3.

Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)

*   Private instance attribute: `width`:
    *   property `def width(self):` to retrieve it
    *   property setter `def width(self, value):` to set it:
        *   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`

        *   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
*   Private instance attribute: `height`:
    *   property `def height(self):` to retrieve it
    *   property setter `def height(self, value):` to set it:
        *   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`

        *   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
*   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
*   Public instance method: `def area(self):` that returns the rectangle area
*   Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    *   if `width` or `height` is equal to `0`, perimeter is equal to `0`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('2-rectangle').Rectangle

my\_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my\_rectangle.area(), my\_rectangle.perimeter()))

print("--")

my\_rectangle.width = 10
my\_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my\_rectangle.area(), my\_rectangle.perimeter()))

guillaume@ubuntu:~/$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/$
```
**No test cases needed**



### 4.

Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)

*   Private instance attribute: `width`:
    *   property `def width(self):` to retrieve it
    *   property setter `def width(self, value):` to set it:
        *   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`

        *   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
*   Private instance attribute: `height`:
    *   property `def height(self):` to retrieve it
    *   property setter `def height(self, value):` to set it:
        *   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`

        *   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
*   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
*   Public instance method: `def area(self):` that returns the rectangle area
*   Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    *   if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
*   `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    *   if `width` or `height` is equal to 0, return an empty string
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('3-rectangle').Rectangle

my\_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my\_rectangle.area(), my\_rectangle.perimeter()))

print(str(my\_rectangle))
print(repr(my\_rectangle))

print("--")

my\_rectangle.width = 10
my\_rectangle.height = 3
print(my\_rectangle)
print(repr(my\_rectangle))

guillaume@ubuntu:~/$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/$
```
**Object address can be differentNo test cases needed**



### 5.

Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)

*   Private instance attribute: `width`:
    *   property `def width(self):` to retrieve it
    *   property setter `def width(self, value):` to set it:
        *   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`

        *   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
*   Private instance attribute: `height`:
    *   property `def height(self):` to retrieve it
    *   property setter `def height(self, value):` to set it:
        *   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`

        *   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
*   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
*   Public instance method: `def area(self):` that returns the rectangle area
*   Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    *   if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
*   `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    *   if `width` or `height` is equal to 0, return an empty string
*   `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('4-rectangle').Rectangle

my\_rectangle = Rectangle(2, 4)
print(str(my\_rectangle))
print("--")
print(my\_rectangle)
print("--")
print(repr(my\_rectangle))
print("--")
print(hex(id(my\_rectangle)))
print("--")

# create new instance based on representation
new\_rectangle = eval(repr(my\_rectangle))
print(str(new\_rectangle))
print("--")
print(new\_rectangle)
print("--")
print(repr(new\_rectangle))
print("--")
print(hex(id(new\_rectangle)))
print("--")

print(new\_rectangle is my\_rectangle)
print(type(new\_rectangle) is type(my\_rectangle))

guillaume@ubuntu:~/$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/$
```
**No test cases needed**



### 6.

Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)

*   Private instance attribute: `width`:
    *   property `def width(self):` to retrieve it
    *   property setter `def width(self, value):` to set it:
        *   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`

        *   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
*   Private instance attribute: `height`:
    *   property `def height(self):` to retrieve it
    *   property setter `def height(self, value):` to set it:
        *   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`

        *   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
*   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
*   Public instance method: `def area(self):` that returns the rectangle area
*   Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    *   if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
*   `print()` and `str()` should print the rectangle with the character `#`:
    *   if `width` or `height` is equal to 0, return an empty string
*   `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
*   Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('5-rectangle').Rectangle

my\_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my\_rectangle.area(), my\_rectangle.perimeter()))

del my\_rectangle

try:
    print(my\_rectangle)
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

guillaume@ubuntu:~/$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
\[NameError\] name 'my\_rectangle' is not defined
guillaume@ubuntu:~/$
```
**No test cases needed**



### 7.

Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)

*   Private instance attribute: `width`:
    *   property `def width(self):` to retrieve it
    *   property setter `def width(self, value):` to set it:
        *   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`

        *   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
*   Private instance attribute: `height`:
    *   property `def height(self):` to retrieve it
    *   property setter `def height(self, value):` to set it:
        *   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`

        *   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
*   Public class attribute `number_of_instances`:
    *   Initialized to `0`
    *   Incremented during each new instance instantiation
    *   Decremented during each instance deletion
*   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
*   Public instance method: `def area(self):` that returns the rectangle area
*   Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    *   if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
*   `print()` and `str()` should print the rectangle with the character `#`:
    *   if `width` or `height` is equal to 0, return an empty string
*   `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
*   Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('6-rectangle').Rectangle

my\_rectangle\_1 = Rectangle(2, 4)
my\_rectangle\_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number\_of\_instances))
del my\_rectangle\_1
print("{:d} instances of Rectangle".format(Rectangle.number\_of\_instances))
del my\_rectangle\_2
print("{:d} instances of Rectangle".format(Rectangle.number\_of\_instances))

guillaume@ubuntu:~/$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/$
```
**No test cases needed**



### 8.

Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)

*   Private instance attribute: `width`:
    *   property `def width(self):` to retrieve it
    *   property setter `def width(self, value):` to set it:
        *   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`

        *   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
*   Private instance attribute: `height`:
    *   property `def height(self):` to retrieve it
    *   property setter `def height(self, value):` to set it:
        *   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`

        *   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
*   Public class attribute `number_of_instances`:
    *   Initialized to `0`
    *   Incremented during each new instance instantiation
    *   Decremented during each instance deletion
*   Public class attribute `print_symbol`:
    *   Initialized to `#`
    *   Used as symbol for string representation
    *   Can be any type
*   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
*   Public instance method: `def area(self):` that returns the rectangle area
*   Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    *   if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
*   `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`:
    *   if `width` or `height` is equal to 0, return an empty string
*   `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
*   Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('7-rectangle').Rectangle

my\_rectangle\_1 = Rectangle(8, 4)
print(my\_rectangle\_1)
print("--")
my\_rectangle\_1.print\_symbol = "&"
print(my\_rectangle\_1)
print("--")

my\_rectangle\_2 = Rectangle(2, 1)
print(my\_rectangle\_2)
print("--")
Rectangle.print\_symbol = "C"
print(my\_rectangle\_2)
print("--")

my\_rectangle\_3 = Rectangle(7, 3)
print(my\_rectangle\_3)

print("--")

my\_rectangle\_3.print\_symbol = \["C", "is", "fun!"\]
print(my\_rectangle\_3)

print("--")

guillaume@ubuntu:~/$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]
\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]
\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]\['C', 'is', 'fun!'\]
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/$
```
**No test cases needed**



### 9.

Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)

*   Private instance attribute: `width`:
    *   property `def width(self):` to retrieve it
    *   property setter `def width(self, value):` to set it:
        *   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`

        *   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
*   Private instance attribute: `height`:
    *   property `def height(self):` to retrieve it
    *   property setter `def height(self, value):` to set it:
        *   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`

        *   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
*   Public class attribute `number_of_instances`:
    *   Initialized to `0`
    *   Incremented during each new instance instantiation
    *   Decremented during each instance deletion
*   Public class attribute `print_symbol`:
    *   Initialized to `#`
    *   Used as symbol for string representation
    *   Can be any type
*   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
*   Public instance method: `def area(self):` that returns the rectangle area
*   Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    *   if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
*   `print()` and `str()` should print the rectangle with the character `#`:
    *   if `width` or `height` is equal to 0, return an empty string
*   `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
*   Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
*   Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
    *   `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`

    *   `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`

    *   Returns `rect_1` if both have the same area value
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('8-rectangle').Rectangle

my\_rectangle\_1 = Rectangle(8, 4)
my\_rectangle\_2 = Rectangle(2, 3)

if my\_rectangle\_1 is Rectangle.bigger\_or\_equal(my\_rectangle\_1, my\_rectangle\_2):
    print("my\_rectangle\_1 is bigger or equal to my\_rectangle\_2")
else:
    print("my\_rectangle\_2 is bigger than my\_rectangle\_1")

my\_rectangle\_2.width = 10
my\_rectangle\_2.height = 5
if my\_rectangle\_1 is Rectangle.bigger\_or\_equal(my\_rectangle\_1, my\_rectangle\_2):
    print("my\_rectangle\_1 is bigger or equal to my\_rectangle\_2")
else:
    print("my\_rectangle\_2 is bigger than my\_rectangle\_1")

guillaume@ubuntu:~/$ ./8-main.py
my\_rectangle\_1 is bigger or equal to my\_rectangle\_2
my\_rectangle\_2 is bigger than my\_rectangle\_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/$
```
**No test cases needed**



### 10.

Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)

*   Private instance attribute: `width`:
    *   property `def width(self):` to retrieve it
    *   property setter `def width(self, value):` to set it:
        *   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`

        *   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
*   Private instance attribute: `height`:
    *   property `def height(self):` to retrieve it
    *   property setter `def height(self, value):` to set it:
        *   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`

        *   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
*   Public class attribute `number_of_instances`:
    *   Initialized to `0`
    *   Incremented during each new instance instantiation
    *   Decremented during each instance deletion
*   Public class attribute `print_symbol`:
    *   Initialized to `#`
    *   Used as symbol for string representation
    *   Can be any type
*   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
*   Public instance method: `def area(self):` that returns the rectangle area
*   Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    *   if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
*   `print()` and `str()` should print the rectangle with the character `#`:
    *   if `width` or `height` is equal to 0, return an empty string
*   `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
*   Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
*   Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
    *   `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`

    *   `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`

    *   Returns `rect_1` if both have the same area value
*   Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('9-rectangle').Rectangle

my\_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my\_square.area(), my\_square.perimeter()))
print(my\_square)

guillaume@ubuntu:~/$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/$
```
**No test cases needed**
