for i in range(5):
    print(i)
    
print ("-----------------\n")
for c in 'hello':
    print(c)

print ("-----------------\n")

for x in ('a','b',5,6,9):
    print (x)

print ("-----------------\n")

for i,j in [(1,2),(3,4),(5,6)]:
    print(i, j)

print ("-----------------\n")

for i in range (1,9):
    print (i)
    if i % 7 ==0:
        print ('multipleof 7 found ')
        break
else:
    print('no multiple of 7 found ')


