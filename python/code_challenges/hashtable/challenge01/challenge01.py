# Write here the code challenge solution



class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None



class Tree:
    def  __init__(self):
        self.root=None
    def insert(self,value):
        if value == None:
            return

        node= Node(value)
        if self.root==None:
            self.root=node
            return self.root
        
        current=self.root
        while True:
            if current.value>node.value:
                if current.left==None:
                    current.left=node
                    return self.root
                current=current.left
            else:
                if current.right==None:
                    current.right=node
                    return self.root
                current=current.right
            
    def toArray_inorder(self,node,list = []):
        if (node == None):
            return list
        # check left
        if (node.left != None):
            self.toArray_inorder(node.left,list)
        list.append(node.value)
        if (node.right != None):
            self.toArray_inorder(node.right,list)
        return list

def findTarget(root : Node, k) -> bool:
    comps = {}
    flag = False
    def inOrder(node):
        if (node.left):
            inOrder(node.left)

        nonlocal comps
        nonlocal flag
        comp = abs(k-node.value)
        if (comps.get(comp) == None):
            comps[node.value] = 1
        else:
            flag = True
        
        if (node.right):
            inOrder(node.right)
    
    inOrder(root)
    return flag


bst = [7,2,9,1,5,None,14]

tree = Tree()
for val in bst:
    tree.insert(val)

print(findTarget(tree.root,3))



