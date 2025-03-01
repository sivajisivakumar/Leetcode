class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==val:
                nums.append('_')
                nums.remove(nums[i])
                print(self.removeElement(nums,val))
            else:
                pass
        count=0
        for i in nums:
            if i!='_':
                count+=1
        return count
        