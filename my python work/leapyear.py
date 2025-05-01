year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


ly=[i for i in range(1,2000) if  i%4==0 and i%100!=0 or i%400==0]
print(ly)