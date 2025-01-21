from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
sol = Solution()
nums = [1, 2, 3, 4, 5, 1]  
result = sol.containsDuplicate(nums)
print(result)  

    