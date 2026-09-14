class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        once = []
        for i in nums:
            if i in once:
                return True
            once.append(i)               
        else: 
            return False
                
            
            



