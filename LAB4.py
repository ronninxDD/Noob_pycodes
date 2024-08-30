import sys

# a=int(input('Enter first Number:'))
# b=int(input('Enter second Number:'))
# c=int(input('Enter third Number:'))
# a,b,c=5,10,6
a=b=c=10
if (a>b) and (a>c):
    print(f'a={a } is greater')
elif(b>a) and (b>c):
    print(f'b={b} is greater')
else:
    print(f'c={c} is greater')


print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

