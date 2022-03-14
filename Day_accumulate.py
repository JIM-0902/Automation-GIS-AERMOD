from datetime import date
import time

def Day_Accumulate():

    seconds=time.time()
    result =time.localtime(seconds)

    year = result.tm_year
    month = result.tm_mon
    day = result.tm_mday
    hour = result.tm_hour



    month_accumulate=month-1
    if(year%4==0):
        Feb=29
    else:
        Feb=28

 

    # 1月
    if(month_accumulate==0):
        day_accumulate=0
    # 2月
    if(month_accumulate==1):
        day_accumulate=31
    # 3月
    if(month_accumulate==2):
        day_accumulate=31+Feb
    # 4月
    if(month_accumulate==3):
        day_accumulate=31+Feb+31
    # 5月
    if(month_accumulate==4):
        day_accumulate=31+Feb+31+30
    # 6月
    if(month_accumulate==5):
        day_accumulate=31+Feb+31+30+31
    # 7月
    if(month_accumulate==6):
        day_accumulate=31+Feb+31+30+31+30
    # 8月
    if(month_accumulate==7):
        day_accumulate=31+Feb+31+30+31+30+31
    # 9月
    if(month_accumulate==8):
        day_accumulate=31+Feb+31+30+31+30+31+31
    # 10月
    if(month_accumulate==9):
        day_accumulate=31+Feb+31+30+31+30+31+31+30
    # 11月
    if(month_accumulate==10):
        day_accumulate=31+Feb+31+30+31+30+31+31+30+31
    # 12月
    if(month_accumulate==11):
        day_accumulate=31+Feb+31+30+31+30+31+31+30+31+30
    
    day_accumulate=day_accumulate+day
    
    return day_accumulate

print(Day_Accumulate())







