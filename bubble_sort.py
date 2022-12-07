from swap import swap

class Bubble:
    def sort(l, reverse=False):

        l = l.copy()
        n = len(l)

        if reverse==False:
            for i in range(n-1,1,-1):
                flag = 0
                for j in range(0,i):
                    if l[j]>l[j+1]:
                        swap(l,j,j+1)
                        flag = 1
                if flag==0:
                    break

        else:
            for i in range(n-1,1,-1):
                flag = 0
                for j in range(0,i):
                    if l[j]<l[j+1]:
                        swap(l,j,j+1)
                        flag = 1
                if flag==0:
                    break
        return l