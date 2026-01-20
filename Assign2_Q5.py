
a=10
b=10
print(id(a)==id(b)) #True 

a="Kalyani"
b="Kalyani"
print(id(a)==id(b)) #True 

a="Kalyani"
b="kalyani"
print(id(a)==id(b)) #False since k is small

#Same value of same datatype gets stored at same memory location resulting same memory address
