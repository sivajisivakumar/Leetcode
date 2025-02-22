class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        low=-2**31
        high=2**31
        rev_int=''
        if x<0:
            x=str(x)
            for i in range(len(x)-1,0,-1):
                rev_int+=x[i]
            if low<int(rev_int)<high:
                return int('-'+rev_int)
            else:
                return int(0)
    
        if x>0:
            x=str(x)
            for i in range(len(x)-1,-1,-1):
                rev_int+=x[i]
            if low<int(rev_int)<high:
                return int(rev_int)
            else:
                return int(0)

        else:
            return 0

