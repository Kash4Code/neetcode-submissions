class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        if len(nums) == 0 or len(nums) == 1:
            return False
        else:
            for num in nums:
                if num in my_set:
                    return True
                else:
                    my_set.add(num)
            return False