#Problem is the "First and Last Position of Element in Sorted Array"
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = False 
        length = len(nums)
        n = int(length/2)
        while not found: #Find starting index of 'target'
            if nums[n]>target:
                n = int(n/2)
            elif nums[n]<target:
                n = n + int(n/2)
            elif nums[n] == target:
                while(nums[n-1]==target):
                    n = n - 1
                found = True
            else: 
                return [-1,-1]
        solution = list()
        solution.append(n)
        found = False #Find ending index of 'target'
        while(not found):
            if nums[n+1] == target:
                n = n+1
            elif nums[n] == target:
                found = True
            else:
                print("Error finding ending index")
        solution.append(n)