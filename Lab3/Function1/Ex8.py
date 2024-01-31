def spy_game(nums):
    int1=2
    ans=False
    for i in nums:
        if i==0:
            int1-=1
        if i==7 and int1==0:
            ans=True
    print(ans)
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])