x,y = 12,42
print('x < y: x is {} and y is {}'.format(x, y))
print('x < y: x is {1} and y is {0}'.format(y, x))
print(f'x < y: x is {x} and y is {y}')
print('x < y: x is %d and y is %d' % (x, y))

print('*'*40)
print('x < y: x is {1:>10} and y is {0:<10}'.format(y, x))
print('x < y: x is {:>10} and y is {:<10}'.format(x, y))


print('*'*40)
print('x < y: x is (%10d) and y is (%-10d)' % (x, y))
print('x < y: x is ({1:>10}) and y is ({0:<10})'.format(y, x))
print('x < y: x is "{:>10}" and y is "{:<10}"'.format(x, y))
print(f'x < y: x is ({x:>10}) and y is ({y:<10})')
print('x < y: x is ({1:>10}) and y is ({0:<10})'.format(y,x))         

print('*'*40)
x = 100
print (f'x in hex is {x:x}')
print ('x in hex is {:x}'.format(x))
print (f'x in octal is {x:o}')
print (f'x in binary is {x:b}')
print (f'x in 3 digial floding dmoe is {x:3f}')

print('*'*40)
for i in range(1,11):
    print(i, end=' ')
print()

# Output:
# (base) [xzwei@ 16:34:53 Python_learning]$ /Users/xzwei/opt/anaconda3/bin/python /Users/Data/Python_learning/xzwei.py
# x < y: x is 12 and y is 42
# x < y: x is 12 and y is 42
# x < y: x is 12 and y is 42
# x < y: x is 12 and y is 42
# ****************************************
# x < y: x is         12 and y is 42        
# x < y: x is         12 and y is 42        
# ****************************************
# x < y: x is (        12) and y is (42        )
# x < y: x is (        12) and y is (42        )
# x < y: x is "        12" and y is "42        "
# x < y: x is (        12) and y is (42        )
# x < y: x is (        12) and y is (42        )
# ****************************************
# x in hex is 64
# x in hex is 64
# x in octal is 144
# x in binary is 1100100
# x in 3 digial floding dmoe is 100.000000
# ****************************************
# 1 2 3 4 5 6 7 8 9 10 

