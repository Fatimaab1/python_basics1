## Python Installation

Visit the Python website linked below and find the latest version to download.

[Python download](https://www.python.org/downloads/)


Once on the website, select the gold download tab at the top of the page selcting the correct operating system you are using. 

## Installing on Mac 
**Step 1:** Once downloaded run the installer on your local machine by double clicking the package. 

**Step 2:** The installer will display a software wizard that will guide you on the different steps you need to follow to complete the installation

**Step 3** When the installation is finished, you'll be shown the Python folder. You can verify if Python and IDLE were installed correctly. To do that, double click on the IDLE file; if the installation is successful, you'll be shown the Python shell.


# Pycharm Installation

To download Pycharm follow the links below, selecting the correct operating system you are using.
Note: Download Community Edition

[Pycharm Mac download](https://www.jetbrains.com/pycharm/download/#section=mac)

[Pycharm windows download](https://www.jetbrains.com/pycharm/download/#section=windows)

[Pycharm Linux download](https://www.jetbrains.com/pycharm/download/#section=linux)


**Step 1:** Once downloaded, drag and drop the application into the Applications folder.

**Step 2:** Select Open when your trying to run the app for the first time.

**Step 3** Confirm the Privacy Policy once you have read the User Agreement and test if PyCharm works by running the program.


# Python introduction 

Python is a general purpose programming language often used in a range of applications including data science, software and web development and automation. 

### Python Variables
A variable is a container used to store data values. Example of a Python variable:
````
Number = '50'
Print(Number)
Output: 50
````

### Taking User input

Python provides a function called input which takes an input from the user to receive information and then stores it into a variable name.
````
User input example:

name = input()
print(name)

````
The above example asks for the users name, when the name is entered, it will then get printed to the screen.


````
# take user input with method called input()
print("please enter your name")
name = input()
print("welcome dear")
print(name)


````
- To add a line of code 
- commands `git add .`
- `git commit -m "logical msg"`
- `git push -u origin main`

### Data types & Operators
#### 2 types of operators
##### Arithmetic operators
`+ - * /`
- `+` adds two operands (var) together
- `-` subtract
- `*` multiply
- `/` divide

a = 4

b = 2

#### Comparison Operators
- `>` greater than
- `<` less than
- `==`equal
- `!=`does not equal to
- `>=`greater than or equal to
- `<=`less than or equal to

````
print(a > b) #True
print(b < a) #False
print(a == b) #False
print(a != b) #True
````
## Built in methods
````
# function methods builtin python
greeting = "Hello World!"

# In this statement what options are available in pythons built in library
print(greeting)
# if we wanted to check if the letters are in string
print(greeting.isalpha()) # true or false

# is it in lower case or upper case
print(greeting.islower()) # boolean
print(greeting.isdigit()) 
print(greeting.endswith("!")) 
print(greeting.startswith("H"))
````
#### Strings Concatenation Casting
- string indexing
- `Hello World!`
- index in python starts with 0
````
# print only world in a print statement using slicing
# print 4th letter from the left to right (use correct indexing for all statements)
# print 7th letter from right to left
# print 6th letter from left to right

word = "only world"
print(len(word))
print(word[:4])
print(word[:-7])
print(word[:6])
Output:
10
only
onl
only w
````


#### welcome user with their name and welcome message - name & message must start with capital
````
example_string = "james"
print(example_string)
print(len(example_string))
example_text = "there's some text with lot's of text"
print(example_text.count("text"))
````

#### find a method to bring the statement in capital/small letters then first letter capital
````
print(example_text.upper())
print(example_text.lower())
````

#### how to replace text within the string
print(example_text)

