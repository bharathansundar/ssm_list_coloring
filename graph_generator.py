class TreeNode:
    def __init__(self, depth, colors, parent=None):
        self.depth = depth
        self.colors = colors
        self.children = []
        self.color = None
        self.parent = parent

    def add_children(self, depth, colors):
        if depth > 0:
            left_child = TreeNode(depth - 1, colors.copy(), parent=self)
            right_child = TreeNode(depth - 1, colors.copy(), parent=self)
            self.children.extend([left_child, right_child])
            left_child.add_children(depth - 1, colors)
            right_child.add_children(depth - 1, colors)

    def assign_color(self, color):
        if color not in self.colors:
            raise ValueError(f"Color {color} is not available for this node.")
        self.color = color
        self.colors.remove(color)
        if self.parent:
            if color in self.parent.colors:
                self.parent.colors.remove(color)
        for child in self.children:
            if color in child.colors:
                child.colors.remove(color)

    def remove_colored_subtrees(self):
        self.children = [child for child in self.children if child.color is None]
        for child in self.children:
            child.remove_colored_subtrees()

    def print_tree(self, level=0):
        print(' ' * (level * 4) + f'Node(depth={self.depth}, color={self.color}, colors={self.colors})')
        for child in self.children:
            child.print_tree(level + 1)

# Usage
# colors = ["red", "green", "blue", "yellow"]
# depth = 3
# root = TreeNode(depth, colors)
# root.add_children(depth, colors)
# root.print_tree()
# print("\nAssigning colors...\n")

# Example of assigning colors
# root.children[0].assign_color("green")
# root.children[1].children[1].assign_color("blue")

# root.print_tree()
# print("\nRemoving colored subtrees...\n")

# root.remove_colored_subtrees()
# root.print_tree()
