class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for i,j in freq.items():
            if j==1:
                return i
        