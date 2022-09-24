"""
Day 10
Today is Friday 23rd sept,2022
Topic: string methods
"""

"""1"""
# print('chandu reddy'.capitalize())  #Chandu

# text='chandu reddy'
# a=text.capitalize()
# print(a)

"""2"""
# print('sampath'.upper())      #SAMPATH

# text='sampath'
# a=text.upper()
# print(a)

"""3"""
# print('RAJ'.lower())          #raj

# text='RAJ'
# a=text.lower()
# print(a)

"""4"""
# print('Chandu is learning Python in Josh Innovations and it is located in Ameerpet'.count('is'))       #2

# text="I am chandu from Hyderabad and it is located in Telangana. Hyderabad is specially known for Biryani and Charminar."
# x=text.count('Hyderabad')
# print(x)                     #2

"""5"""
# print('Chandu is learning Python in Josh Innovations and it is located in Ameerpet'.casefold())         #chandu is learning python in josh innovations and it is located in ameerpet

# text='Chandu is learning Python in Josh Innovations and it is located in Ameerpet'
# a=text.casefold()
# print(a)

"""6"""
# print('Python'.center(20,'0'))            #0000000Python0000000

# text='Python'
# a=text.center(20,'0')
# print(a)

"""7"""
# print('hello world'.endswith('d'))                  #True

# text='hello world'
# a=text.endswith('d')
# print(a)

"""8"""
# print('C\th\ta\tn\td\tu'.expandtabs())      #C       h       a       n       d       u
# print('C\th\ta\tn\td\tu'.expandtabs(6))     #C     h     a     n     d     u
# print('C\th\ta\tn\td\tu'.expandtabs(3))     #C  h  a  n  d  u

# text='C\th\ta\tn\td\tu'
# a=text.expandtabs(6)
# print(a)

"""9"""
# print('Hello, Welcome to Python classes.'.find('to'))       #15
# print('Hello, Welcome to Python classes.'.find('welcome'))       #-1
# print('Hello, Welcome to Python classes.'.find('classes'))       #25

# text='Hello, Welcome to Python classes'
# a=text.find('to')
# print(a)

"""10"""
# print('hi, welcome to my world'.index('my'))        #15
# print('hi, welcome to my world'.index('hI'))        #ValueError: substring not found

# text='hi, welcome to my world'
# a=text.index('my')
# print(a)

"""11"""
# print('chandu1999'.isalnum())           #True
# print('chandu 1999'.isalnum())           #False

# text='chandu1999'
# a=text.isalnum()
# print(a)

"""12"""
# print('hameedsir'.isalpha())            #True
# print('hameed sir'.isalpha())           #False

# text='hameedsir'
# a=text.isalpha()
# print(a)

"""13"""
# print('abcdef_12A'.isidentifier())          #True

# text='abcdef_12'
# a=text.isidentifier()
# print(a)

"""14"""
# print('raj'.islower())              #True
# print('rajSam'.islower())              #False

# text='raj'
# a=text.islower()
# print(a)

"""15"""
# print('12345'.isnumeric())          #True

# text='12345'
# a=text.isnumeric()
# print(a)

