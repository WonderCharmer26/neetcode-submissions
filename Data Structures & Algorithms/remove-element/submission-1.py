class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numsToLookAt = len(nums) - 1
        k = len(nums)
        for index in range(len(nums)):
            while nums[index] == val: 
                nums[index] = nums[numsToLookAt]
                nums[numsToLookAt] = 101
                numsToLookAt -= 1
                k -=1
        return k