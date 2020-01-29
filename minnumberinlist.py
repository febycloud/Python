//数组中未出现的最小正数


num=[4,2,5]
nsort=sorted(num)	
print(nsort)
def mmin(nums):
	nsort=sorted(nums)
	for i in range(len(nsort)):
		if nsort[i]>i+1:
			return i+1
	return i	
a=mmin(num)
print(a)