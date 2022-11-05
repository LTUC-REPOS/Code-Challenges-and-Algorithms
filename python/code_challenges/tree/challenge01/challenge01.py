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
            
    def toArray_Preorder(self,node,list = []):
        if (node == None):
            return list
        list.append(node.value) 
        if (node.left != None):
            self.toArray_Preorder(node.left,list)
        
        if (node.right != None):
            self.toArray_Preorder(node.right,list)
        return list

    def buildTree(self, preorder , inorder  ):
        
        """
        This funtion accepts, an inorder tree traversel and preorder 
        tree traversel and constructs a tree from both,

        """
        

        if not preorder or not inorder:
            return None

        if len(preorder) == 1:
            return Node(preorder[0])
        
        head = Node(preorder[0])
        root_index = inorder.index(preorder[0])
        
        head.left = self.buildTree(preorder[1:root_index + 1],inorder[:root_index])
        head.right = self.buildTree(preorder[root_index + 1:],inorder[root_index + 1:])
        
        return head


# tree = Tree()

# preorder = [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7]
# inorder = [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]

# head = tree.buildTree(preorder,inorder)

# print(tree.toArray_Preorder( head))

