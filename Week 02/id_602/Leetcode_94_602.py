class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        func = self.inorderTraversal
        return func(root.left) + [root.val] + func(root.right) if root else []