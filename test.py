year=int(input("year:"))

if year&4!=0:
    print(year," is not a leep year")
elif year%100==0:
      if year%400==0:
        print(year," is leep year")
      else:
         print( year, "is not a leep year") 
else:
    print(year," is leep year") 
