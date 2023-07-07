q1>class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum1=0
        for i in range(0,len(nums),2):
            sum1=sum1+nums[i]
        return sum1

q2>class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        set1=set()
        n=len(candyType)
        for i in range(len(candyType)):
            set1.add(candyType[i])
        m=len(set1)
        return int(min(n/2,m))

q3>class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total=0
        for i in range(len(flowerbed)-1):
            if(flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
        return n<=0