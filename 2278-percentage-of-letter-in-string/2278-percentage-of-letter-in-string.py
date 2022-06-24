class Solution(object):
    def percentageLetter(self, s, letter):
        letter=s.count(letter)
        s= len(s)
        percentage= 100* (letter)/(s)
        return str(percentage)
        
        
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        