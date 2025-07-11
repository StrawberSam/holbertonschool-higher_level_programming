## Resources

**Read or watch**:

*   [Writing JavaScript Code](/rltoken/fQUkQNjfE1Dw47vcgps6Ig "Writing JavaScript Code")
*   [Variables](/rltoken/FX6qEtLyELhXUg7u23eMDg "Variables")
*   [Data Types](/rltoken/R5-aJ7W7ypXbTAcI54Ut-g "Data Types")
*   [Operators](/rltoken/fQUkQNjfE1Dw47vcgps6Ig "Operators")
*   [Operator Precedence](/rltoken/4PdyDQJJuDXEZmbALqttug "Operator Precedence")
*   [Controlling Program Flow](/rltoken/N0Np7QFZVwSnRopkHsN4ow "Controlling Program Flow")
*   [Functions](/rltoken/21XrxDV4cjQfW8v7r2FNMw "Functions")
*   [Objects and Arrays](/rltoken/LSNtL9tP1DBU0bnBLdF2uA "Objects and Arrays")
*   [Intrinsic Objects](/rltoken/LSNtL9tP1DBU0bnBLdF2uA "Intrinsic Objects")
*   [Module patterns](/rltoken/OOAH-N9qs-oT4Y32ErUELQ "Module patterns")
*   [var, let and const](/rltoken/5dIWvs6Zn5XjcsP18Ti9Uw "var, let and const")
*   [JavaScript Tutorial](/rltoken/PzZBOx5Ms7RL0FX1fihHKw "JavaScript Tutorial")
*   [Modern JS](/rltoken/toueHB-cJAYoXNscJtr3Jw "Modern JS")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/7IvdhdUBt8B_PxSqLjfz9A "explain to anyone"), **without the help of Google**:

### General

*   Why JavaScript programming is amazing
*   How to run a JavaScript script
*   How to create variables and constants
*   What are differences between `var`, `const` and `let`
*   What are all the data types available in JavaScript
*   How to use the `if`, `if ... else` statements
*   How to use comments
*   How to affect values to variables
*   How to use `while` and `for` loops
*   How to use `break` and `continue` statements
*   What is a function and how do you use functions
*   What does a function that does not use any `return` statement return
*   Scope of variables
*   What are the arithmetic operators and how to use them
*   How to manipulate dictionary
*   How to import a file

## Requirements

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/node`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](/rltoken/Wz4slq1c0LivUbiR88Kj_Q "Rules of Standard") + [semicolons on top](/rltoken/n6FW86eM_laCRYFfuHKjXA "semicolons on top"). Also as reference: [AirBnB style](/rltoken/7O__u3p-BU24HUBUh7QXoQ "AirBnB style")
*   All your files must be executable
*   The length of your files will be tested using `wc`

## Tasks

### 1.

Write a script that prints “JavaScript is amazing”:

*   You must create a constant variable called `myVar` with the value “JavaScript is amazing”
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
```
guillaume@ubuntu:~/$ ./0-javascript\_is\_amazing.js
JavaScript is amazing
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ semistandard ./0-javascript\_is\_amazing.js
guillaume@ubuntu:~/$
```


### 2.

Write a script that prints 3 lines:

*   The first line: “C is fun”
*   The second line: “Python is cool”
*   The third line: “JavaScript is amazing”
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
```
guillaume@ubuntu:~/$ ./1-multi\_languages.js
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$
```


### 3.

Write a script that prints a message depending of the number of arguments passed:

*   If no arguments are passed to the script, print “No argument”
*   If only one argument is passed to the script, print “Argument found”
*   Otherwise, print “Arguments found”
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`

Reference: [process.argv](/rltoken/vCoaeNm6cQ46Ns3YLGBxAw "process.argv")
```
guillaume@ubuntu:~/$ ./2-arguments.js
No argument
guillaume@ubuntu:~/$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/$
```


### 4.

Write a script that prints the first argument passed to it:

*   If no arguments are passed to the script, print “No argument”
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
*   You are not allowed to use `length`
```
guillaume@ubuntu:~/$ ./3-value\_argument.js
No argument
guillaume@ubuntu:~/$ ./3-value\_argument.js School
School
guillaume@ubuntu:~/$
```


### 5.

