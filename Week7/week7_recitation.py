# P1
def ArrangeBooks(p):
    # Base cases
    if p == 0:
        return 1  # Only one way to arrange 0 books (empty shelf)
    if p == 1:
        return 3  # Three ways to arrange 1 book (standing, lying, leaning)
    
    # Recursive case
    # For each remaining book, we have 3 possibilities
    # Standing + arrange remaining (p-1) books
    # Lying flat + arrange remaining (p-1) books
    # Leaning + arrange remaining (p-1) books
    return (ArrangeBooks(p-1) + 
            ArrangeBooks(p-1) + 
            ArrangeBooks(p-1))

# Test cases
for i in range(5):
    print(f"Number of ways to arrange {i} books: {ArrangeBooks(i)}")

# Tail recursive solution for P1
def ArrangeBooksTail(p, accumulator=1):
    # Base cases
    if p == 0:
        return accumulator
    if p == 1:
        return accumulator * 3
    
    # Tail recursive case
    # Since each book has 3 possibilities, multiply accumulator by 3
    return ArrangeBooksTail(p - 1, accumulator * 3)

# Test cases
for i in range(5):
    print(f"Number of ways to arrange {i} books: {ArrangeBooksTail(i,1)}")


# P2
def FindPaths(r, c):
    # Base cases
    if r == 1 and c == 1:  # Reached bottom-right corner
        return 1
    if r == 1:  # Only one row left, can only move right
        return 1
    if c == 1:  # Only one column left, can only move down
        return 1
    
    # Recursive case
    # Sum of paths when moving right and moving down
    return FindPaths(r, c - 1) + FindPaths(r - 1, c)

# Test cases
def test_maze(rows, cols):
    print(f"Number of paths in a {rows}x{cols} maze: {FindPaths(rows, cols)}")

# Test with different maze sizes
test_maze(2, 2)  # Should return 2
test_maze(2, 3)  # Should return 3
test_maze(3, 3)  # Should return 6
test_maze(4, 4)  # Should return 20

# P3
def isValidHTML(html):
    stack = []
    i = 0
    while i < len(html):
        if html[i] == '<':
            # Found an opening bracket
            if i + 1 < len(html) and html[i + 1] == '>':
                # Found "<>"
                stack.append('<>')
                i += 2
            else:
                # Found "<"
                stack.append('<')
                i += 1
        elif html[i] == '>':
            # Found a closing bracket
            if not stack:  # Stack is empty
                return False
            if stack[-1] == '<':
                stack.pop()
                i += 1
            else:
                return False
        else:
            i += 1
    
    # Check if all tags were properly closed
    return len(stack) == 0

# Test cases
test_cases = [
    "<><>",     # Valid
    "<<>>",     # Valid
    "><",       # Invalid
    "<>>",      # Invalid
    "",         # Valid
    "<>",       # Valid
    "<<<>>>",   # Valid
    "><<>",     # Invalid
]

for test in test_cases:
    print(f'"{test}" is {"valid" if isValidHTML(test) else "invalid"}')