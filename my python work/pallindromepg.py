# we have to check that the given entered string is pallendrome or not.
s=input("Enter your string for checking if it is pallendrome or not....") #...malayalam
flag=True
for i in range(0,len(s)//2):
    if s[i] != s[len(s)-i-1]:
        flag=False
        print("Not pallendrome...............")
        break

if flag==True:
    print("palendrome")


#programe to find no of words in a string without using split() function
c=input("Enter your string for counting its words....") 
L=[]
temp=" "
for i in c:
    if i != " ":
        temp=temp+i
    else:
        L.append(temp)
        temp=" "
L.append(temp)
print(L)




