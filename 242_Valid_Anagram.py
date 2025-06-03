class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dict = {}
        
        for i in range(0, len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] +=1
        
        for i in range(0, len(t)):
            if t[i] not in dict:
                return False
            
            if dict[t[i]] == 0:
                return False
            
            if dict[t[i]] > 0:
                dict[t[i]] -= 1

        return True


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
