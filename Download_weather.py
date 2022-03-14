from time import thread_time_ns, time_ns
import urllib.request as req
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import Calculation
import math
import Download_uv
import time
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler
import XLS
import Vd_value
import csv







def task():

#抓取中央氣象局網址，真正的網址是XHR的格式，所以不是一般看到的那個
#從network選取XHR(所有採用AJAX技術之網站)
    url = "https://www.cwb.gov.tw/V8/C/W/Observe/MOD/24hr/46749.html?T=305"

    requests=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        })
    with req.urlopen(requests) as response:
        data=response.read().decode('utf-8')


#解析原始碼，取得氣象值
    root=bs4.BeautifulSoup(data,"html.parser")
    #print(root)

#時間資料處理
    ths=root.find('th')
    row=str(ths.get_text())
    row1=str(row.split())
    print("下載中央氣象局的資料時間:", row1)

    month = int(row1[2:4])
    day = int(row1[5:7])
    hour = int(row1[11:13])
    #print(month)

    if (hour<0):
        hour=hour+24
        
        
    if (month<10):
        M = str(month)
        M = '0'+M
        month_txt=str(month)
        month_txt=' '+month_txt
    else:
        M = str(month)
        month_txt=str(month)
    if (day<10):
        D = str(day)
        D = '0'+D
        day_txt=str(day)
        day_txt=' '+str(day)
    else:
        D = str(day)
        day_txt=str(day)
        
    if (hour<10):
        H = str(hour)
        H = '0'+H
        hour_txt=str(hour)
        hour_txt=' '+str(hour)
    else:
        H = str(hour)
        hour_txt=str(hour)
    #print(month_txt)


#氣象資料下載
    trs = root.find_all('tr')
    rows = list()
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr('td')])
    print('中央氣象局原始數據:',rows[0])


#使用之數據
    Uz=float(rows[0][3]) #風速
    
    if Uz == "--":
        Uz=0
   
    T=float(rows[0][0]) #溫度
    RH=float(rows[0][6]) #相對濕度
    winddirect=str(rows[0][2]) #風向
    rainfall=float(rows[0][8]) #降雨量
    uv=float(Download_uv.task()) #紫外線
    Pasquill=Calculation.Uv_value(uv,Uz)
    
    Press=float(rows[0][7]) #大氣壓力

    print('風速:',Uz)
    print('溫度:',T)
    print('相對溼度:',RH)
    print('風向:',winddirect)
    print('降雨量:',rainfall)
    print('紫外線:',uv)
    print('大氣壓力:',Press)

    Z=10
    Z0=0.2

#將風向轉成度數
    if winddirect=="北":
        winddirect_value=int(0)
    elif winddirect=="北北東":
        winddirect_value=int(22.5)
    elif winddirect=="東北":
        winddirect_value=int(45)
    elif winddirect=="東北東":
        winddirect_value=int(67.5)
    elif winddirect=="東":
        winddirect_value=int(90)
    elif winddirect=="東南東":
        winddirect_value=int(112.5)
    elif winddirect=="東南":
        winddirect_value=int(135)
    elif winddirect=="南南東":
        winddirect_value=int(157.5)
    elif winddirect=="南":
        winddirect_value=int(180)
    elif winddirect=="南南西":
        winddirect_value=int(202.5)
    elif winddirect=="西南":
        winddirect_value=int(225)
    elif winddirect=="西南西":
        winddirect_value=int(247.5)
    elif winddirect=="西":
        winddirect_value=int(270)
    elif winddirect=="西北西":
        winddirect_value=int(292.5)
    elif winddirect=="西北":
        winddirect_value=int(315)
    elif winddirect=="北北西":
        winddirect_value=int(337.5)
    elif winddirect=="靜風":
        winddirect_value=int(0)

    
    # 計算Td
    Td = Calculation.td(T,RH)

    # 計算混和層高
    mixing_height = Calculation.Mechanical_mixing_height(T,Td,Pasquill,Uz,Z,Z0)

    print('混和層高度：', mixing_height)
    print('uv值:',uv)
    print('大氣穩定度:',Pasquill)

