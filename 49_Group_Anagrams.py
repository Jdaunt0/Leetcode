class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {} # key = list[e:1 a:1 t:1] : value = str(e.g eat, tea, ate)

        for str in strs:
            count = [0] * 26
            for letter in str:
                count[ord(letter) - ord("a")] += 1

            key = tuple(count)

            if key not in dict:
                dict[key] = [str]
            else:
                dict[key].append(str)
        
        return list(dict.values())

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))