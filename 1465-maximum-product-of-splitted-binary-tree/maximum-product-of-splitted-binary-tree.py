class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        total = 0
        self.best = 0
        
        def sumTree(node):
            if not node:
                return 0
            s = node.val + sumTree(node.left) + sumTree(node.right)
            self.best = max(self.best, s * (total - s))
            return s
        
        def computeTotal(node):
            if not node:
                return 0
            return node.val + computeTotal(node.left) + computeTotal(node.right)
        
        total = computeTotal(root)
        sumTree(root)
        return self.best % MOD
