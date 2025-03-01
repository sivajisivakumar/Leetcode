class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        char=""
        for i in range(len(digits)):
            tmp=str(digits[i])
            char+=tmp
        total=int(char)+1
        n2=str(total)
        new_list=[]
        for i in n2:
            new_list.append(int(i))
        return new_list