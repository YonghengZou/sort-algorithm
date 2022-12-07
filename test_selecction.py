import random

def test(l):
    n = len(l)

    for i in range(0,n-1,1):
        min_index = i
        flag = 0 
        for j in range(i,n,1):
            if l[j]<l[min_index]:
                min_index = j
                flag = 1
        if flag==0:
            break
        
        swap(l,i, min_index)

def swap(l, p1, p2):
    temp = l[p1]
    l[p1] = l[p2]
    l[p2] = temp

x = random.sample(range(1,100),10)
print(x)
test(x)
print(x)