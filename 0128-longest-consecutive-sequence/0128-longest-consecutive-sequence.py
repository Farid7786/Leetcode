class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        s=0
        if len(nums)==0:
            return 0
        length=1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                length+=1
            elif nums[i+1]-nums[i]==0:
                continue
            else:
                if length>s:
                    s=length
                length=1
        if length >s:
            return length
        else:
            return s