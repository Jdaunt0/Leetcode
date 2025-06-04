#can be improved
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dictS, dictT = {}, {}
        
        for i in range(0, len(s)):
            if s[i] not in dictS:
                dictS[s[i]] = 0
            else:
                dictS[s[i]] += 1
            
            if t[i] not in dictT:
                dictT[t[i]] = 0
            else:
                dictT[t[i]] += 1

        return dictS == dictT


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
