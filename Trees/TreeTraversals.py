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
        #print('Preorder : %s' % root.data)
        Tree_Traversal(root.left)
        #print('InOrder : %s' % root.data)
        Tree_Traversal(root.right)
        print('PostOrder: %s' % root.data)


D = Tree(28)
E = Tree(0)
C = Tree(271, left=D, right=E)
H = Tree(17)
G = Tree(3, left=H)
F = Tree(561, right=G)
B = Tree(6, left=C, right=F)
M = Tree(641)
L = Tree(401, right=M)
N = Tree(257)
K = Tree(1, left=L, right=N)
J = Tree(2, right=K)
P = Tree(28)
O = Tree(271, right=P)
I = Tree(6, left=J, right=O)
A = Tree(341, left=B, right=I)

d = Tree('d')
e = Tree('e')
c = Tree('c', left=d, right=e)
h = Tree('h')
g = Tree('g', left=h)
f = Tree('f', right=g)
b = Tree('b', left=c, right=f)
m = Tree('m')
l = Tree('l', right=m)
n = Tree('n')
k = Tree('k', left=l, right=n)
j = Tree('j', right=k)
p = Tree('p')
o = Tree('o', right=p)
i = Tree('i', left=j, right=o)
a = Tree('a', left=b, right=i)

Tree_Traversal(a)
