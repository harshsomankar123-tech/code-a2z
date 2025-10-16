class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_current = 0
        # maxi = nums[0]
        # for i in nums:
        #     if max_current<0:
        #         max_current=0
        #     max_current+=i
        #     if max_current>maxi:
        #         maxi=max_current
        # return maxi
     curr_sum = nums[0]
     max_sums = nums[0]
     for x in nums[1:]:
        curr_sum = max(x, curr_sum +x)
        max_sums = max(max_sums,curr_sum)
     return max_sums  
