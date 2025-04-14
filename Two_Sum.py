'''
Answer to the Two Sum leetcode question
It works by making a hashmap to store the values that we have already checked 
in the array

the answer will be x + y = target, so by changing the function to x - target = y 
we can find the answer by looping through the array and cecking
if (the current value - target) is in the hashmap.

if not, then current value in the array is added to the hashmap 
for the next itteration of the for loop.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i in range(0,len(nums)):
            diff = target - nums[i]
            if (diff) in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4],6))
print(solution.twoSum([3,3],6))