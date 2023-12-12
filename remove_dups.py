# put BREAKPOINTS!!!
nums = [2, 7, 12, 22, 3, 3, 37, 40, 40, 77, 86, 144]



def removeDuplicates(nums):
    sorted_nums = sorted(nums, reverse=False)
    print("sorted_list", sorted_nums)
    dup_list = []
    curr_idx = 0
    next_idx = curr_idx + 1
    for idx in range(len(sorted_nums)-1):
        # print("\n ----CURR IDX----> ", curr_idx)
        if  sorted_nums[idx] != sorted_nums[next_idx]:
            pass
            # print("curr_idx  | next_dx  if", curr_idx, next_idx)
            # print("curr-value -> ", sorted_nums[idx])
            # print("next_value ->", sorted_nums[next_idx])
            
        if sorted_nums[idx] == sorted_nums[next_idx]:
            # print("### ### curr_idx dos | next_dx", curr_idx, next_idx)
            # print("curr-value dos -> ", sorted_nums[idx])
            # print("next_value ->", sorted_nums[next_idx])
            dup_list.append(sorted_nums[next_idx])
            # print("done")
        curr_idx += 1
        next_idx += 1
    
    print("dup_list --->", dup_list)
    return sorted_nums
        

removeDuplicates(nums)


# for x in range(len(nums)):
    # print("idx,", x)
    # print(nums[x])
    # print(len(nums))