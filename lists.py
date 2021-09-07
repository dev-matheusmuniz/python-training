#In python, we have different types of lists, here I will show some of them that are most used.

my_playlist = ["Eminem", "SOAD", "Thousand Foot Krutch", "Kant", "Hungria"]
#Above u can see the list type, which is muttable and we can add and remove values from it.

my_playlist.append("Kansas")
#.append() add a value to the last position in the list

print(my_playlist)

my_playlist.pop()
#.pop() is used to remove and return the last position in the list. For just removing, use .remove().

print(my_playlist)

#If you want to create an immutable list, you can create a tuple or turn a list into a tuple.

my_loved_playlist = tuple(my_playlist)
#Here I turned my_playlist into a touple, with the variable "my_loved_playlist"

print(my_loved_playlist)

#If you just want to create a tuple, create a var receiving values into ().
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
#Days of the week are immutable, so, I created it as a tuple.

#Set is another way to use lists in python, but with it we can create a list without duplicating any value. For it, use {}
cpf_usuarios = {38591794893}
#PS: set is not an ordered list of elements! If you search for an index in it, an error should appear.

#For adding value to a set, use .add.
cpf_usuarios.add(38591794893)

print (cpf_usuarios)