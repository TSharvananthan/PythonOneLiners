def array123(nums): return True if [nums[n:n+3] == [1, 2, 3] for n in range(len(nums))].count(True) > 0 else False
