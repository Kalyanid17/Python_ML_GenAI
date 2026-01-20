def Addtion( a, b):
    res =  a+b
    return res

def Substraction( a, b):
    res =  a-b
    return res

def Multiplication( a, b):
    res =  a*b
    return res

def Division( a, b):
    res =  a/b
    return res

print("Enter first no : ")
No1 = int(input())
print("Enter second no : ")
No2 = int(input())

print("Addition : ",Addtion(No1,No2))
print("Substraction : ",Substraction(No1,No2))
print("Multiplication : ",Multiplication(No1,No2))
print("Division : ",Division(No1,No2))