"""
    Complete the solution so that the function will break up camel casing, 
    using a space between words.
"""
import re
def solution(s):
    return "".join([re.sub("[A-Z]", f" {letter}", letter) for letter in s])

print(solution("breakCamelCase"))