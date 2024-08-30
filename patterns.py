alps = ['a','b','c','d','e']
a=len(alps)
print(a)
for  i in range (0,a+1):
    print()
    for j in range(i):
        print(f'{alps[j]} ',end="")


print('\n-------------------------------')
for i in range (1,10):
    print()
    for j in range(1,i+1):
        print(j ,end=' ')
