#python program to check if year is a leap year or not
year=2000
#to get year(integer input)from the user
#year=int(input("enter a year:"))
#divided by 100 means century year(ending with 00)
#century year divided by 400 is leap year
if(year %400==0)and (year %100==0):
  print("{0}is a leap year".format(year))
#not divided by 100 means not a century year
#year divided by 4 is a leap year
elif(year %4==0)and (year %100!=0):
  print("{0}is a leap year".format(year))
  #if not divided by both 400(century)and 4(not century year)
  #year is not leap year
else:
  print("{0} is not a leap year".format(year))