#List comprehension is a term for facilities that python gives us in lists, follow the example below:

fruits = ["apple", "grape", "orange", "pineapple"]
#I want to make a list with the content of "fruits", but in upper case, so:

upper_list = []
for fruit in fruits:
    upper_list.append(fruit.upper())

print(upper_list)

#But that is not the way I want, with list comprehension, we can turn all that code above into this:

upper_list2 = [fruit.upper() for fruit in fruits]

print(upper_list2)

#As you can see, we have the same results, but just in one line... well, that's python, bitch!