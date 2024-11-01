# exercise1 
def isValid(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    for char in s:
        if char == '(':
            stack.append(')')
        elif char == '{':
            stack.append('}')
        elif char == '[':
            stack.append(']')
        else:
            if stack and stack.pop() != char:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False
# Alternative solution
def isValidAlt(s):
    n = len(s)
    if n % 2 == 1:
        return False
    stack = []
    mapping = {")" : "(", "]" : "[", "}" : "{"}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if top_element != mapping[char]:
                return False
        
        else:
            stack.append(char)
    return not stack
print(isValidAlt("(){}()"))

# Exercise 2
def climb_stairs(n):
    # Base cases
    if n < 0:
        return 0
    if n == 0:
        return 1
        
    # Recursive case: sum of ways from taking 1, 2, or 3 steps
    return climb_stairs(n-1) + climb_stairs(n-2) + climb_stairs(n-3)

# Test the function
print(climb_stairs(5))