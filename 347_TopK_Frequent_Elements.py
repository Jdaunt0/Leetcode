class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {} # key=num : value=count
        count = [[] for i in range(len(nums)+1)]

        for num in nums:
            dict[num] = 1 + dict.get(num,0)
        
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