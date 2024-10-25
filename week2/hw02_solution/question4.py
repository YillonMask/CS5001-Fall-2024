import string

# recursive function
def is_palindrome_helper(s):
    # Base case: if the string is empty or has only one character, it's a palindrome
    if len(s) <= 1:
        return True

    # Compare the first and last characters, and call the function recursively on the middle substring
    if s[0] == s[-1]:
        return is_palindrome_helper(s[1:-1])
    else:
        return False


def is_palindrome():
    user_input = input("Please enter a string: ")

    # Convert to lowercase and remove all non-alphanumeric characters
    cleaned_string = (
        user_input.lower().replace(" ", "").translate(str.maketrans("", "", string.punctuation))
    )

    # Call the recursive helper function
    if is_palindrome_helper(cleaned_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


# Example usage
is_palindrome()
