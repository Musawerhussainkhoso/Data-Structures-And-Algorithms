#while loop
#1. Print numbers from 1 to 5
'''number = 1

while number <= 5:
    print(number)
    number += 1
   ''' 
def print_num(number):
    #base case
    if number>5:
        return
    #recursive
    print(number)
    print_num(number+1)
print_num(1)

print("--------------")
'''
number = 5

while number >= 1:
    print(number)
    number -= 1'''
    
def print_num(number):
    #base case
    if number < 1:
        return
    #recursive
    print(number)
    print_num(number-1)
print_num(5)

print("-----------------------------------------")

'''number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Sum:", total)'''

'''def print_num(number , total):
    if number>5:
        return
    print(number)
    print_num(total+number , number+1)
print(total)
'''
'''number = 5
counter = 1

while counter <= 10:
    print(number, "x", counter, "=", number * counter)
    counter += 1
   ''' 
def table(number , counter):
    if counter > 10:
        return
    print(number, "x", counter, "=", number * counter)
    table(number , counter+1)
table(5 , 1)
    
