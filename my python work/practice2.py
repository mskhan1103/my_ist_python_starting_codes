# Write a program to replace an item with a different item if found in the list
L = [1,2,3,4,5,3]
# replace 3 with 300
for i in range(len(L)):
  if L[i]==3:
    L[i]=300

print(L)
L = [1, 2, 3, 4, 5, 3]

for index in range(len(L)):  # Iterate using index
    if L[index] == 3:
        L[index] = 300  # Modify the actual list

print(L)



L = [1, 2, 3, 4, 5, 3]

# Replace all occurrences of 3 with 300
L = [300 if i == 3 else i for i in L]  # Using list comprehension

print(L)


# Write a program to remove duplicate items from a list
L = [1, 8, 3, 4, 5]
ascending = True  # Assume the list is sorted
for i in range(len(L)-1):
    if L[i] > L[i + 1]:  # If any element is greater than the next one
        ascending = False
        break

if ascending:
    print("List is in ascending order")
else:
    print("List is not in ascending order")

