#String built ins. reminder strings are immutable, so none of these are modifying
#the original string

#-- len() : returns the number of characters in a string, including whitespace and symbols

phrase = "What's it to ya???"
print(len(phrase))

#-- upper() : returns a full uppercase version of the entire string

phrase = 'Wow it is really nice out!'
yell_phrase = phrase.upper()

print(yell_phrase)

#-- lower() : return the full lowercase version of the entire string

phrase = 'Wow look at all these BOOKS!'
inside_voice = phrase.lower()


#-- title() : formats strings in a Title Case, capitalizing every word separated by a space

person = 'abraham lincoln'
print(person.title())

#-- replace(substring, replacer, how_many=all) : replace a sunstring of a string with a replacer

am = 'Good Morning Morning Morning'
pm = am.replace('Morning', 'Evening', 2)

print(pm)

#-- strip() : removes unwanted text from either side of a string, default to remove whitespace

class_146 = '             WOO THIS CLASS ROCKS              '
print(class_146)
print(class_146.strip())

#can tune to strip specific characters

gibberish = ' *&%$*&%$ Diamond in the rough (*%^*&%)*%)* '
print(gibberish.strip(' *@!#$%^&*()')) #continues to stip until it runs into a character that is not included in our garbage

#-- lstrip() : strips only from the left side

#--------works just like strip() just from the left onyl

#-- rstrip() : strips only from the right side

#--------works just like strip() just from the right only



#-- .find(sub) : returns the start index of the substring, if substring not present, returns -1

jungle = 'There is a TiGeR in my jungle'
tiger = jungle.lower().find('tiger') #can chain methods together to be read from left to right

lower_jungle = jungle.lower()
tiger = lower_jungle.find('tiger')
print(tiger)


#-- .count(sub) : counts the occurances of the substring in the main string

green = 'Green is my favorite color. I like green trees, green limes, GrEen cars, and green clothing, Green Eggs and Ham!'

print(green.lower().count('green')) #temporarily lower casing the string so that I can search for lower case green


#-- startswith(sub) : returns True or False depending on whether the string starts with sub or not

name = 'Jeffery'
print(name.lower().startswith('j'))

people = ['Alex', 'Aj', 'Brian', 'Clinton', 'Gerardo', 'Harsh']

al_team = []
for student in people:
    if student.lower().startswith('al'):
        al_team.append(student)

print(al_team)

#-- endswith(sub) : returns a True or False depending on whether the string ends with the sub or not

name = 'Travis'
print(name.endswith('s'))


#un-inviting the Freys from the wedding

guest_list = ['Rob Stark', 'Catlyn Stark', 'Jorah Mormont', 'Walder Frey', 'George Frey', 'Arthur Tully']

#un-invite 
new_list = []
for guest in guest_list:
    if not guest.endswith('Frey'):
        new_list.append(guest)

print(new_list)

#Three string checkers, all goo for checking user input()

#--- isalpha() : returns true if the string is made entirly of alphabetic character

letter = 'aasdf'
print(letter.isalpha())

#--- isdigit() : return true if the string is made entirly of  numeric characters

nums = '12345'
print(nums.isdigit())

# age = input('How old are you? ')

# if age.isdigit():
#     age = int(age)
#     print(f'On your birthday you will be {age + 1}')
# else:
#     print('Please enter only numbers')


#-- isspace() : returns true if string is comprised oh only whitespace

#if you're trying to manipulate casing

word = 'My Test Variable'
snake_case = ''
for letter in word.lower():
    if letter.isspace():
        snake_case += '_'
    else:
        snake_case += letter


print(snake_case)


#--- .split(sub) splits your string based on a specified substring, into a list of strings, default split on space

words = 'This-is-one-big string with many words'
words_list = words.split()

print(words_list)

flavors = input('Tell me all of your favorite flavors, (separate with space please): ').split()
print(flavors)


#--- Membership checks in strings, checking if a substring is in a string
# in

magic_word = 'blueberry'
scentence = 'Im having blueberry pancakes for dinner!'

if magic_word in scentence:
    print('WE GOT BLUEBERRY!')