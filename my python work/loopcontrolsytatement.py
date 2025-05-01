

#.........programe that will find out prime no in bt two given values ......
lower=int(input("any integer value lower one ...."))
higher=int(input("any integer value lower one ...."))

for i in range(lower,higher+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
     print(i)            