Write a script that prints two arguments passed to it, in the following format: “ is ”

*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
```
guillaume@ubuntu:~/$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/$ ./4-concat.js c
c is undefined
guillaume@ubuntu:~/$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/$
```


### 6.

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

*   If the argument can’t be converted to an integer, print “Not a number”
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
*   You are not allowed to use `try/catch`
```
guillaume@ubuntu:~/$ ./5-to\_integer.js
Not a number
guillaume@ubuntu:~/$ ./5-to\_integer.js 89
My number: 89
guillaume@ubuntu:~/$ ./5-to\_integer.js "89"
My number: 89
guillaume@ubuntu:~/$ ./5-to\_integer.js 89.89
My number: 89
guillaume@ubuntu:~/$ ./5-to\_integer.js School
Not a number
guillaume@ubuntu:~/$
```


### 7.

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

*   The first line: “C is fun”
*   The second line: “Python is cool”
*   The third line: “JavaScript is amazing”
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
*   You are not allowed to use any `if/else` statement
*   You can use only one `console.log`
*   You must use a loop (`while`, `for`, etc.)
```
guillaume@ubuntu:~/$ ./6-multi\_languages\_loop.js
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$
```


### 8.

Write a script that prints `x` times “C is fun”

*   Where `x` is the first argument of the script
*   If the first argument can’t be converted to an integer, print “Missing number of occurrences”
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
*   You can use only two `console.log`
*   You must use a loop (`while`, `for`, etc.)
```
guillaume@ubuntu:~/$ ./7-multi\_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi\_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi\_c.js
Missing number of occurrences
guillaume@ubuntu:~/$ ./7-multi\_c.js -3
guillaume@ubuntu:~/$
```


### 9.

Write a script that prints a square

*   The first argument is the size of the square
*   If the first argument can’t be converted to an integer, print “Missing size”
*   You must use the character `X` to print the square
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
*   You must use a loop (`while`, `for`, etc.)
```
guillaume@ubuntu:~/$ ./8-square.js
Missing size
guillaume@ubuntu:~/$ ./8-square.js School
Missing size
guillaume@ubuntu:~/$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/$ ./8-square.js -3
guillaume@ubuntu:~/$
```


### 10.

Write a script that prints the addition of 2 integers

*   The first argument is the first integer
*   The second argument is the second integer
*   You have to define a function with this prototype: `function add(a, b)`
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
```
guillaume@ubuntu:~/$ ./9-add.js
NaN
guillaume@ubuntu:~/$ ./9-add.js 1
NaN
guillaume@ubuntu:~/$ ./9-add.js 1 7
8
guillaume@ubuntu:~/$ ./9-add.js 13 89
102
guillaume@ubuntu:~/$
```


### 11.

Write a script that computes and prints a factorial

*   The first argument is integer (argument can be cast as integer) used for computing the factorial
*   Factorial of `NaN` is `1`
*   You must do it recursively
*   You must use a function
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
```
guillaume@ubuntu:~/$ ./10-factorial.js
1
guillaume@ubuntu:~/$ ./10-factorial.js 3
6
guillaume@ubuntu:~/$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/$
```


### 12.

Write a script that searches the second biggest integer in the list of arguments.

*   You can assume all arguments can be converted to integer
*   If no argument passed, print `0`
*   If the number of arguments is 1, print `0`
*   You must use `console.log(...)` to print all output
*   You are not allowed to use `var`
```
guillaume@ubuntu:~/$ ./11-second\_biggest.js
0
guillaume@ubuntu:~/$ ./11-second\_biggest.js 1
0
guillaume@ubuntu:~/$ ./11-second\_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/$
```


### 13.

Update this script to replace the value `12` with `89`:

*   You are not allowed to use `var`
```
guillaume@ubuntu:~/$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/\*
YOUR CODE HERE
\*/
console.log(myObject);

guillaume@ubuntu:~/$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/$
```


### 14.

Write a function that returns the addition of 2 integers.

*   The function must be visible from outside
*   The name of the function must be `add`
*   You are not allowed to use `var`

[Tip](/rltoken/RJ9f5jTEwwzvgfbqijdiig "Tip")
```
guillaume@ubuntu:~/$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/$ ./13-main.js
8
guillaume@ubuntu:~/$
```
