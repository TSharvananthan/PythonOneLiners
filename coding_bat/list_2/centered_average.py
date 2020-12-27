def centered_average(nums): return sorted(nums)[len(nums)//2] if len(nums) % 2 != 0 else (sorted(nums)[len(nums)//2] + sorted(nums)[len(nums)//2 - 1]) // 2
