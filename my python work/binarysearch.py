import math

lis = [33, 34, 65, 78, 78, 90, 98, 222, 223, 445, 665]
value = int(input("Enter value to be searched: "))

low = 0
high = len(lis) - 1
found = False

while low <= high:
    mid = (low + high) // 2  # Integer division
    if lis[mid] == value:
        print("Value found at index:", mid)
        found = True
        break
    elif lis[mid] < value:
        low = mid + 1  # Search in right half
    else:
        high = mid - 1  # Search in left half

if not found:
    print("Value not found in the list.")


# linear search implementation.
lis1=[33, 34, 65, 78, 78, 90, 98, 222, 223, 445, 665]
item=int(input("enter value to be searched ....."))
for i in lis1:
 if item==i:
     print("item is found at position ",i)
 else:
    print("item is not found ")