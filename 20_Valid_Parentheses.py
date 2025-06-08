class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        
        for c in s:
            if c in parentheses:
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False


#unit tests
import unittest
class test_ValidParentheses(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.isValid("()" ), True)

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.isValid("()[]{}"), True)

    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.isValid("(]"), False)

    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.isValid("([])"), True)
    
    def test_5(self):
        solution = Solution()
        self.assertEqual(solution.isValid("[(])"), False)
    
    
if __name__ == '__main__':
    unittest.main()