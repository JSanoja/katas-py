"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""
def valid_parentheses(paren_str):
    print(paren_str)
    if paren_str == "" : return True
    if paren_str == "(" or paren_str[0:1] != "(" : return False
    arr = list(paren_str)[1:]
    i=0
    for p in arr:        
        if p == ")" :
            del arr[i]
            break
        i+=1
    return valid_parentheses("".join(arr))
    

print(valid_parentheses("()(())((()))(())()"))
print(valid_parentheses(")(()(())((()))(())()"))
print(valid_parentheses("())(()"))