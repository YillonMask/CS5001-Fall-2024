"""
1. Intensive Practice of For-Else
"""

"""
Check if a list is sorted: 
Write a program that checks if a list of numbers is sorted in ascending order. 
If any number is out of order, print ”List is not sorted” and stop the loop. 
If the loop completes without finding any issues, print ”List is sorted” using for-else.
"""
def check_sorted(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            print("List is not sorted")
            break
    else:
        print("List is sorted")


# Test the functions
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 4, 3, 5]
check_sorted(lst1)  # List is sorted
check_sorted(lst2)  # List is not sorted


"""
Check if a string contains only vowels: 
Write a program that checks if a string contains only vowels (a, e, i, o, u). 
If a non-vowel character is found, print ”Non-vowel character found” and stop. 
If the loop completes without finding a non-vowel, print ”All vowels” using for-else.
"""
def check_vowels(s):
    vowels = "aeiou"
    for char in s:
        if char.lower() not in vowels:
            print("Non-vowel character found")
            break
    else:
        print("All vowels")


# Test the functions
s1 = "aeiou"
s2 = "hello"
check_vowels(s1)  # All vowels
check_vowels(s2)  # Non-vowel character found


"""
Search for the longest word in a list: 
Write a program that searches for the longest word in a list of words. 
If all words have the same length, print ”All words are of equal length.” 
Otherwise, print the longest word using a for-else structure.
"""
def find_longest_word(words):
    longest_word = words[0]
    all_equal_length = True

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
            all_equal_length = False  # Found a longer word, so they are not all equal length
        elif len(word) != len(longest_word):
            all_equal_length = False  # Found a word of different length

    if all_equal_length:
        print("All words are of equal length.")
    else:
        print("The longest word is:", longest_word)

# For-else solution
def find_longest_word_alt(words):
    if not words:
        return "Empty list"
    longest_word = words[0]
    for word in words[1:]:
        if len(word) != len(longest_word):
            longest_word = max([longest_word, word], key=len)
            break
    else:
        print("All words are of equal length.")
        return
    print("The longest word is:", longest_word)

# Test the functions
words1 = ["apple", "banana", "cherry"]
words2 = ["apple", "peach", "grape"]
find_longest_word(words1)  # The longest word is: banana
find_longest_word(words2)  # All words are of equal length.


"""
Find the hidden treasure: 
Write a program that simulates a treasure hunt on a 2D grid. 
The grid is represented as a list of lists, with one of the grid cells marked as the treasure (’T’). 
The program should search the grid row by row. 
If the treasure is found, print ”Treasure found!” and stop. 
If the search completes and the treasure is not found, print ”Treasure not found, keep looking!” using for-else.
"""
def find_treasure(grid):
    for row in grid:
        if "T" in row:
            print("Treasure found!")
            break
    else:
        print("Treasure not found, keep looking!")


# Test the functions
grid1 = [
    ['.', '.', '.', '.'],
    ['.', 'T', '.', '.'],
    ['.', '.', '.', '.'],
]
grid2 = [
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
]
find_treasure(grid1)  # Treasure found!
find_treasure(grid2)  # Treasure not found, keep looking!


"""
Alien invasion detection: 
Write a program that simulates an alien defense system. 
The system scans the sky and checks for any UFOs in a list of sky objects. 
If a UFO (’UFO’) is detected, print ”Alien invasion detected, prepare defenses!” and break the loop. 
If no UFOs are detected after scanning all sky objects, print ”Sky is clear, no alien activity” using for-else.
"""
def detect_ufo(sky_objects):
    for obj in sky_objects:
        if obj == "UFO":
            print("Alien invasion detected, prepare defenses!")
            break
    else:
        print("Sky is clear, no alien activity")


# Test the functions
sky1 = ["star", "star", "UFO", "star"]
sky2 = ["star", "star", "star", "star"]
detect_ufo(sky1)  # Alien invasion detected, prepare defenses!
detect_ufo(sky2)  # Sky is clear, no alien activity
