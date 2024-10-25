def place_objects_in_ar(objects, positions):
    # Check if the lengths of objects and positions lists match
    if len(objects) != len(positions):
        raise ValueError("Error: Number of objects and positions do not match.")

    successfully_placed = []

    # Iterate through objects and positions
    for obj, pos in zip(objects, positions):
        try:
            # Check if position is a valid 3D coordinate
            if len(pos) != 3:
                raise ValueError("Position must have exactly 3 coordinates")

            # Try to convert each coordinate to float
            x, y, z = map(float, pos)

            # If successful, add to the list of successfully placed objects
            successfully_placed.append((obj, (x, y, z)))

        except (ValueError, TypeError):
            print(f"Warning: Invalid position for object {obj} skipped.")

    return successfully_placed


# Test the function
if __name__ == "__main__":
    # Test case 1: All valid inputs
    objects1 = ["Chair", "Table", "Lamp"]
    positions1 = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
    print("Test case 1 result:")
    print(place_objects_in_ar(objects1, positions1))

    print("\n" + "-" * 50 + "\n")

    # Test case 2: Some invalid positions
    objects2 = ["Chair", "Table", "Lamp", "Bookshelf"]
    positions2 = [
        (1.0, 2.0, 3.0),
        (4.0, "5.0", 6.0),
        (7.0, 8.0),
        (10.0, 11.0, "twelve"),
    ]
    print("Test case 2 result:")
    print(place_objects_in_ar(objects2, positions2))

    print("\n" + "-" * 50 + "\n")

    # Test case 3: Mismatched list lengths
    objects3 = ["Chair", "Table"]
    positions3 = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
    print("Test case 3 result:")
    try:
        place_objects_in_ar(objects3, positions3)
    except ValueError as e:
        print(f"Caught expected error: {e}")
