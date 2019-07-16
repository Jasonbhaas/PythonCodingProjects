class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        current_sub_array = 0

        for num in nums:
            current_sub_array += num
            if current_sub_array > max_so_far:
                max_so_far = current_sub_array
            if current_sub_array < 0:
                current_sub_array = 0

        return max_so_far
