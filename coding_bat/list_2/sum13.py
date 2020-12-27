def sum13(nums):
    total = 0
    i = 0
    while i <= len(nums):
        if nums[i] == 13:
            i += 1
            continue

        total += nums[i]
        i += 1

    return i

x = [1, 2, 2, 1]
y = [1, 1]
z = [1, 2, 2, 1, 13]

print(sum13(x))
print(sum13(y))
print(sum13(z))
