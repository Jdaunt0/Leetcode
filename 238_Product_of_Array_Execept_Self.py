class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        
        pre=1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        
        post=1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= post
            post *= nums[i]
            
        return output

import unittest
class test_ProductEceptSelf(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([1,2,3,4]), [24,12,8,6])

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([1,2,4,6]), [48,24,12,8])

    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([-1,0,1,2,3]), [0,-6,0,0,0])

    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])
    
    
if __name__ == '__main__':
    unittest.main()