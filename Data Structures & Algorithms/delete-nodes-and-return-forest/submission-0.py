class Solution:
    res = set()
    to_delete_set = set()
    def helper(self, root, parent, dir):
        if len(Solution.to_delete_set) == 0:
            return 
        if root.val in Solution.to_delete_set:
            Solution.to_delete_set.remove(root.val)
            if root in Solution.res:
                Solution.res.remove(root)
            if parent is not None:
                if dir == "left":
                    parent.left = None
                elif dir == "right":
                    parent.right = None
            if root.left is not None:
                Solution.res.add(root.left)
                self.helper(root.left, root, "left")
            if root.right is not None:
                Solution.res.add(root.right)
                self.helper(root.right, root, "right")
        else:
            if root.left is not None:
                self.helper(root.left, root, "left")
            if root.right is not None:
                self.helper(root.right, root, "right")

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        Solution.res.clear()
        if root is None:
            return []
        Solution.to_delete_set.clear()
        Solution.to_delete_set = set(to_delete)
        Solution.res.add(root)
        self.helper(root, None, "")
        return list(Solution.res)
