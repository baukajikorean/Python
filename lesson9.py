# s = "C:\d\\new.txt"
# print(s)

# s = r'C:\d\new.txt'
# print(s)

# Concatenation of strings
# s = 'Py' 'thon'
# print(s)

# s1 = 'Hello, '
# s2 = "world!"
# s3 = s1 + s2
# print(s3)

# name = "John"
# age = 20

# print('My name is ' + name + ". I'm " + str(age) + " years old.")

# print("Hi " * 10)

# Index
# a = "Hello world!"
# print(a[0])
# print(a[-12])
# a[0] = "D"
# print(a)

# Срезы a[начало:конец:шаг]
a = "Hello world!"
print(a[0:12])       # Hello world!
print(a[0:12:2])     # Hlowrd
print(a[0:5])        # Hello
print(a[:5])         # Hello
print(a[6:12])       # world!
print(a[6:])         # world!
print(a[::2])        # Hlowrd
print(a[::-1])       # !dlrow olleH
print(a[:5] + a[6:]) # Helloworld!