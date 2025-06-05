class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {} # key=num : value=count
        count = [[] for i in range(len(nums))]

        for num in nums:
            if num not in dict:
                dict[num] = 0
            else:
                dict[num] += 1
        
        for key, value in dict.items():
            count[value].append(key)

        result = []
        
        for x in range(len(count)-1,-1,-1):
            if count[x] !=[]:
                for y in range(len(count[x])):
                    result.append(count[x][y])

        return result[:k]
    
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1,1,2,2,3,3,3], 2))
print(solution.topKFrequent([1], 1))