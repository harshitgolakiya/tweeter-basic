a= [1,1,2,3,1,5,1,3,4,3,5,6,7,8,8,9,9,9,8,9,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,1]
k = 2
c= []
d= []
for i in range(len(a)):
    if a[i] not in c:
        e=0
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                e+=1
                if a[i] not in c:
                    c.append(a[i])
        if e!=0:
            d.append(e+1)


temp = None
for i in range(len(d)):
    for j in range(len(d)):
        if d[i] > d[j]:
            temp = d[i]
            d[i] = d[j]
            d[j] = temp
            temp = c[i]
            c[i] = c[j]
            c[j] = temp

for i in range(k):
    print(c[i])

# from collections import Counter
# import heapq

# a = [1, 1, 2, 3, 1, 5, 1, 3, 4, 3, 5, 6, 7, 8, 8, 9, 9, 9, 8, 9, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1]
# k = 2

# # Count the frequency of each element
# counter = Counter(a)

# # Find the k most common elements
# most_common = heapq.nlargest(k, counter.items(), key=lambda x: x[1])

# # Print the k most frequent elements
# for element, frequency in most_common:
#     print(element)
