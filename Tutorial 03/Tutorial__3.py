#1.Use if by itself to test a condition and do one set of actions if it is true otherwise do nothing.
  #a) Test wih values: 99,100,101
n = int(input("Give me a number over 100: "))
if n<=100:
    print(n,'is not over 100')
    
  #b) A program to read in someone' age. Display 'can vote' if they are old enough.
age = int(input('Enter your age: '))
if age >= 18:
    print('Can Vote')

#2. Use an if-else to test a condition, do one set of actions if it is true
#otherwise do another set of actions.
  #a) Test with values: -1, 0, 1
x = int(input('Give me a number: '))
if x<0:
    print(x, 'is negative')
else:
    print (x, 'is positive')

  #b)a program to display “FAIL” if the mark entered is less than 40%
  #otherwise it should display “PASS”.
marks = int(input('Enter your marks: '))
if marks < 40:
    print('FAIL')
else:
    print('PASS')

  #c)a program to read in a centigrade temperature value.
  #and if the temperature is above 19 display ‘Hot’, otherwise display ‘Cold’.

centigrade = int(input('Enter the temperature in centigrade: '))
if centigrade > 19:
    print('Hot')
else:
    print('Cold')

  #d)a program that checks whether a number is even or odd and
  #then displays the appropriate message.
number = int(input('Enter a number: '))
if (number % 2 == 0):
    print('Number is even')
else:
    print('Number is odd')

#3. random module

import random
secret_number = random.randint(1,20)
print (secret_number)
secret_number = random.randint(1,4)
print (secret_number)

#Program that simulates a single flip of a coin.
#It should randomly print either ‘Heads’ or ‘Tails’

result = random.randint(0,1)
if result == 0:
    print('Heads')
else :
    print('Tails')

#4.
    #a)Ask the user to enter ‘1’ if they want to convert from Celsius to Fahrenheit or enter ‘2’ if they want to convert from Fahrenheit to Celsius.

choice = int(input('Enter 1 if you need to convert temperature from celsius to fahrenheit or enter 2 if you want to convert from fahrenheit to celsius: '))
if choice == 1:
    temp = int(input('Enter the celsius temperature: '))
    f = (9.0/5.0)*temp + 32
    print ('Converted fahrenheit value is:',f)
elif choice == 2:
    temp = int(input('Enter the fahrenheit temperature: '))
    c = (temp-32)*(5.0/9.0)
    print ('Converted celcius value is: ',c)
else:
    print('Invalid Option')

    #b) Calculator
integer_1 = int(input('Enter integer 1: '))
integer_2 = int(input('Enter integer 2: '))
operator = input('Enter your operator +,-,* or / : ')

if operator == '+':
    print(integer_1 + integer_2)
elif operator == '-':
    print(integer_1 - integer_2)
elif operator == '*':
    print(integer_1*integer_2)
elif operator == '/':
    if integer_2 == 0:
        print('Error')
    else:
        print(integer_1/integer_2)

    #c)Tip Calculator

cost = int(input('Please enter your meal cost: '))
dinnersatis = int(input(' 1 = Totally satisfied\n 2 = Satisfied\n 3 = Dissatisfied\nPlease rate our dinner: ' ))
if dinnersatis == 1:
    tip = cost*0.20
    print('You rated "Totally Satisfied", here is your tip: ', tip , 'Thank you')
elif dinnersatis == 2:
    tip = cost*0.15
    print('You rated "Satisfied", here is your tip: ', tip , 'Thank you')
elif dinnersatis == 3:
    tip = cost*0.10
    print('We are sorry, hope you enjoy our next meal!, here is your tip: ',tip,'Thank you')
else :
    print('You have entered a wrong number')

#5. and, or, not booleans
  #and
m = int(input('Give me number between 1 and 10: '))
if m >= 1 and m < 11:
    print('Well done! you gave me: ',m)
else:
    print('You entered a wrong number')

  #or
mark = int(input('Enter your mark: '))
if mark<0 or mark>100:
    print('Invalid mark')
elif mark >= 70:
    print('Exceptional result!')
elif mark >= 40:
    print ('Satisfactory result!')
else:
    print('You have failed')

  #not
x = 10
if not x>10:
    print("not returned True")
else:
    print("not returned False")

#6. Challenge Question.

response = input('Do you like Python? (Yes/No): ')
if response.lower() == 'yes' or response.lower() == 'y':
    print ('You are on the right course')
elif response.lower() == 'no' or response.lower() == 'n':
    print ('You might change your mind')
else:
    print ('I did not understand')




