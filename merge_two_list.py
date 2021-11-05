'''
Give two lists with numbers, merget them to one and remove duplicated number.
'''
A=[1,3,3,5,7,9]  
B=[2,4,6,8,8,9,5,7,1]

def merget_remove_dup(L):
    D=[]
    for i in L:
        if i not in D:
            D.append(i)
    return D

print(merget_remove_dup(A+B))

