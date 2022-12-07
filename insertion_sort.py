from swap import swap

class Insertion:
    def sort(l:list, reverse=False):
        l = l.copy()
        n=len(l)
        for i in range(1,n):
            # for j in range(i-1,-1,-1):
            #     if l[i]<l[j]:
            #         swap(l, j+1, j)
            j = i
            while j>=1 and l[j]<l[j-1]:
                swap(l, j, j-1)
                j -= 1
    
        return l


# if __name__ == "__main__":
#     for i in range(0,-1,-1):
#         print(i)