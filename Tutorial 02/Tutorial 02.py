#1.Built-in Functions
#Check if the results are as expected.
total = 10
print(total)
print(type(total))

#joining total and greet.
greet = 'Hello'
both = str(total)+str(' ')+str(greet)
print(both)

#CHecking the outputs
a = "10"
b = "99"
c = a + b
print (c)
print (type(c))
c = int(c)
print(c)
print(type(c))

#Amending the above program so that it prints out the value 109

a = 10
b = 99
c = a + b
print(c)
print(type(c))

#2. Keyboard input
name = input('Please enter your name: \n')
print('Hello', name)

#Extending to ask age with response)
age = input('Please enter your age: \n')
print('Thank you for your response')

#3Printing
k= "test\test2\answers.txt"
print(repr(k))

#4. Difference print statements
the_text = input('Enter some text.\n')
#print version 01
print('This is what you entered: ')
print(the_text)
#print version 02
print('This is what you entered: ',the_text)
#print version 03
print('This is what you entered: ',end='')
print(the_text)

#5. testing end=''
print("A",end='')
print("B",end='')
print("C",end='')
print("D",end='\n')

#6. program to get and print the number of pets a user has.
number = input('Please enter the pets count of yours:\n')
print('Your pet count is:',number)

#7. the pseudocode to put zero into variable running_total.
#Then write separate instructions to add the following numbers onto what is in the variable, adding one number at a time 5, 8, 2, 3.
#Print running_total.
running_total = 0
running_total = running_total + 5
running_total = running_total + 8
running_total = running_total + 2
running_total = running_total + 3
print(running_total)

#8.Python program of following pseudocode.
#total <- 0
#INPUT num_1
#INPUT num_2
#total <- num_1 + num_2

total = 0
num_1 = input('num_1= ')
num_2 = input('num_2= ')
total = int(num_1) + int(num_2)
print(total)

#9.Python program using the pseudocode shown.
#INPUT cost_of_item
#INPUT cash_paid (e.g., 10 for £10)
#CALCULATE change

cost_of_item = input('cost= ')
cash_paid = input('cash paid= ')
Change = int(cash_paid) - int(cost_of_item)
print(Change)

#10.program that will convert a Centigrade temperature (c) entered as input into
#Fahrenheit (f) using the formula: f = (9/5)* c + 32
c = input('Enter a centigrade value = ')
f = (9.0/5.0)*int(c) + 32
print(f)

#11.program to calculate the volume of a box.
#Enter in the values for the three dimensions (length, height, width).
length = input('Enter length = ')
height = input('Enter height = ')
width = input('Enter width = ')
volume = int(length)*int(height)*int(width)
print('Volume of the box = ',volume)

#12.program that changes meters (m) to centimeters (c).
#The program should allow you to enter in the number of meters and then print out the number of centimeters.
meter = input('Enter the meter value= ')
centimeters = int(meter)*100
print(centimeters)






