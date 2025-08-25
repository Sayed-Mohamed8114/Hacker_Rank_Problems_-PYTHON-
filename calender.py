
import calendar
line=input().split()
day=int(line[0])
month=int(line[1])
year=int(line[2])

index_day=calendar.weekday(year,month,day)
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(days[index_day])
