class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        #For each stone s in S, we need to check if it is a jewel or not i.e. it is a part of J or not
        #Also, it is given that elements in J are distinct, otherwise it is wise to do set(J) before checking 
        #element presence to reduce the complexity 
        
        J = set(J) #Unnecessary since J is distinct for current problem, but good for general cases
        count = sum([s in J for s in S]) #For each s in S, we check if it is present in J also #Case sensitive
        return count #No. of stones that are also distinct jewel type 
