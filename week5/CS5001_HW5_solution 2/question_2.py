"""
Write a python code to print the following pattern with loop.
"""
def print_patterns():
    # Pattern 1 (right-aligned)
    print("Pattern 1:")
    for i in range(5, 0, -1):
        print(" " * (5 - i) + "".join(str(j) for j in range(i, 0, -1)))
    for i in range(1, 6):
        print(" " * (5 - i) + "".join(str(j) for j in range(i, 0, -1)))
    print("\n")

    # Pattern 2 (centered)
    print("Pattern 2:")
    for i in range(4):
        print(" " * (4 - i) + "*" * (2 * i + 1))
    for i in range(2, -1, -1):
        print(" " * (4 - i) + "*" * (2 * i + 1))
    print("\n")

    # Pattern 3 (centered)
    print("Pattern 3:")
    for i in range(1, 6):
        line = "".join(str(j) for j in range(1, i + 1)) + "".join(str(j) for j in range(i - 1, 0, -1))
        print(" " * (5 - i) + line)

print_patterns()