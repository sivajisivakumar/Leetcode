class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            ele=nums[i]*nums[i]
            nums.pop(i)
            nums.insert(i,ele)
        nums.sort()
        return nums