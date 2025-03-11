class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                nums[i-1]="_"
            k+=1
        while "_" in nums:
            nums.remove("_")
        return len(nums)