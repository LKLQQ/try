# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 左子树的左孩子==右子树的右孩子 and 左子树的右孩子 == 右子树的左孩子

        '''
        递归,自定义函数
        '''
        if root is None:
            return True
        return self.check(root.left, root.right)

    def check(self, left: TreeNode, right: TreeNode):
        # 递归的终止条件是两个节点都为空
        # 或左右有任意一个不为空，一定不对称
        # 两个节点的值不相等
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)


def buildTree(lst):
    def grab(it, nextlevel):
        value = next(it, "N")
        if value != "N":
            node = TreeNode(value)
            nextlevel.append(node)
            return node

    # Create the root of the tree
    it = iter(lst)
    nextlevel = []
    root = grab(it, nextlevel)

    while nextlevel:
        level = nextlevel
        nextlevel = []
        for node in level:
            node.left = grab(it, nextlevel)
            node.right = grab(it, nextlevel)
    return root


root = eval(input().replace('null', 'None'))
root = buildTree(root)
s = Solution()
print(s.isSymmetric(root))

