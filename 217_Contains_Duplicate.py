class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {} # key: int : value: int

        for i in range(0, len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] = True
            else:
                hashmap[nums[i]] = False
        
        if True in hashmap.values():
            return True
        else:
            return False
        
solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3,4]))
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))