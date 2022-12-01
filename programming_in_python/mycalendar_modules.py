import sys

location = sys.path # assign the sys function to a variable
print(location) # all the possible locations the interpreter will look for when searching for modules, including the current working directory
for i in location:
    print(i)

import calendar

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
isitleap = calendar.isleap(2036)
print(isitleap)