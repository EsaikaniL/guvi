//esai
my_tr1 = input()
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("yes")
else:
   print("no")
