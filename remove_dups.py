nums = [2, 7, 12, 22, 3, 3, 37, 40, 40, 77, 86, 144]



def removeDuplicates(nums):
    sorted_nums = sorted(nums, reverse=False)
    print("sorted_list", sorted_nums)
    dup_list = []
    # prev_idx = curr_idx - 1
    curr_idx = 0
    next_idx = curr_idx + 1
    for num in sorted_nums:
        print("\n ----CURR IDX----> ", curr_idx)
        if num != sorted_nums[next_idx]:
            print("curr_idx  | next_dx  if", curr_idx, next_idx)
            print("curr-value -> ", num)
            print("next_value ->", sorted_nums[next_idx])
            
        if num == sorted_nums[next_idx]:
            print("### ### curr_idx dos | next_dx", curr_idx, next_idx)
            print("curr-value dos -> ", num)
            print("next_value ->", sorted_nums[next_idx])
            dup_list.append(sorted_nums[next_idx])
            print("done")
        curr_idx += 1
        # todo need to change logic here
        if num <= len(sorted_nums):
            next_idx += 1
    
        
    
    print("dup_list --->", dup_list)
    return sorted_nums
        

removeDuplicates(nums)