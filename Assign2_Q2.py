#What is difference between, Explain using id()
a = 10
b = 10

print("Integer a " + str(id(a)))
print(f"Integer b {id(b)}")

a = [10]
b = [10]

print("List a " + str(id(a)))
print("List b " + str(id(b)))

'''
    Integer a 4324320736
    Integer b 4324320736
    List a 4301951744
    List b 4302051392

    For Integer it allocates same memory location to same value. That means it created
    only 1 object in a memory and 2 identifiers as 'a' and 'b'. Whereas for List it created
    2 different memory locations sequentially for storing same value with2 different identifiers.
'''