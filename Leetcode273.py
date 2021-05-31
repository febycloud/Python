#!/usr/bin/env python3
class Solution:
	def numberToWords(self, num: int) -> str:
		#简历index以空格分开，此时to19[7]='Seven'
		to19 = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
		tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
		#递归函数
		def helper(num):
			#比20小直接用to19
			if num<20:
				return to19[num]
			#20-100，十位nums//10再减去2因为index从20开始，个位再递归
			if num<100:
				return tens[num//10-2]+' '+helper(num%10)
			#100-1000百位num//100用to19，十位个位再递归
			if num<1000:
				return to19[num//100]+' Hundred '+helper(num%100)
		#小于1000直接使用
		if num<1000:
			return helper(num)
		#大于1000则有123,456看作123Thousand456，分开part1,part2分别使用
		if num>=1000:
			part1=num//1000
			part2=num%1000
			return helper(part1)+' Thousand '+helper(part2)


