class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        inc=0
        while True:
            power=2**inc
            if power==n:
                return True
            if power>n:
                return False
            inc+=1
        