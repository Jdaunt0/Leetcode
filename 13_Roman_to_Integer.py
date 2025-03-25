'''
Answer to the Roman numeral to integer leetcode question
It works by creating a hashmap to convert the roman numeral to its integar value
then, It loops through the roman numeral charater by character in reverse order

if the current character is greater than the next character, that means the arithmetic operation should be negitive
for instance IV = 4, going through this program: 5 > 1, therefore = 1-5 = 4

if the current character is less than or equal to the next character, that means the arithmetic operation should be positive 
for instance VI = 6 going through this program: 1 < 5, therefor = 1+5 = 6


example: VICXMCM = 1994
 _________________________________
| RomNum   | comparison |  ans    |
| V = 5    | 5          |  = 5    |
| I = 1    | 5 > 1      |  = 4    |
| C = 100  | 1 < 100    |  = 104  |
| X = 10   | 100 > 10   |  = 94   |
| M = 1000 | 10 < 1000  |  = 1094 |
| C = 100  | 1000 > 100 |  = 994  |
| M = 1000 | 100 < 1000 |  = 1994 |
|__________|____________|_________|

'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Hashmap to convert roman numerals to its integer value
        romanMap = {
            'I': 1, 
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = romanMap[s[len(s)-1]] # Initialise answer value, set to the last roman numeral digit

        for i in range(len(s)-1,0,-1): # Reverse order for loop

            if(romanMap[s[i]] > romanMap[s[i-1]]): # If the current roman numeral is less than or equal to the next roman numeral
                ans-= romanMap[s[i-1]] # add the next roman numeral to the answer
            else: # If the current roman numeral is greater than the next
                ans+= romanMap[s[i-1]] # subtract the next roman numarl from the answer

        return ans 
        


solution = Solution()

print("III = ", solution.romanToInt("III"))
print("LVIII = ", solution.romanToInt("LVIII"))
print("MCMXCIV = ", solution.romanToInt("MCMXCIV"))




















# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         romanMap = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
#         ans= romanMap[s[len(s)-1]]
#         for i in range(len(s)-1,0,-1):
#             # print("("+str(i-1)+ ")", s[i-1], "=", romanMap[s[i-1]],end=' || ')
#             if(romanMap[s[i]] < romanMap[s[i-1]]):
#                 # print(romanMap[s[i]], "<", romanMap[s[i-1]])
#                 ans+= romanMap[s[i-1]]
#             elif(romanMap[s[i]] > romanMap[s[i-1]]):
#                 # print(romanMap[s[i]], ">", romanMap[s[i-1]])
#                 ans-= romanMap[s[i-1]]
#             else:
#                 # print(romanMap[s[i]], "=", romanMap[s[i-1]])
#                 ans+= romanMap[s[i-1]]
#             print("i:", i,"ans =", ans)
            
            
                                                
#             # if(romanMap[s[i-1]] < romanMap[s[i]]):
#             #     print(" <",end=' ')
#             # elif(romanMap[s[i-1]] > romanMap[s[i]]):
#             #     print(" <",end=' ')
#             # else:
#             #     print(" =",end=' ')
#             # print("("+str(i)+ ")", s[i], "=", romanMap[s[i]],end='')
#             # print("")
#             # print(s[i-1], "=", romanMap[s[i-1]],end=' ')
#             # if(romanMap[s[i]] < romanMap[s[i+1]]):
#             #     print(" < ", end='')
#             # elif(romanMap[s[i]] > romanMap[s[i+1]]):
#             #     print(" > ", end='')
#             # else:
#             #     print(" = ", end='')
            
#             # if int_array[i - 1] >= int_array[i]:
#             #     ans += int_array[i]
                
            
#             #print("ans=", ans)
        
        
#         return ans
        


# solution = Solution()
# print("ans= ", solution.romanToInt("III"))
