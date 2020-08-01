def is_leap_year(year):
    if year%4 == 0:
        if year%100 ==0 and year%400 != 0: #3 years per 400 surplus 
            return False
    
        return True
    else:   
        return False

def month_name(number):
    if number == 1:
        return 'January'
    elif number == 2:
        return 'February'
    elif number == 3:
        return 'March'
    elif number == 4:
        return 'April'
    elif number == 5:
        return 'May'
    elif number == 6:
        return 'June'   
    elif number == 7:
        return 'July'
    elif number == 8:
        return 'August'
    elif number == 9:
        return 'September'
    elif number == 10:
        return 'October'
    elif number == 11:
        return 'November'
    elif number == 12:
        return 'December'
    
def days_in_month(month_number,year):
    if month_number in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month_number in {4, 6, 9, 11}:
        return 30
    elif month_number == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
        
def first_day_of_year(year):
        day_num = ((1 + 5*((year - 1)%4)) + 4*((year - 1)%100) + 6*((year - 1)%400))%7
        return day_num
    
def first_day_of_month(month_number, year):
    weekday_num = first_day_of_year(year)
    day_num = 0
    for m in range(1, month_number):
        day_num += days_in_month(m,year)
        
    for i in range(1,day_num+1):            #day num starts at 0
        if weekday_num == 6:
            weekday_num = 0
        
        else:
            weekday_num += 1
            
    return weekday_num            