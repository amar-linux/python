
a=10
b=0

try:
    a/b
except ZeroDivisionError:
    print("division by zero")
finally:
    print('this will always execute')

a=0
b=2

while a < 4:
    print('-----------------')
    a+=1
    b-=1

    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - division by zero".format(a,b))
        break
    finally:
        print('{0}, {1}-- alaways executes'.format(a,b))

    print ("{0}, {1}--main loop".format(a,b))

    