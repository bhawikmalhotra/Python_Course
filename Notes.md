                                               python course

to run any python code or compiler in command prompt we need write command "python"

>>> import keyword
>>> print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

variable is a container that store some data or values for ex:- a = 35, 
while identifiers are the names of any variables, function or classes etc. for ex :- def shyam()

every variable is a identifier but not every identifier is a variable.
we should not use keyword or special symbols as a variable.
every identifier is case sensitive.
identifier name should be start with any name or underscore.
type keyword is used as a variable.

single valued data types:
1. numeric data types:                 2.boolean(bool)
   a. int
   b. float
   c. complex: it is a combination of real and imaginary(j) parts.

multi valued data types:
1. string (str)                       2. list
3. tuple                              4. set
5. dictionary

* in strings single qoute is used to define a single word or double qoute is used to define a sentence and triple quotes are used to define a paragraph in a string.
* string adding is called 'Concadination.


* List are the collection of homogenious or heterogenius data types which are ordered and mutable(changable) and allows duplicate values.
  list is defined by using square brackets[].

* Tuple are the collection of homogenious or heterogenius data types which are ordered and immutable(unchangable) and allows duplicate values.
   tuple is defined by using round brackets().

tuple is used in password or other sensitive data because it is immutable.

* set are the collection of homogenious or heterogenius data types which are unordered and mutable(changable) and does not allows duplicate values.
    set is defined by using curly brackets{}.

 * dictionary are the collection of key-value pairs which are unordered and mutable(changable) and does not allows duplicate keys.
    dictionary is defined by using curly brackets{} with key-value pairs.
    .keys can not be changed but values can be changed with the help of keys.

indexing : it is a way to access the elements of a data structure by their position or key.
   for example in a list, we can access elements by their index like list[0], list[1] etc.
   in a dictionary, we can access values by their keys like dict['key1'], dict['key2'] etc.

slicing : it is a way to extract a portion of a data structure by specifying a range of indices.
   for example in a list, we can slice elements like list[0:3] to get the first three elements.
   in a string, we can slice characters like string[1:5] to get characters from index 1 to 4.
   slicing syntax is [start:stop:step]
   print(type[2:5:1]) # it will print from index 2 to 4 with step 1

negative slicing : it is a way to access elements from the end of a data structure using negative indices.
   for example in a list, we can access elements like list[-1] to get the last element, list[-2] to get the second last element etc.
   in a string, we can access characters like string[-1] to get the last character, string[-2] to get the second last character etc.
   negative slicing syntax is [ -start : -stop : -step ]
   print(b[-1:-3:-1]) # it will print from last index to 3rd last index with step -1
   print(b[-3:]) # it will print from 3rd last index to first index
   print(b[:-3]) # it will print from first index to 3rd last index
   print(b[::-1]) # it will print the reverse of the string
   print(b[-5:-1]) # it will print from 5th last index to 2nd last index   

git commands:
1. git init : to initialize a git repository in the current directory.
2. git add . : to add all the files in the current directory to the staging area
3. git commit -m "message" : to commit the changes in the staging area with a message.
4. git status : to check the status of the repository.
5. git push origin main : to push the changes to the remote repository on the main branch.
6. git config --global user.name "your name" : to set the global username for git.
7. git config --global user.email "your email" : to set the global email for git.


OOps
# encalsulation
   it is done by 
         __methodname()
         or i can do with methdods of class like : __a or __func()

   pyhon Dont supporst full encapsulation 
      # i can still acces private members of class via : Dir(methodName)


# inheritense
    # single, multiple, mutlilevel, hirarchial
    # Super() - this is use to access the methods of parents class in base class 
        # this concept is known as 'MRO' - Method Resoltuion Order, which has technology (c3 linezation) which search methods in class , it just override the base to parent

# Polymorphism
   Means ability to take diff forms , same object diff form
   A single object behave differently

   * in python, with the help of polymorphysm we change behaviour of operators like +-*= 

   Dunder Methods [ like 10 + 20 = 30 - | pythin see (10).__add__(20) ]

   # Eg: 
   class Point:
      def __init__ (self,a,b):
         self.a = a
         self.b = b
   
      def __add__(self, other)
         return Point(self.a + self.other)

   test = Point(3,5)
   print(test)


# File Handeling
   - it refers to performing operation on the file - read, write, close
   - the key functions for working woth files in python is 
   [Open]
         file_obj = Open('filename', Mode, encoding)

   [with]
         with open("filename', mode, encoding) as fil