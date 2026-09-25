class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        establish a counter at zero 
        establish what is a current at zero 
        take the max of each of those two for every iteration
        return the final max '''
        count = 0 
        maxi = 0 

        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maxi = max(count, maxi)
            else:
                count=0
                i+=1
        return maxi
        