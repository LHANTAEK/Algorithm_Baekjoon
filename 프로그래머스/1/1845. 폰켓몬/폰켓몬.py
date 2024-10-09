def solution(nums):
    answer = 0
    nums_set_len = len(list(set(nums)))
    ponket_nums = len(nums) // 2
    
    if nums_set_len <= ponket_nums:
        answer = nums_set_len
        
    else:
        answer = ponket_nums
        
    return answer