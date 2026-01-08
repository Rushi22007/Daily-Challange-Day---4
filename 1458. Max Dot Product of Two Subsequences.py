class Solution:
    def maxDotProduct(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        dp = [[-10**9] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                product = nums1[i] * nums2[j]

                take_both = product
                if i > 0 and j > 0 and dp[i - 1][j - 1] > 0:
                    take_both += dp[i - 1][j - 1]

                skip_nums1 = dp[i - 1][j] if i > 0 else -10**9
                skip_nums2 = dp[i][j - 1] if j > 0 else -10**9

                dp[i][j] = max(take_both, skip_nums1, skip_nums2)

        return dp[n - 1][m - 1]
