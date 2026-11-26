class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0
        ans = [0] * len(nums)
        for x in nums:
            if x == 0:
                zeroes += 1
                continue
            if zeroes > 1:
                product = 0
            else:
                product *= x

        for i in range(len(nums)):
            if zeroes > 1:
                return ans
            if nums[i] == 0 and zeroes == 1:
                ans = [0] * len(nums)
                ans[i] = product
                return ans

            else:
                ans[i] = product // nums[i]
        return ans
