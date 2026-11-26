class Solution:
    def freqList(self,s:str)->List[int]:
        freq=[0]*26
        for c in s :
            index=ord(c)-ord('a')
            freq[index]+=1
        return tuple(freq)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        resultMap={}
        for i in range(len(strs)):
            key=self.freqList(strs[i])
            if key not in resultMap:
                resultMap[key]=[]
            resultMap[key].append(strs[i])
        return list(resultMap.values())