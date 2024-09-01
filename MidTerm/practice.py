
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root.left is None or root.right is None:
            return root.val
        l = postorderTraversal(self, root.left)
        r = postorderTraversal(self, root.right)
        print(l,r)

def main():
    postorderTraversal()


if __name__ == "__main__":
    main()



