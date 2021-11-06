# list all prime number which smaller than the given target number in a list:

target=2

def is_prime(i):
    if i <=0:
        return False
    for x in range(2,i): 
        if i%x ==0: # eg, when i=4, if x=2, then 4%2=0, it means, 4 is not prime number.
            return False
    return True    

res=[]
for x in range(1,target):
    if is_prime(x):
        res.append(x)
print(res)

'''
The trick part is when calculate number 1 and 2. due to range(2,1) and range(2,2) will give no any number.
so, it will never return False.
'''

