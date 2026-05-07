class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0 for i in range(len(nums))]
        n=len(nums)
        
        prefix[0]=1
        i=1

        for j in range(1,n):
            prefix[j] = prefix[j-1]*nums[j-1]
            j+=1
        
        for k in range(n-2,-1,-1):
            prefix[k]=prefix[k]*i*nums[k+1]
            i= i*nums[k+1]
        return prefix

        
        