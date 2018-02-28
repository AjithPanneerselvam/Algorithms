"""
To check whether the given expression has their paranthesis({}, [], ()) balanced using stack data structure
"""
import stack


def paranthesis(expression):

    size = len(expression)
    open_braces = ['(','[','{']
    close_braces = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    s = stack.Stack(size)

    for char in expression:
        if char in open_braces:
            s.push(char)
        elif char in close_braces:
            if close_braces[char] == s.pop():
                continue
            else:
                return False

    if s.ssize() == 0:
        return True
    else:
        return False


# ### Testcases ###
# print paranthesis("(((expression)))")
# print paranthesis("([])")
# print paranthesis("([)")
