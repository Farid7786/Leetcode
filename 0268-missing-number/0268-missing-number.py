class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            s+=nums[i]
        return ((len(nums)*(len(nums)+1))//2)-s