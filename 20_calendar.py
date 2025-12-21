# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

# print (calendar.TextCalendar(firstweekday=6).formatyear(2015))

(month,day,year )= input().split(" ")

print(calendar.day_name[calendar.weekday(int(year),int(month),int(day))].upper())