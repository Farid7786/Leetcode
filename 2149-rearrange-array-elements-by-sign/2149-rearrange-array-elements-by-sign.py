class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in range(0,len(nums)):
            if nums[i]>=0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        i=0
        j=0
        while i<len(nums):
            nums[i]=pos[j]
            nums[i+1]=neg[j]
            i+=2
            j+=1
        return nums