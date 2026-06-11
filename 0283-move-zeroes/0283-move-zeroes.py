class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        h=0
        while h<len(nums):
            if nums[h]!=0:
                nums[l],nums[h]=nums[h],nums[l]
                h+=1
                l+=1
            else:
                h+=1

        