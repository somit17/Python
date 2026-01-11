def kadane_algo(nums):

    cur_sum,max_sum=0,nums[0]
    for num in nums:
        cur_sum = max(cur_sum,0)
        cur_sum+=num
        max_sum += max(max_sum,cur_sum)

    return max_sum


#if we need to return pointers then -- >
#use sliding window variation -> Time complexity O(n)


def sliding_window(nums):
    max_sum=nums[0]
    cur_sum=0
    l,max_l,max_r= 0,0,0

    for r in range(len(nums)):
        if cur_sum < 0:
            cur_sum = 0
            l=r
        cur_sum+=nums[r]
        if max_sum > cur_sum:
            max_sum = cur_sum
            max_l,max_r = l,r

    return [max_l,max_r]
