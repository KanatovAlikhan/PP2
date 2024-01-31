def has_33(nums):
    ans=False
    size=len(nums)
    for i in range(size):
        if nums[i]==3 and nums[i+1]==3:
            ans=True
            break
    print(ans)
has_33([1, 3, 3])