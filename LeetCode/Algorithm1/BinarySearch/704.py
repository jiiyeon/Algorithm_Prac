class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for item in nums:
            if item == target:
                return nums.index(target)
        return -1

