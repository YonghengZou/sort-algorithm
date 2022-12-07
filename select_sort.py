from swap import swap

class Select:
    # def __init__(self) -> None:
    #     pass

    def sort(l: list, reverse: bool=False) -> list:
        
        l = l.copy()
        n = len(l)
        
        if reverse==False:
            for i in range(n-1):
                min_index = i
                for j in range(i, n):
                    if l[j]<l[min_index]:
                        min_index = j
                swap(l, min_index, i)
        else:
            for i in range(n-1):
                max_index = i
                for j in range(i, n):
                    if l[j]>l[max_index]:
                        max_index = j
                swap(l, max_index, i)           
        return l