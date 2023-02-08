#lex_auth_0127135945621340161163

def string_both_ends(input_string):
	if(len(input_string)>2):
	   return input_string[:2]+input_string[-2:]
	elif(len(input_string)==2):
	   return input_string+input_string
	else:
	   return -1

input_string="w3w"
print(string_both_ends(input_string))