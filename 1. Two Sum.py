# 1. Two Sum

# Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target.

# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums.sort()    
    sum = nums[0]

    for num in range(0,target-1):
        if (nums[num] != nums[num+1]):
            sum = sum + nums[num+1]
    return sum
  
def main(): 
  nums= [1, 2, 3, 1, 1, 4, 5, 6] 
  target = len(nums) 
  print(twoSum(nums, target)) 
  
if __name__ == '__main__': 
    main() 