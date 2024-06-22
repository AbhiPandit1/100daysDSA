class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def at_most_k(nums, k):
            count = 0
            left = 0
            result = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    k -= 1
                
                while k < 0:
                    if nums[left] % 2 != 0:
                        k += 1
                    left += 1
                
                result += right - left + 1
            
            return result
        
        return at_most_k(nums, k) - at_most_k(nums, k - 1)
