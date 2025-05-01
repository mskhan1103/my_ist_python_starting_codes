######..... Create a list of squares for numbers from 1 to 10, but only include even squares....############


################........... No : 1 List...............###############
li=[ i**2 for i in range(1,11)]
print(li)


# Create a list of numbers from 1 to 50 that are divisible by both 3 and 5.
li1=[i for i in range(1,51) if i%5==0 and i%3==0]
print(li1)


##############################.... No :2 through tuple ########################################

tup=tuple((i**2 for i in range(1,11)))
print(tup)

# Create a tuple containing the first 10 even numbers squared.
tup1=tuple(i**2 for i in range(1,31) if i%2==0)
print("tuple.......",tup1)

# no ............................############# : 3 set ############################################
se={x for x in range(1,11)}
print(se)

# Create a set containing the first 10 even numbers squared.

set1={i**2 for i in range(1,10) if i%2==0}
print("set that conatin no from 1,10 and their squares ",set1)

# set that contain values from 1,99 which have multiple of 9
set2={i for i in range(1,99) if i%9==0}
print("set that contain values from 1,99 which have multiple of 9",sorted(set2))


################################## no : 4 dictionary............................#############################

#write values from 1 to 10 in the form of dictionary 
dict={i:i for i in range(1,11)}
print("write values from 1 to 10 in the form of dictionary",dict)

# using if condition
# we have to pict up the stock whose value is greater than 0
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
dict0={key:value for (key,value) in products.items() if value>0}
print(dict0)



# we have to pict up the stock whose value is greater than 10
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
dict10={i:j for (i,j) in products.items() if j==10}
print("This for items whose values are equal to 10 ..........",dict10)




# we have to print a multiplication table from 2,5 in the form of nested comprehension.

dict={i:{j:j*i for j in range(1,11) } for i in range(2,5)}
print(dict)




