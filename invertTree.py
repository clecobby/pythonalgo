class TreeNode:
    def __init__(self,val , left = None, right = None):
        self.left=left
        self.right= right
        self.val= val
        

class Solution:
    
    def revertTree(self, head: TreeNode)-> TreeNode:
        if not head :
            return None
        
        head.left,head.right = head.right,head.left
        self.revertTree(head.left)
        self.revertTree(head.right)
        
        return head


head =TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3))
solution = Solution()



solution.revertTree(head)



def printTree(root):
    if not root:
        return
    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)        


print("preorder traversal of inverted tree:")
printTree(head)