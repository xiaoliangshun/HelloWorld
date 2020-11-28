class Solution:
    def reversePairs(self, nums):
        def reversePairsRecursive(nums,l,r):
            if l == r:
                return 0
            else:
                mid = (l+r) // 2
                n1 = reversePairsRecursive(nums,l,mid)                #二分
                n2 = reversePairsRecursive(nums,mid+1,r)
                n = n1+n2

                i = l; j = mid+1                         #看左边有多少个比右边*2大的值
                while i <= mid:
                    while j <= r and nums[i] > nums[j]*2: j+=1
                    n += j - mid - 1
                    i += 1

                list1 = [0]*(r-l+1)                       #归并排序
                i = l; j = mid+1; p = 0
                while i<=mid or j<=r:
                    if i>mid:
                        list1[p] = nums[j]
                        p += 1; j += 1
                    elif j>r:
                        list1[p] = nums[i]
                        p += 1; i += 1
                    else:
                        if nums[i] < nums[j]:
                            list1[p] = nums[i]
                            i += 1; p += 1
                        else:
                            list1[p] = nums[j]
                            j += 1; p += 1

                    nums[l:r+1] = list1

                    return n

        leng = len(nums)
        if leng == 0:
            return 0
        return reversePairsRecursive(nums,0,leng-1)


nums =[1,3,2,3,1]
print(Solution().reversePairs(nums))
