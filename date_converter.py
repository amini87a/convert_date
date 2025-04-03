def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def shamsi_to_miladi(year, month, day):
    if month > 10 or (month == 10 and day > 10):
        year += 622
    else:
        year += 621
    
    if is_leap(year):
        miladi_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        miladi_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    sh_to_mi = {
        1: (3, 21), 2: (4, 21), 3: (5, 22), 4: (6, 22), 5: (7, 23), 6: (8, 23),
        7: (9, 23), 8: (10, 23), 9: (11, 22), 10: (12, 22), 11: (1, 21), 12: (2, 20)
    }
    
    miladi_month, base_day = sh_to_mi[month]
    miladi_day = base_day + (day-1)
    
    while miladi_day > miladi_days[miladi_month-1]:
        miladi_day -= miladi_days[miladi_month-1]
        
        miladi_month += 1
        if miladi_month > 12:
            miladi_month = 1
    
    if (month>=1 and month<=3)or (month>=6 and month<=10):
        miladi_day-=1
    if month==5 and day>=1 and day>=9:
        miladi_day-=1
    elif month==5 and day>=10:
        miladi_day-=2
    
    print(f"Miladi: year:{year} month:{miladi_month} day:{miladi_day}")

def miladi_to_shamsi(year, month, day):
    
    if month < 3 or (month == 3 and day < 21):
        year -= 622
    else:
        year -= 621
    
    if is_leap(year):
        shamsi_days = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30]
    else:
        shamsi_days = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    
    mi_to_sha = {
        1: (10, 11), 2: (11, 12), 3: (12, 11), 4: (1, 12), 5: (2, 11), 6: (3, 11),
        7: (4, 10), 8: (5, 10), 9: (6, 10), 10: (7, 10), 11: (8, 10), 12: (9, 9)
    }
    
    shamsi_month, base_day = mi_to_sha[month]
    shamsi_day = base_day + (day-1)
    
    
    while shamsi_day > shamsi_days[shamsi_month - 1]:
        shamsi_day -= shamsi_days[shamsi_month - 1]
        shamsi_month += 1
    
        if shamsi_month > 12:
            shamsi_month = 1
    if (month>=1 and month<=2)or (month>=5 and month<=9)or(month==11):
        shamsi_day+=1
    elif month==12:
        shamsi_day+=2
    
    print(f"Shamsi: year:{year} month:{shamsi_month} day:{shamsi_day}")

while True:
    mode = int(input("Choose conversion mode: shamsi->miladi(1)  miladi->shamsi(2) :"))
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    
    if mode == 1:
        shamsi_to_miladi(year, month, day)
    elif mode == 2:
        miladi_to_shamsi(year, month, day)
    else:
        print("Invalid choice! Please enter 1 or 2.") 