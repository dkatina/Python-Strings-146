
#String Formatting allows us to embed variables driectly into string

#f string

flavor = 'the Purple Bag'
food = 'Dorito'

statement = f"My favorite {food} flavor is {flavor}"
print(statement)


# .format()
city = 'Atlanta'
team = 'Braves'

info = 'The {} are from {}!'.format(team, city)
print(info)


#Advanced f strings, embedding full inline expressions

name = ''

#We can conditionally add a space before the name using concatentation.
greeting = f'Hello there{" " + name if name else ""}, how are you doing?'

print(greeting)
