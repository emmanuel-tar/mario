from datetime import datetime,timedelta
#current date for today
current_date = datetime.now()

#yesterday date and time

one_day = timedelta(days=1)
yesterday = current_date - one_day



#Date portion display

print('Day: ' +str(current_date.day))
print('Month: ' +str(current_date.month))
print('Year: ' +str(current_date.year))

#Date Input

birthday = input('Enter your Birthday: (dd/mm/yyyy)?' )
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' +str(birthday_date))

birthday_eve = birthday_date - one_day
print('One Day Before My Birthday: ' +str(birthday_eve))


print('Today is: ' +str(current_date))
print('Yesterday was: ' +str(yesterday))