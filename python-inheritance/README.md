## Resources

**Read or watch**:

*   [Inheritance](/rltoken/pRigaMtzlZIXHVXZJ7yRMQ "Inheritance")
*   [Multiple inheritance](/rltoken/q7hgZ43Gu_snerCNUwqzuw "Multiple inheritance")
*   [Inheritance in Python](/rltoken/04VYC46DWxWLhcUpRVmHGg "Inheritance in Python")
*   [Learn to Program 10 : Inheritance Magic Methods](/rltoken/fojEQ8bllfZecx-ZKKurTw "Learn to Program 10 : Inheritance Magic Methods")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/qtTNU4FKGaIHTtnDLLrVYQ "explain to anyone"), **without the help of Google**:

### General

*   What is a superclass, baseclass or parentclass
*   What is a subclass
*   How to list all attributes and methods of a class or instance
*   When can an instance have new attributes
*   How to inherit class from another
*   How to define a class with multiple base classes
*   What is the default class every class inherit from
*   How to override a method or attribute inherited from the base class
*   Which attributes or methods are available by heritage to subclasses
*   What is the purpose of inheritance
*   What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

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

### Python Test Cases

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files should end with a new line
*   All your test files should be inside a folder `tests`
*   All your test files should be text files (extension: `.txt`)
*   All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Documentation

*   Do not use the words `import` or `from` inside your comments, the checker will think you are trying to import some modules

## Tasks

### 1.

Write a function that returns the list of available attributes and methods of an object:

