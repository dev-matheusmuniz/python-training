first_name = input("Please, insert your first name: ")
last_name = input("Now, your last name: ")

print("Welcome, Mr(s) {} {}".format(first_name, last_name))
# if you want to order things differently, use the position between the keys, like this:
#   print("Welcome, Mr(s) {1} {0}".format(fist_name, last_name))
# That way, the output will be "Welcome, Mr(s) Muniz Matheus"

ammount_str = input("Input the ammount in your bank account today: ")
ammount = float(ammount_str)
day = 1
month = 9
year = 2021

print("Today, {:02}/{:02}/{:04}, you have $ {:.2f} in your bank account".format(day, month, year, ammount))

# To define a value as float in the interpolation, use the command :f between the keys, like the example above
# but in that example, the .2f was used to define that only 2 digits are allowed after the .
# For date, I've used the command :02 and :04 to format the date, which have 2 digits for d and m, and 4 digits for y
# when I define d as 1, m as 9, the output will set a zero before the number.