# 四捨五入或是無條件捨去
    winddirec      = math.floor(winddirect_value)
    mixing_height  = round(mixing_height)

    print('四捨五入後混合層高度:',mixing_height)
    
    
    seconds=time.time()
    result =time.localtime(seconds)
    accumulate_day = result.tm_yday

# 轉換成str(字串)格式
    windspeed        =str(Uz)
    winddirec        =str(winddirect_value)
    rainfall         =str(rainfall)
    rh               =str(RH)
    accumulate_day   =str(accumulate_day)
    mixing_height    =str(mixing_height)
    temp             = round(T, 1)
    Press            =round(Press)

    # 轉換sfc輸入格式
    windspeed       = windspeed
    winddirec       = winddirec+'.0'
    ambtemp         = temp+273
    rainfall        = rainfall+'0'
    RH              = rh[:-1]
    mixing_height   = mixing_height+'.'
    press_pfl       =str(Press)+'.'


    # 寫入SFC檔
    path='Output.SFC'
    R=open(path,'w')
    R.write('   24.145N  120.684E          UA_ID:   466920  SF_ID:   467490  OS_ID:              VERSION: 21112  BULKRN  CCVR_Sub TEMP_Sub\n')
    R.write("22"+'{:>3}'.format(month_txt)+'{:>3}'.format(day_txt)+'{:>4}'.format(accumulate_day)+'{:>3}'.format(hour_txt)+'{:>7}'.format('-4.0')+'{:>7}'.format('0.500')+'{:>7}'.format('-9.000')+'{:>7}'.format('-9.000')+'{:>6}'.format('-999.')+'{:>6}'.format(mixing_height)+'{:>9}'.format('12.3')+'{:>8}'.format('1.2000')+'{:>7}'.format('0.80')+'{:>7}'.format('1.00')+'{:>8}'.format(windspeed)+'{:>7}'.format(winddirec)+'{:>7}'.format('14.0')+'{:>7}'.format(ambtemp)+'{:>7}'.format('2.0')+'{:>6}'.format('0')+'{:>7}'.format(rainfall)+'{:>7}'.format(RH)+'{:>7}'.format(press_pfl)+'{:>6}'.format('0')+'{:>15}'.format('NAD-SFC NoSubs'))
    R.close()
    
    # 寫入PFL檔
    path2='Output.PFL'
    R2=open(path2,'w')
    R2.write('22'+'{:>3}'.format(month_txt)+'{:>3}'.format(day_txt)+'{:>3}'.format(hour_txt)+'{:>8}'.format('14.0')+'{:>2}'.format('1')+'{:>8}'.format(winddirec)+'{:>9}'.format(windspeed)+'{:>9}'.format(temp, '.2f')+'{:>9}'.format('99.00')+'{:>9}'.format('99.00'))
    R2.close()


    #輸入車流量資料
    time.sleep(2)
    Vd_value.vd_value()
    print("車流量輸入+INP檔完成")
    time.sleep(2)


    #呼叫檔案執行
    path3='aermod.exe'
    subprocess.call(path3)

    #使輸出csv檔案轉檔成xls檔，方便GIS使用
    time.sleep(2)
    XLS.XLS()
    print("轉檔成功")


    #將天氣資料存檔
    mixing_height_value=[]
    Uz_value=[]
    temp_value=[]
    days_value=[]
    Pasquill_value=[]
    winddirect_value=[]
    

    mixing_height_value.append(mixing_height)
    Uz_value.append(Uz)
    temp_value.append(temp)
    days_value.append(row1)
    Pasquill_value.append(Pasquill)
    winddirect_value.append(winddirect)
    
 
    with open('Mechanical mixing height.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([days_value[0],mixing_height_value[0],Uz_value[0],temp_value[0],Pasquill_value[0],winddirect_value[0]])

    time.sleep(10)

    



task()    
#排成


scheduler=BlockingScheduler()
scheduler.add_job(task,"interval",minutes=60)
scheduler.start()


'''
import Open_GIS
'''









