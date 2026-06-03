class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        freq={}
        result=[]
        for i in range(0,len(nums)):
            freq[nums[i]]=0
        def backtracking(nums,ans,freq):
            if len(ans)==len(nums):
                result.append(ans.copy())
                return 
            for i in range(len(nums)):
                if freq[nums[i]]==0:
                    ans.append(nums[i])
                    freq[nums[i]]=1
                    backtracking(nums,ans,freq)
                    last=ans.pop()
                    freq[last]=0
        backtracking(nums,ans,freq)
        return result
