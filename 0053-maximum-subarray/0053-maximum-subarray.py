class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=float('-inf')
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum>l:
                l=sum
            if sum<0:
                sum=0
        print(i)
        print(len(nums))
        return l