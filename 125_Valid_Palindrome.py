class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alnum = ""
        for c in s:
            if c.isalnum():
                alnum += c.lower()

        return alnum == alnum[::-1]

import unittest
class test_ProductEceptSelf(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome("A man, a plan, a canal: Panama"), True) #amanaplanacanalpanama

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome("race a car"), False)

    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(" "), True)

    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome("Was it a car or a cat I saw?"), True)
    
    def test_5(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome("tab a cat"), False)
    
    
if __name__ == '__main__':
    unittest.main()