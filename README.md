#Find the largest or smallest element.maybe more elements.

#找到最大或者最小的n个元素。


##可以利用heapq模块中的nlargest()和nsmallest()函数。

###heapq.nlargest(n, iterable, key=None) 
Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.
###heapq.nsmallest(n, iterable, key=None) 
Return a list with the n smallest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.


##ps：当要找的元素数量相对较少的时候用该方法较好。当n=1时，用min（）和max（）更快。当n与集合本身差不多大时，更快的方法是用sorted（items）[:N]或[-N:]。