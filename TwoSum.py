class BST:
    def node(self, value = None):
        self.val = value
        self.index = None
        self.left = None
        self.right = None

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
        
    def findValue(self, value):
        if value < self.value:
            return self.left.findValue(value)
        elif value > self.value:
            return self.right.findValue(value)
        elif value == self.value:
            return self.index

class Solution(object):    
    def twoSum(self, nums, target):
        root = BST.node(self)
        for i in nums:
            root.insert(nums[i])
        