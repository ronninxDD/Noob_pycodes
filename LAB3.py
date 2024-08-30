print('Enter any two numbers:')

a = int(input('n1='))
b = int(input('n1='))

#arithmetical operators
print(f'a={a}  b={b}')
print(f'{a}+{b}={a+b}')
print(f'{a}%{b}={a%b}')
print(f'{a}-{b}={a-b}')
print(f'{a}/{b}={a/b}')
print(f'{a}*{b}={a*b}')
print(f'{a}^{b}={a**b}')
print(f'{a}//{b}={a//b}')
print(f'{a if a<b else b}')
print('\n \n')
#comparison operators
if (a==b):
    print(f'{a} is equal to {b}')
else:
    print(f'{a} is not equal to {b}')
    if (a<b):
        print(f'{a} is less than to {b}')
    elif (a>b):
        print(f'{a} is greater than to {b}')

if (a<0) and (b<0):
    print('both a and b are negative')
elif (a<0) and (b>0):
    print('a is negative and b is positive')
elif (a>0) and (b>0):
    print('both numbers are positive')
elif (a>0 and b<0):
    print('a is positive and b is negative')
elif (a==0 or b==0):
    print('Either a or b is zero')
    if (a==0 and b==0):
        print('both a and b are zero')
    elif(a==0 and b!=0):
        print('a is zero b is not')
    else:
        print('a is not zero b is zero')
else:
    print('whatever')

if not(a==b):
    print('a is not equal to b')
else:
    print('a is equal to b')  

#logical operators
t =True
f = False

print(t and f)
print(t or f)
print(not t)

#bitwise operators
print(a & b)
print(a | b)
print(a^b)
print(~a)
print(a<<1)
print(b>>1)

#assignment operators
c=a+b;
print(c)
c+=5
print(c)
c-=3
print('c')
