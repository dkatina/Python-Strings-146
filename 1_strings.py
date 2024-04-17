
#Strings are our datatype for storing text

#we define strings with ' ' and " "


#escape slash \ allows us to use ' or " in their respective strings without terminating
astring = 'this is a string with \' single \'quotes'
print(astring)
bstring = "this is a strig with double quotes"

#-- They are Immutable 
#--- This means you can't change the data that is stored in memory
#-- You can however still reassign

word = 'Hello'
print(word)
print(id(word))

word = word + ' World'
print(word)
print(id(word))

#Whenever we try to manipulate a string, we simply add the modifications and move them to a new slot in memory


#Indexing into strings

#The same as indexing into lists
#Indices are in numeric order starting from 0

name = 'Kevin'
second_letter = name[1]
print(second_letter)

#Slicing in strings
#Same as slicing list [start:stop] stop is non-inclusive, meaning the character at
#at the stop index will not be included in the slice

pie = 'apple pie'
apple = pie[:5]
print(apple)

pie = pie[6:]
print(pie)

#reverse slice

palindrome = 'tacos are cool'
reveresed = palindrome[::-1] 
print(reveresed)
