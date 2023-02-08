#lex_auth_0127136075580375041172

def check_22(num_list):
    new_str=" "
    for i in range(len(num_list)):
       new_str=new_str+str(num_list[i])
    
    if '22' in new_str:
       return True
    else:
       return False
        
print(check_22([3,2,5,1,2,1,2,2]))