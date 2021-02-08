class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sm = 0
        for i in nums:
            c = nums.count(i)
            if c == 1:
                sm += i
        return sm