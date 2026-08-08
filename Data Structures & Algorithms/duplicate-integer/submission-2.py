class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt=defaultdict(int)
        for i in nums:
            dictt[i]+=1
        print(dictt)
        for i,key in dictt.items():
            if key>=2:
                return True
        return False