def bracket_pattern(input_str):
    if input_str.startswith(")") or input_str.endswith("("):
        return False
    else:
        count1,count2=0,0
        for i in range(len(input_str)):
            if input_str[i]=="(":
                count1+=1
            elif input_str[i]==")":
                count2+=1
            else:
                break
        if count1==count2:
            return True
        else:
            return False
    
input_str="(())("
print(bracket_pattern(input_str))