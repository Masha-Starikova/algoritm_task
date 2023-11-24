from typing import List

# Задача1: Two Sum

def to_sum(nums: List[int], target: int) -> List[int]:
    '''найти пару числе из списка nums которые в сумме будут равны target'''
    for i in range(len(nums)):
        j = i + 1
        print (nums[i])
        print (nums[j])
        if nums[i] < target:
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return print([i, j])
                else:
                    j += 1


# Test
to_sum(nums = [2,7,11,15], target = 9)
to_sum(nums = [3,2,4], target = 6)
to_sum(nums = [3,3], target = 6)

