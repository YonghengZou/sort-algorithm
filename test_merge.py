x = [1]
y = [2]

def merge(l1, l2):
    m = len(l1)
    n = len(l2)
    l3 = []
    i=0
    j=0
    while i<=m or j<=n:
        if i<m and j<n:
            if l1[i]<l2[j]:
                l3.append(l1[i])
                i += 1
            else:
                l3.append(l2[j])
                j += 1
        elif i==m:
            for j in range(j,n):
                l3.append(l2[j])
            return l3
        elif j==n:
            for i in range(i,m):
                l3.append(l1[i])
            return l3

print(merge(x,y))
    
