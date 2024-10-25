class FamilyTree:
    def __init__(self):
        # Family tree structure: each person is mapped to a dict of 'children' and 'parent'.
        self.tree = {}

    def add_person(self, name, parent=None):
        """ Add a new person to the family tree. """
        if name in self.tree:
            print(f"{name} is already in the family tree.")
            return

        # Add the person with an empty set of children and an optional parent
        self.tree[name] = {'children': set(), 'parent': parent}

        # If the person has a parent, add the person to the parent's set of children
        if parent:
            if parent not in self.tree:
                print(f"{parent} is not in the tree. Adding {parent} to the tree as well.")
                self.add_person(parent)  # Add the parent if they're not already in the tree
            self.tree[parent]['children'].add(name)
        print(f"{name} has been added to the family tree.")

    def remove_person(self, name):
        """ Remove a person and all their descendants from the family tree. """
        if name not in self.tree:
            print(f"{name} is not in the family tree.")
            return

        # Recursively remove all descendants
        descendants = self.get_all_descendants(name)
        for descendant in descendants:
            del self.tree[descendant]

        # Remove the person from their parent's children set
        parent = self.tree[name]['parent']
        if parent:
            self.tree[parent]['children'].discard(name)

        # Finally, remove the person
        del self.tree[name]
        print(f"{name} and all their descendants have been removed from the family tree.")

    def display_children(self, name):
        """ Display a person's direct children. """
        if name not in self.tree:
            print(f"{name} is not in the family tree.")
            return

        children = self.tree[name]['children']
        if children:
            print(f"{name}'s children: {', '.join(children)}")
        else:
            print(f"{name} has no children.")

    def get_all_descendants(self, name):
        """ Recursively find all descendants of a person. """
        if name not in self.tree:
            print(f"{name} is not in the family tree.")
            return set()

        descendants = set(self.tree[name]['children'])
        for child in self.tree[name]['children']:
            descendants.update(self.get_all_descendants(child))
        return descendants

    def display_descendants(self, name):
        """ Display all descendants of a person. """
        descendants = self.get_all_descendants(name)
        if descendants:
            print(f"All descendants of {name}: {', '.join(descendants)}")
        else:
            print(f"{name} has no descendants.")


# Example usage:
family_tree = FamilyTree()

# Adding people to the family tree
family_tree.add_person("Alice")
family_tree.add_person("Bob", "Alice")
family_tree.add_person("Charlie", "Bob")
family_tree.add_person("David", "Bob")
family_tree.add_person("Eve", "Charlie")

# Displaying direct children
family_tree.display_children("Bob")  # Bob's children: Charlie, David

# Displaying all descendants
family_tree.display_descendants("Alice")  # All descendants of Alice: Bob, Charlie, David, Eve

# Removing a person and all their descendants
family_tree.remove_person("Bob")  # This will remove Bob, Charlie, David, and Eve

# Try displaying descendants of Alice again after removal
family_tree.display_descendants("Alice")  # Alice has no descendants now