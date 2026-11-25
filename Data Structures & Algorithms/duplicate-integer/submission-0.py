class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        hashSet=set(nums)
        if (len(hashSet)==len(nums)):
            return False
        return True