#lex_auth_01269446319507046499

def remove_duplicates(value):
   c=''
   for i in range(0,len(value)):
      b=value[i]
      if b not in c:
         c=c+b
   return c

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
