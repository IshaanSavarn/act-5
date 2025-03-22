# program make a simple calculator

# this function adds two numbers
def add(x,y):
    return x+ y
# This function multiplies two numbers
def multiply(x,y):
    return x*y

# This function subtracts two numbers
def subtracts(x,y):
    return x-y
#This function  divides two numbers
def divide(x,y):
    return x / y
num1=int(input("Enter Number 1 :"))
num2=int(input("Enter number 2 : "))

print("Sum :",add (num1,num2))
print("Difference :", subtract(num1,num2))
print("product :",multiplay(num1,num2))
print("quotient:", divide(num1,num 2))