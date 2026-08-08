class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt=defaultdict(list)
        for i in range(len(strs)):
            string=sorted(strs[i])
            val="".join(string)
            dictt[val].append(strs[i])

        res=[]
        for key,val in dictt.items():
            res.append(val)
        return res