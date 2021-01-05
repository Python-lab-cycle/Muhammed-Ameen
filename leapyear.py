#print leap year between two given years

print("print leap year between two given years")
print("enter start year:")
startYear=int(input())
print("enter last year:")
endYear=int(input())
print("List of leap years:")
#loop through between start and end year
for year in range(startYear,endYear):
#check if the yearis Leap year
     
 if((year%4==0)and(year%100!=0)or (year%400==0)):
    print(year)
