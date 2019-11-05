class Solution(object):
    def searchInsert(self, nums, target):
        count = 0
        for i in range(len(nums)):
            if nums[i] < target:
                count = count + 1
        return count
