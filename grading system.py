print("enter marks obtained in 5 subjects:")
maths=int(input())
science=int(input())
english=int(input())
hindi=int(input())
sanskrit=int(input())
tot=maths+science+english+hindi+sanskrit
avg=tot/5
if avg>=91 and avg<=100:
    print("your grade is A1")
elif avg>=81 and avg<=91:
    print("your grade is A2")
elif avg>=71 and avg<=81:
    print("your grade is B1")
else :
    print("your grade is B2")
   
