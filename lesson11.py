# форматирование строк
name = "John"
age = 24
# print("My name is " + name + ". I'm " + str(age) + " years old.")
# старый вариант с Python 2
# print("My name is %(name)s. I'm %(age)d years old." %{"name": name, "age": age})
# позиционный маркер
# print("My name is %s. I'm %d." %(name, age))
# print("Title: %s, Price: %.2f" %("Sony", 499.99))
# print("My name is {} and I'm {}.".format(name, age))
# print("My {1} name is {0} and I'm {0}.".format(name, age))
# print("My name is {x}. I'm {y}".format(x="John", y=age))

# 3.6 version f-strings
print(f"My name is {name} and I'm {age}.")
print(f"My name is {name} and I'm {age + 1}.")