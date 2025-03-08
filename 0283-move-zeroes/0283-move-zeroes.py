class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            for i in range(nums.count(0)):
                nums.remove(0)
                nums.append(0)
            
        return nums

                