class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        MaxConsecutiveOnes: int = 0
        CurrentMax: int = 0
        for index in range(len(nums)):
            if nums[index] == 1:
                CurrentMax += 1
                if CurrentMax > MaxConsecutiveOnes:
                    MaxConsecutiveOnes = CurrentMax
            else:
                if CurrentMax > MaxConsecutiveOnes:
                    MaxConsecutiveOnes = CurrentMax
                    CurrentMax = 0
                else:
                    CurrentMax = 0
        return MaxConsecutiveOnes
            

        