class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num_dict = {}

        for num in nums:

            if num not in num_dict:
                num_dict[num] = 1

            else:
                num_dict[num] += 1

        for i in num_dict.keys():

            if num_dict[i] > n/2:
                return i
        
        return 0