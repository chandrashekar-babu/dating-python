# Getting Started with Python

One of the easiest ways to learn how Python works is to get a good understanding of the interactive python interpreter that comes bundled by default when you install Python. I’ll now demonstrate on the use of the default python interpreter that comes bundled with Python. So, to get started, just type ```python ``` at the shell prompt on all UNIX variants and clones (Linux). On Windows platform, you can run the idle GUI instead. 

The steps to the followed are as below:

1.  Select **IDLE (Python GUI)** from the **Python 3.3** Section in Windows Start->Programs menu.
![Selecting the **IDLE (Python GUI)**  in Windows Start->Programs->Python 3.3 menu](http://localhost:8000/Windows_Idle_Program.png)

2.  Now click on the **IDLE (Python GUI) ** and you will be greeted with the IDLE GUI window as below:

![The Windows Python IDLE GUI prompt](http://localhost:8000/Windows_Idle_Prompt.png)

On UNIX and Linux environments, you can install a more intuitive python interface by installing bpython - a better python interpreter. You can know more about it by visiting the official website - http://www.bpython-interpreter.org/

The advantage of using bpython over standard python interpreter are as below:

1. Syntax highlighting and intuitive autocompletion support on pressing the **tab** key.

2. Syntax and function help hints (featured most commonly on sophisticated IDE as show in the screenshot below).

![Context sensitive help provided by bpython](http://localhost:8000/BPython_Context_Help.png)


3. Support for saving statements and constructs typed in the interactive prompt into a log file, for further reference and for prototyping

![Official website of BPython Interpreter - http://www.bpython-interpreter.org/](http://localhost:8000/BPython_Website.png)

You can install bpython interpreter on your UNIX/Linux environment by using python setup-tools. Try the following command at the shell prompt as below:

	 ```$ sudo easy_install bpython```

![BPython installation using easy_install](http://localhost:8000/BPython_Installation_MacOSX.png)

After bpython is installed, try typing ```bpython ``` at the shell prompt. The following screenshot displays the interface:

![BPython interface on most UNIX/Linux environments](http://localhost:8000/BPython_Interface.png)

## Python statements and expressions
Once you’ve learnt to start the python interpreter of your choice (python, bpython IDLE), you can now learn how to write python programs by practicing at the interactive python ```>>> ``` prompt. 

Let us try out some simple expressions at the python ```>>> ``` prompt:

```python
>>> 3 + (4 * 5)
23
>>> print(“Hello world”)
Hello world
>>> max(10, 20, 44, 3, 15)
44
>>>
```

In the above example, the first expression is a simple arithmetic expression.
The second and third are function calls. The python interpreter prints the result of expressions immediately in the next line and prints the ```>>> ``` prompt again waiting for the next statement/expression.

> The above pattern is particularly known as the Read-Evaluate-Print-Loop or REPL for short. Most interactive interpreters are implemented using the REPL architectural pattern.

In Python, statements are broadly categorised as **simple** and **compound** statements. A simple statement ends with a newline, which means it is a single line statement.  The most commonly used simple statements are as below:

1. Assignment statement
Examples:
```python
>>> a = 10
>>> name = “John”
>>> big_number = max(10, 44, 22, 11, 45, 43, 21)
```

2. Expressions
```python
>>> 4 + (5*2)
14
>>> print(“Welcome to Python”)
Welcome to Python
```

3. Loading modules and accessing module members
```python
>>> import sys
>>> from os import getcwd
>>> from dircache import listdir as ls
```

4. Deleting variables
```python
>>> del a
>>> del name
```
## Python variables and objects
### Objects and Types/Classes
Python represents everything as an **object**. An **object** is an program’s abstraction of data that mimic objects in the real world. A program generally creates new objects, relates and interacts with them.  Python removes these objects from memory when the program no longer uses them. 

At the ```>>> ``` prompt, when you typed ```3 + (4 * 5)```, Python would’ve created five objects to represent this expression. To begin with, the numbers 3, 4 and 5 are represented as first three objects. Now, multiplying 4 and 5 results to value 20 which is  represented as the fourth object. Finally adding 3 with 20 results to 23 is the fifth object. This object representing value 23 is returned as the result of the expression and all other objects that were created by now is removed from memory by a technique known as Garbage Collection.
> Note: Unlike other mainstream programming languages like C++/Java, Python treats **everything** as an object. Numbers, Strings, boolean values are all treated as first-class objects.  

Python (since version 2.0) is a *pure object oriented programming language*. This implies some fundamental rules. They are as below:

### 1. All identifiers are variables.
Every name that you define is a variable. Unlike other languages, in Python, function name, module name, class name are also variables. This means,  all definitions in python essentially create a variable.
> Note: This basic rule makes python fully orthogonal and a pure object oriented programming language. 
 
### 2. All variables are references to objects.
Every variable is a reference to an object. Think of variables in python as 
similar to sticker labels/tags on products in a grocery store. The tags by themselves store nothing - but just a reference number. These reference numbers ultimately map to a particular object. Thus a variable acts more like a **label** to an object.
These labels provide an intuitive means to access an object. 
> Note: What you should know is that variables store nothing but reference (which can be merely a big number). This reference number is unique to every object created within the python program, thus it’s aptly called the object’s identity number of simply object-id.

For example, when you type ```a = 10 ``` at the python ```>>> ``` prompt for the first time, python creates a variable called ```a``` and also an object that represents the integer value ```10```. Every object has a unique identity (the object-id). This object id is what gets mapped into the variable ```a```. Thus, we would say that ```a``` refers to ```10```.

### 3. Everything in Python is an object. 
Yes, you read that right! Everything that can be referred to is an object in python. Numbers, strings, lists and all other forms of collections, functions, classes, modules, file handles, sockets, threads and processes  - are all first class objects. This means, all of them can be referred to by using variables and manipulated more easily using generic algorithms.

### 4. Objects are strongly typed. Variables are type-less.
In Python, unlike many mainstream languages, variables are type-less. This means, while defining variables we do not explicitly bind a variable to a particular data type. This is because of the nature that variables act as mere labels to objects in Python.
However, objects are strongly typed. For example, a numeric object cannot be treated as a string and likewise a string object cannot be treated as a number. This provides a balance between flexibility to the programmer while ensuring that he does not shoot his own foot.

### 5. Objects without references are garbage collected.
In Python, when you define a variable, you are actually creating a new reference to an object. Thus, every object in Python maintain a reference count - a number of references to themselves. When a variable is explicitly deleted or loses its scope, the object’s reference count  is decremented. If an object’s reference count becomes zero during the decrement, then the object is garbage collected. 

## Anatomy of a Python program
![Anatomy diagram of a python program](http://localhost:8000/Python_Program_Anatomy.png)


When a python program is parsed and loaded into primary memory by the python interpreter, it creates a stack frame for the ____main____ namespace and creates all global variables under this namespace. All global variable definitions in the program belong to the ____main____ namespace. 

All global variables that are defined under the ____main____ namespace refer to objects that are allocated in runtime on **heap**. 

Each object contain attributes that refer to other objects on heap.
A function object also has a stack frame that contain **local** variables that refer to objects again on heap.
 
## Python syntax and style guide - PEP8
