class Solution(object):
    def lengthOfLastWord(self, s):
        li=s.strip().split()
        if not li:
            return 0
        return len(li[-1])
