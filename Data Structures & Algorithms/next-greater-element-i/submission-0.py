class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater_map[stack.pop()] = num
                
            stack.append(num)
        
        while stack:
            next_greater_map[stack.pop()] = -1

        return [next_greater_map[num] for num in nums1]