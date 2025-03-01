class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s=""
        for i in s:
            if 97<=ord(i)<=122:
                new_s+=i
            if 65<=ord(i)<=90:
                t=i.lower()
                new_s+=t
            if i.isalnum(): 
                new_s += i.lower()
                
        if new_s==new_s[::-1]:
            return True
        else:
            return False
