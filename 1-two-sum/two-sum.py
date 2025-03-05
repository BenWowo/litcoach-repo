class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a mapping for (num, index)
        table = dict()
        for index, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], index]
            table[num] = index
            
        # This should never happen
        return [-1, -1]