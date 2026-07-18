#Given a number N, print all numbers from 1 to N using recursion.
inp = int(input("Enter a number : "))
def print_num(num):
    if num > inp:
        return 
    print(num)
    print_num(num+1)
print_num(1)    

#reverse 
inp = int(input("Enter a number : "))
def print_num(num):
    if num < 1:
        return 
    print(num)
    print_num(num - 1)
print_num(inp)


