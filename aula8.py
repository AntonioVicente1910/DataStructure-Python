# def sumList(nums):
#    sum = 0
#    for i in nums:
#        sum = sum + 1
#    return sum
#
nums = [1, 2, 4, 6, 8]

#sumList(nums) = nums[0] + sumList(nums[1])


def sumList(nums):
    if len(nums) == 1:
        return nums[0]

    else:
        return nums[0] + sumList(nums[1:])
    
print(sumList(nums))
