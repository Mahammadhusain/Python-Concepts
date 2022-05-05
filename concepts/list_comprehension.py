a=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# print([i for i in a]) # returns list of all elements of (a)

# print([i for i in a if i%2 == 0]) # returns list of all even elements of (a)
# print([i for i in a if i%2 != 0]) # returns list of all odd elements of (a)

# Multiple loop
nums1 = ['1', '2', '3']
nums2 = [4, 5, 6]
nums=[(x,y) for x in nums1 for y in nums2]
# print(nums)


# Matrix Convert in to List
matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatList=[num for row in matrix for num in row]
# print(flatList)


# Even-Odd with range 
even_nums = [x for x in range(21) if x%2 == 0]
# print(even_nums)
odd_nums = [x for x in range(21) if x%2 != 0]
# print(odd_nums)

# Two list convert in to dict using zip() (if list out of range then no error its continue with lower range of both list)
a= [1,2,3]
b=[4,5,6]
# print(dict(zip(a,b)))

# Two common range list convert in to dict using dictionary comprehension (if list out of range return list out of range error)
a= [1,2,3]
b=[4,5,6]
mydict = {a[i]:b[i] for i in range(len(a))}
# print(mydict)

# Count specific items from list
names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']
# nm=input('Enter name to count: ')
# count=names.count(nm)
# print('count = ', count)

# Count Each items from list -------- (1-way)
names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']
d={}
for i in range(len(names)-1):
    # print(range(len(names))) # because rannge(0,10) start from 0
    # print(range(len(names))-1) # because rannge(0,9) start from 0
    x=names[i]
    # print(x)  # Print all items
    c=0
    for j in range(i,len(names)):
        c=names.count(x)  # count for all names
        print(c)
    count=dict({x:c}) # make dictionary {names:counts}
    if x not in d.keys():
        d.update(count)
# print(d)

# Count Each items from list -------- (2-way)
names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']
nameset=set(names)
d={name:names.count(name) for name in nameset}
print(d)

# Count Each items from list -------- (3-way)
from collections import Counter
names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']
d=dict(Counter(names))
print(d)


