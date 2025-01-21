#target - pointer = check in hashmap
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i, n in enumerate(nums):
            val = target - n 
            if val in hashset:
                print([hashset[val],i])
                return [hashset[val],i]
            hashset[n]=i