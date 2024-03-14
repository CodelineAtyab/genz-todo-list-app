def gen_pali(nums):
    for i in range(2, nums +2):
        pali = int('1' * (i - 2) + '1') ** 2
        print(pali)

nums = 5
gen_pali(nums)
