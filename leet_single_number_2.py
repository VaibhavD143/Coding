""""
Intution : 
First:
cnt : to decide wether ans is negative or positive
first : ith bit is 1 if ith bit in all numbers occured 3x+1 times.
sec : ith bit is 1 if ith bit from all numbers occured 3x+2 times
if ith bit happen to occure 3rd time we reset it to 0
at the end we have our number in one, as all other bits will hit 3x times except bits present in result number

Second:
Intution is same,just we are performing all operations altogether
one = ~two & (one^n) : for each bit, if bit is set in n and not in one and not in two then set it. set ith bit in one if ith bit is occuring 3x+1 th time
two = ~one & (two^n) : for each bit, if bit is not set in `one` after performing above operation(that implies it was 1->0, transition):
                                        1> if bit is set in n and not in two then its increament, set bit in two
                                        2> if bit is set in n and also in two, counter exhausted so unset bit in two
                                    if transition is from 0->1 then increament happened there and not requires here, so unset bit in two
if asked question is number repeats 2 times then we should return `two`
General solution : https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers

- Either we can create k-1(where each elements repeats k times) variables to keep count of bits,and reset  when it reaches k.
We return number as asked, i.e. single element repeats p times and others k time then there can be k-1 variables for counter.
To return, if  p = 3 then we return `third`.that is 3rd occurence of bit

- we can use binary representation as mentioned in above post


"""
class Solution:
    def singleNumber(self, nums) -> int:
#         cnt=0
#         first = 0
#         sec = 0
#         for n in nums:
#             if n<0:
#                 n=-n
#                 cnt+=1
#                 cnt%=3
#             for i in range(32):
#                 if n&(1<<i):
#                     if first&(1<<i):
#                         if sec&(1<<i):
#                             first ^=(1<<i)
#                             sec ^= (1<<i)
#                         else:
#                             sec|=(1<<i)
#                     else:
#                         first|=(1<<i)
#         return first if cnt == 0 else -first
        one = two = 0
        for n in nums:
            one = ~two & (one^n)
            two = ~one & (two^n)
        print(two)
    #k=4 and p = 3
    def threeTwo(self,nums):
        one = two = three = 0
        for n in nums:
            one = ~three & ~two & (one ^ n) #bit 0
            two = ~three & ~one & (two^n)   #bit 1
            three = ~one & ~two & (three^n) #bit 2
        print(three)
s = Solution()
s.threeTwo([2,2,2,2,-3,-3,-3,5,5,5,7,7,7,7,5])