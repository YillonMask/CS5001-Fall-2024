def reverse(s):
    # Base case: if the string is empty or has one character, return it as is
    if len(s) <= 1:
        return s
    # Recursive case: reverse the substring excluding the first character and append the first character
    return reverse(s[1:]) + s[0]


# Example usage
input_string = "Hello, Alice! You are 21 years old."
reversed_string = reverse(input_string)
print(reversed_string)  # Output: dlo sraey 12 era uoY !ecilA ,olleH
