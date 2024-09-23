import random
sum=0

for i in range(1,random.randint(1,1000)):
    sum += i

print(sum)


for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()