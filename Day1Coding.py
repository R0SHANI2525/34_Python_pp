#que1:
firstname=input()
lastname=input()
print(lastname,"",firstname)


#que2:
import calendar
print(calendar.month(2026,1))

# que3:
from datetime import datetime
d1=datetime(2014, 7, 2)
d2=datetime(2014, 7, 11)
difference=d2-d1
print(difference)


#que4:check vowel or not
vowel=("a","e","i","o","u","A","E","I","O","U")
letter=input("enter letter")
if letter in vowel:
    print("vowel",letter)
else:
    print("no vowel")






