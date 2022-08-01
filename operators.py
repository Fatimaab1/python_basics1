#Comparison operators


#- `>` greater than
#- `<` less than
#- `==`equal
#- `!=`does not equal to
#- `>=`greater than or equal to
#- `<=`less than or equal to

#a = 4
#b = 2
#print(a > b) #True
#print(b < a) #False
#print(a == b) #False
#print(a != b) #True

#greeting = "Hello World!"

# In this statement what options are available in pythons built in library
#print(greeting)
# if we wanted to check if the letters are in string
#print(greeting.isalpha()) # true or false

# is it in lower case or upper case
#print(greeting.islower()) # boolean
#print(greeting.isdigit())
#print(greeting.endswith("!"))
#print(greeting.startswith("H"))

#greeting = "Hello World!"
#01234567891011
# -1 = last character in string (works backwards)
#print(len(greeting))
#print(greeting[-5])

# print only world in a print statement using slicing
# print 4th letter from the left to right (use correct indexing for all statements)
# print 7th letter from right to left
# print 6th letter from left to right

#example_string = "james"
#print(example_string)
#print(len(example_string))

# welcome user with their name and welcome message - name & message must start with capital
#example_text = "there's some text with lot's of text"
#print(example_text.count("text"))

# find a method to bring the statement in capital/small letters then first letter capital
#print(example_text.upper())
#print(example_text.lower())

# how to replace text within the string
#print(example_text)

# Concatenation & Casting

first_name = "James"
middle_name = "007"
last_name = "Bond"
age = 47
#print(first_name)
#print(middle_name)
#print(last_name)
#select ctr /
print(first_name + middle_name)
print(first_name, "" + middle_name, "" + last_name + "" + str(age))