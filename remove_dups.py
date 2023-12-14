# put BREAKPOINTS!!!
nums = [2, 7, 12, 22, 3, 3, 37, 40, 40, 77, 86, 144]



def removeDuplicates(nums):
    for idx in range(len(nums)-1, 0, -1):
        if nums[idx] == nums[idx-1]:
            temp = nums[idx] #3
            nums[idx] = nums[len(nums) -1] # 3= 144
            nums[len(nums) -1] = temp # 144 = 3
            nums.pop()
        nums.sort()
    
    print("count --->", nums)
    return len(nums)
        

removeDuplicates(nums)

