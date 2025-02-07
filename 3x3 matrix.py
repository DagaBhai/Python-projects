import random
def subgrid(n):
    total_number=[i for i in range(1,10)]
    subgridmatrix=[]
    for i in range(n):
        l=[""]*n
        for i in range(len(l)):
            random_pos=random.randrange(0,len(total_number))
            random_number=total_number.pop(random_pos)
            l[i]=random_number
        subgridmatrix.append(l)
    return subgridmatrix

n=3
print(subgrid(n))