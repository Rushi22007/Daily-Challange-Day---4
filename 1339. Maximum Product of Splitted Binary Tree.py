class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.totalSum = 0
        self.maxProduct = 0

        def getTotalSum(node):
            if not node:
                return 0
            return node.val + getTotalSum(node.left) + getTotalSum(node.right)

        def getSubtreeSum(node):
            if not node:
                return 0

            left = getSubtreeSum(node.left)
            right = getSubtreeSum(node.right)

            subTreeSum = left + right + node.val
            product = subTreeSum * (self.totalSum - subTreeSum)

            self.maxProduct = max(self.maxProduct, product)

            return subTreeSum

        self.totalSum = getTotalSum(root)
        getSubtreeSum(root)

        return self.maxProduct % MOD
