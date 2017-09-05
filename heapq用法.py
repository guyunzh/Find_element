import heapq
nums=[1,8,2,23,7,-4,18,23,42,37,2,-66]
print (heapq.nlargest(3,nums))  #print [42, 37, 23]
print (heapq.nsmallest(3,nums))   #print [-66, -4, 1]

#这两个函数都可以接受一个参数key，可以做更多的运算
print(heapq.nlargest(3,nums,key=abs))  #print [-66, 42, 37]
print(heapq.nsmallest(3,nums,key=abs))  #print  [1, 2, 2]

#还可以用sorted（）方法来进行全排序，然后切片选择需要的元素个数
print(sorted(nums,key=abs)[:3])   #print  [1, 2, 2]
print(sorted(nums,key=abs,reverse=True)[:3])   #print [-66, 42, 37]
#用print(sorted(nums)[-3：])也可以替代print(sorted(nums)[-3:])