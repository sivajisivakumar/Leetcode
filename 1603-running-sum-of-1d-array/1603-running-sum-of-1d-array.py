class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        n=[]
        for i in range(len(nums)):

            sum=sum+nums[i]
            nums.pop(i)
            nums.insert(i,sum)
        
        return nums
        