*   Prototype: `def lookup(obj):`
*   Returns a `list` object
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
lookup = \_\_import\_\_('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my\_attr1 = 3
    def my\_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

guillaume@ubuntu:~/$ ./0-main.py
\['\_\_class\_\_', '\_\_delattr\_\_', '\_\_dict\_\_', '\_\_dir\_\_', '\_\_doc\_\_', '\_\_eq\_\_', '\_\_format\_\_', '\_\_ge\_\_', '\_\_getattribute\_\_', '\_\_gt\_\_', '\_\_hash\_\_', '\_\_init\_\_', '\_\_le\_\_', '\_\_lt\_\_', '\_\_module\_\_', '\_\_ne\_\_', '\_\_new\_\_', '\_\_reduce\_\_', '\_\_reduce\_ex\_\_', '\_\_repr\_\_', '\_\_setattr\_\_', '\_\_sizeof\_\_', '\_\_str\_\_', '\_\_subclasshook\_\_', '\_\_weakref\_\_'\]
\['\_\_class\_\_', '\_\_delattr\_\_', '\_\_dict\_\_', '\_\_dir\_\_', '\_\_doc\_\_', '\_\_eq\_\_', '\_\_format\_\_', '\_\_ge\_\_', '\_\_getattribute\_\_', '\_\_gt\_\_', '\_\_hash\_\_', '\_\_init\_\_', '\_\_le\_\_', '\_\_lt\_\_', '\_\_module\_\_', '\_\_ne\_\_', '\_\_new\_\_', '\_\_reduce\_\_', '\_\_reduce\_ex\_\_', '\_\_repr\_\_', '\_\_setattr\_\_', '\_\_sizeof\_\_', '\_\_str\_\_', '\_\_subclasshook\_\_', '\_\_weakref\_\_', 'my\_attr1', 'my\_meth'\]
\['\_\_abs\_\_', '\_\_add\_\_', '\_\_and\_\_', '\_\_bool\_\_', '\_\_ceil\_\_', '\_\_class\_\_', '\_\_delattr\_\_', '\_\_dir\_\_', '\_\_divmod\_\_', '\_\_doc\_\_', '\_\_eq\_\_', '\_\_float\_\_', '\_\_floor\_\_', '\_\_floordiv\_\_', '\_\_format\_\_', '\_\_ge\_\_', '\_\_getattribute\_\_', '\_\_getnewargs\_\_', '\_\_gt\_\_', '\_\_hash\_\_', '\_\_index\_\_', '\_\_init\_\_', '\_\_int\_\_', '\_\_invert\_\_', '\_\_le\_\_', '\_\_lshift\_\_', '\_\_lt\_\_', '\_\_mod\_\_', '\_\_mul\_\_', '\_\_ne\_\_', '\_\_neg\_\_', '\_\_new\_\_', '\_\_or\_\_', '\_\_pos\_\_', '\_\_pow\_\_', '\_\_radd\_\_', '\_\_rand\_\_', '\_\_rdivmod\_\_', '\_\_reduce\_\_', '\_\_reduce\_ex\_\_', '\_\_repr\_\_', '\_\_rfloordiv\_\_', '\_\_rlshift\_\_', '\_\_rmod\_\_', '\_\_rmul\_\_', '\_\_ror\_\_', '\_\_round\_\_', '\_\_rpow\_\_', '\_\_rrshift\_\_', '\_\_rshift\_\_', '\_\_rsub\_\_', '\_\_rtruediv\_\_', '\_\_rxor\_\_', '\_\_setattr\_\_', '\_\_sizeof\_\_', '\_\_str\_\_', '\_\_sub\_\_', '\_\_subclasshook\_\_', '\_\_truediv\_\_', '\_\_trunc\_\_', '\_\_xor\_\_', 'bit\_length', 'conjugate', 'denominator', 'from\_bytes', 'imag', 'numerator', 'real', 'to\_bytes'\]
guillaume@ubuntu:~/$
```
**No test cases needed**



### 2.

Write a class `MyList` that inherits from `list`:

*   Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
*   You can assume that all the elements of the list will be of type `int`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
MyList = \_\_import\_\_('1-my\_list').MyList

my\_list = MyList()
my\_list.append(1)
my\_list.append(4)
my\_list.append(2)
my\_list.append(3)
my\_list.append(5)
print(my\_list)
my\_list.print\_sorted()
print(my\_list)

guillaume@ubuntu:~/$ ./1-main.py
\[1, 4, 2, 3, 5\]
\[1, 2, 3, 4, 5\]
\[1, 4, 2, 3, 5\]
guillaume@ubuntu:~/$
```


### 3.

Write a function that returns `True` if the object is _exactly_ an instance of the specified class ; otherwise `False`.

*   Prototype: `def is_same_class(obj, a_class):`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
is\_same\_class = \_\_import\_\_('2-is\_same\_class').is\_same\_class

a = 1
if is\_same\_class(a, int):
    print("{} is an instance of the class {}".format(a, int.\_\_name\_\_))
if is\_same\_class(a, float):
    print("{} is an instance of the class {}".format(a, float.\_\_name\_\_))
if is\_same\_class(a, object):
    print("{} is an instance of the class {}".format(a, object.\_\_name\_\_))

guillaume@ubuntu:~/$ ./2-main.py
1 is an instance of the class int
guillaume@ubuntu:~/$
```
**No test cases needed**



### 4.

Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

*   Prototype: `def is_kind_of_class(obj, a_class):`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
is\_kind\_of\_class = \_\_import\_\_('3-is\_kind\_of\_class').is\_kind\_of\_class

a = 1
if is\_kind\_of\_class(a, int):
    print("{} comes from {}".format(a, int.\_\_name\_\_))
if is\_kind\_of\_class(a, float):
    print("{} comes from {}".format(a, float.\_\_name\_\_))
if is\_kind\_of\_class(a, object):
    print("{} comes from {}".format(a, object.\_\_name\_\_))

guillaume@ubuntu:~/$ ./3-main.py
1 comes from int
1 comes from object
guillaume@ubuntu:~/$
```
**No test cases needed**



### 5.

Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

*   Prototype: `def inherits_from(obj, a_class):`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
inherits\_from = \_\_import\_\_('4-inherits\_from').inherits\_from

a = True
if inherits\_from(a, int):
    print("{} inherited from class {}".format(a, int.\_\_name\_\_))
if inherits\_from(a, bool):
    print("{} inherited from class {}".format(a, bool.\_\_name\_\_))
if inherits\_from(a, object):
    print("{} inherited from class {}".format(a, object.\_\_name\_\_))

guillaume@ubuntu:~/$ ./4-main.py
True inherited from class int
True inherited from class object
guillaume@ubuntu:~/$
```
**No test cases needed**



### 6.

Write an empty class `BaseGeometry`.

*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
BaseGeometry = \_\_import\_\_('5-base\_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

guillaume@ubuntu:~/$ ./5-main.py
<5-base\_geometry.BaseGeometry object at 0x7f2050c69208>
\['\_\_class\_\_', '\_\_delattr\_\_', '\_\_dict\_\_', '\_\_dir\_\_', '\_\_doc\_\_', '\_\_eq\_\_', '\_\_format\_\_', '\_\_ge\_\_', '\_\_getattribute\_\_', '\_\_gt\_\_', '\_\_hash\_\_', '\_\_init\_\_', '\_\_le\_\_', '\_\_lt\_\_', '\_\_module\_\_', '\_\_ne\_\_', '\_\_new\_\_', '\_\_reduce\_\_', '\_\_reduce\_ex\_\_', '\_\_repr\_\_', '\_\_setattr\_\_', '\_\_sizeof\_\_', '\_\_str\_\_', '\_\_subclasshook\_\_', '\_\_weakref\_\_'\]
\['\_\_class\_\_', '\_\_delattr\_\_', '\_\_dict\_\_', '\_\_dir\_\_', '\_\_doc\_\_', '\_\_eq\_\_', '\_\_format\_\_', '\_\_ge\_\_', '\_\_getattribute\_\_', '\_\_gt\_\_', '\_\_hash\_\_', '\_\_init\_\_', '\_\_le\_\_', '\_\_lt\_\_', '\_\_module\_\_', '\_\_ne\_\_', '\_\_new\_\_', '\_\_reduce\_\_', '\_\_reduce\_ex\_\_', '\_\_repr\_\_', '\_\_setattr\_\_', '\_\_sizeof\_\_', '\_\_str\_\_', '\_\_subclasshook\_\_', '\_\_weakref\_\_'\]
guillaume@ubuntu:~/$
```
**No test cases needed**



### 7.

Write a class `BaseGeometry` (based on `5-base_geometry.py`).

*   Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
BaseGeometry = \_\_import\_\_('6-base\_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

guillaume@ubuntu:~/$ ./6-main.py
\[Exception\] area() is not implemented
guillaume@ubuntu:~/$
```
**No test cases needed**



### 8.

Write a class `BaseGeometry` (based on `6-base_geometry.py`).

*   Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
*   Public instance method: `def integer_validator(self, name, value):` that validates `value`:
    *   you can assume `name` is always a string
    *   if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    *   if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
BaseGeometry = \_\_import\_\_('7-base\_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer\_validator("my\_int", 12)
bg.integer\_validator("width", 89)

try:
    bg.integer\_validator("name", "John")
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

try:
    bg.integer\_validator("age", 0)
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

try:
    bg.integer\_validator("distance", -4)
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

guillaume@ubuntu:~/$ ./7-main.py
\[TypeError\] name must be an integer
\[ValueError\] age must be greater than 0
\[ValueError\] distance must be greater than 0
guillaume@ubuntu:~/$
```


### 9.

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

*   Instantiation with `width` and `height`: `def __init__(self, width, height):`
    *   `width` and `height` must be private. No getter or setter
    *   `width` and `height` must be positive integers, validated by `integer_validator`
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

guillaume@ubuntu:~/$ ./8-main.py
<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
\['\_Rectangle\_\_height', '\_Rectangle\_\_width', '\_\_class\_\_', '\_\_delattr\_\_', '\_\_dict\_\_', '\_\_dir\_\_', '\_\_doc\_\_', '\_\_eq\_\_', '\_\_format\_\_', '\_\_ge\_\_', '\_\_getattribute\_\_', '\_\_gt\_\_', '\_\_hash\_\_', '\_\_init\_\_', '\_\_le\_\_', '\_\_lt\_\_', '\_\_module\_\_', '\_\_ne\_\_', '\_\_new\_\_', '\_\_reduce\_\_', '\_\_reduce\_ex\_\_', '\_\_repr\_\_', '\_\_setattr\_\_', '\_\_sizeof\_\_', '\_\_str\_\_', '\_\_subclasshook\_\_', '\_\_weakref\_\_', 'area', 'integer\_validator'\]
\[AttributeError\] 'Rectangle' object has no attribute 'width'
\[TypeError\] height must be an integer
guillaume@ubuntu:~/$
```
**No test cases needed**



### 10.

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

*   Instantiation with `width` and `height`: `def __init__(self, width, height):`:
    *   `width` and `height` must be private. No getter or setter
    *   `width` and `height` must be positive integers validated by `integer_validator`
*   the `area()` method must be implemented
*   `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`
```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
Rectangle = \_\_import\_\_('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

guillaume@ubuntu:~/$ ./9-main.py
\[Rectangle\] 3/5
15
guillaume@ubuntu:~/$
```
**No test cases needed**



### 11.

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

*   Instantiation with `size`: `def __init__(self, size):`:
    *   `size` must be private. No getter or setter
    *   `size` must be a positive integer, validated by `integer_validator`
*   the `area()` method must be implemented
```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
Square = \_\_import\_\_('10-square').Square

s = Square(13)

print(s)
print(s.area())

guillaume@ubuntu:~/$ ./10-main.py
\[Rectangle\] 13/13
169
guillaume@ubuntu:~/$
```
**No test cases needed**



### 12.

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

*   Instantiation with `size`: `def __init__(self, size):`:
    *   `size` must be private. No getter or setter
    *   `size` must be a positive integer, validated by `integer_validator`
*   the `area()` method must be implemented
*   `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
Square = \_\_import\_\_('11-square').Square

s = Square(13)

print(s)
print(s.area())

guillaume@ubuntu:~/$ ./11-main.py
\[Square\] 13/13
169
guillaume@ubuntu:~/$
```
**No test cases needed**
