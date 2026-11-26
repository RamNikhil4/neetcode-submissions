class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freqMap = {}
        for i in range(len(nums)):
            freqMap[nums[i]] = freqMap.get(nums[i], 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for key, val in freqMap.items():
            buckets[val].append(key)
        n = len(buckets) - 1
        while len(ans) < k:
            if len(buckets[n]) > 1:
                i = 0
                while i < len(buckets[n]) and len(ans) <k:
                    ans.append(buckets[n][i])
                    i +=1
            else :
                ans.extend(buckets[n])
            
            
            n -=1
        return ans
