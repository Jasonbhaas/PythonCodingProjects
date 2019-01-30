class Tree:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        if (left):
            left.parent = self
        self.right = right
        if (right):
            right.parent = self
        self.data = data

    def Add_Left_Child(self, left):
        self.left = left
        left.parent = self

    def Add_Right_Child(self, right):
        self.right = right
        right.parent = self

    def Is_Root(self):
        return (self.parent == None)

    def Is_Leaf(self):
        return not (self.left or self.right)


def Tree_Traversal(root):
    if root:
        print('Preorder : %d' % root.data)
        Tree_Traversal(root.left)
        print('InOrder : %d' % root.data)
        Tree_Traversal(root.right)
        print('PostOrder: %d' % root.data)


D = Tree(28)
L = Tree(0)
C = Tree(271, left=D, right=L)
H = Tree(17)
G = Tree(3, left=H)
