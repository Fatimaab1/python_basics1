# Python Introduction
## Python Variables
### Github set up with HTTPS




- add image
- ![](path of the image)

- Add a block of code 

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

