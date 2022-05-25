#Problem is the "First and Last Position of Element in Sorted Array"
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        found = False 
        length = len(nums)
        divisor = 1/2
        n = int(length/2)
        if length == 0:
            return [-1,-1]
        elif length == 1 and nums[0]==target:
            return [0,0]
        elif nums[-1] < target:
            return [-1,-1]
        elif nums[-1] == target:
            n = length-1
            
        while not found and n>0:   #Find starting index of 'target'
            #print(f'the value of n is {n}, and the value of nums[n] is {nums[n]}')
            if nums[n]>target:
                n = int(n/2)
            elif nums[n]<target:
                n = n + int(n*divisor)
            if nums[n] == target:
                while n-1 >=0 and nums[n-1]==target:
                    n = n-1
                found = True 
            divisor *= 1/2

        if not found:
            return [-1,-1]

        solution = list()
        solution.append(n)
        while n+1 < length and nums[n+1] == target:    #Find ending index of 'target'
            n = n+1
        solution.append(n)
        return solution