class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet=set(nums)
        maxLength=0
        for num in hashSet:
            if num-1 not in hashSet:
                current = num
                count=1
                while current + 1  in hashSet:
                    current+=1
                    count+=1
                maxLength= max(maxLength,count)
        return maxLength
                    

        