#Problem is the "First and Last Position of Element in Sorted Array"
import math
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = False 
        length = len(nums)
        n = int(length/2)
        while not found:
            if nums[n]>target:
                n = int(n/2)
            elif nums[n]<target:
                n = n + int(n/2)
            elif nums[n] == target:
                while(nums[n-1]==target):
                    n = n - 1
                found = True
                
        