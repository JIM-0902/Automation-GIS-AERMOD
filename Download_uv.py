import csv
from datetime import date
from os import write
import requests
import pandas as pd
import io
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import math

def task():
    
    def timedata_change1(result1):
        year           = result1.tm_year
        month          = result1.tm_mon
        day            = result1.tm_mday
        hour           = result1.tm_hour
        minutes        = result1.tm_min
        seconds        = result1.tm_sec

    
        #print(year ,month ,day ,hour ,minutes ,seconds)
    
    
        
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
    

        Y    = str(year)
        Hour = str(hour)
        Min  = str(minutes)
        S    = str(seconds)

        TIME = Y+'-'+M+'-'+D+' '+H+':00'
    
        #print(TIME)
    
        return TIME
        
    # 抓取資料，下載csv檔
    url = "https://data.epa.gov.tw/api/v1/uv_s_01?limit=1000&api_key=93304003-71f2-4da8-8416-64fc1980ef65&sort=ImportDate%20desc&format=csv"
    uv=requests.get(url).content
    uvdata=pd.read_csv(io.StringIO(uv.decode('utf-8')))

    # 時間
    A=True
    seconds=time.time()
    result1 =time.localtime(seconds)
    timedata_change1(result1)
    time_condition = len(uvdata[(uvdata.County=="臺中市")&(uvdata.PublishTime==timedata_change1(result1))])
    #print(time_condition)
    
    while(A==True):
        result1 =time.localtime(seconds)
        timedata_change1(result1)

        time_condition = len(uvdata[(uvdata.County=="臺中市")&(uvdata.PublishTime==timedata_change1(result1))])
        #print(time_condition)

        List =[time_condition]
        #print(List)
        A    = 0 in List
        #print(A)
        seconds=seconds-3600
        #print(result)
    
    #print(result1)
    
    
    year           = result1.tm_year
    month          = result1.tm_mon
    day            = result1.tm_mday
    hour           = result1.tm_hour
    minutes        = result1.tm_min
    seconds        = result1.tm_sec

    
    #print('抓取的資料時間:',year ,month ,day ,hour ,minutes ,seconds)
    
    year_txt=year
    year_txt=str(year_txt)


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
    

    Y    = str(year)
    Hour = str(hour)
    Min  = str(minutes)
    S    = str(seconds)

    TIME= Y+'-'+M+'-'+D+' '+H+':00'
 
    
    
    
    

    data_uv=[]

    def download1(County):
        name=uvdata[(uvdata.County=="臺中市")&(uvdata.SiteName=="臺中")&(uvdata.PublishTime==TIME)]
        #print(len(name))

                                                                                   
        County=[]
        PublishAgency=[]
        PublishTime=[]
        SiteName=[]
        UVI=[]                                                           

        for i in range(len(name)):
            County.append(name.iloc[i,0])
            PublishAgency.append(name.iloc[i,1])
            PublishTime.append(name.iloc[i,2])
            SiteName.append(name.iloc[i,3])
            UVI.append(name.iloc[i,4])
    
        dict={"County":County,"PublishAgency":PublishAgency,"PublishTime":PublishTime,"SiteName":SiteName,"UVI":UVI}
    
        df=pd.DataFrame(dict)
        df.to_csv('uv.csv',index=False, encoding='big5')

        time.sleep(1)

        file='uv.csv'

        with open(file,encoding='big5') as csvFile:
            csvReader = csv.reader(csvFile)
            datas = list(csvReader)
            print(datas)
            
        data_uv.append(datas[0][4])
        data_uv.append(datas[1][4])
    
        print(data_uv)
        
    
        localtime = time.asctime( time.localtime(time.time()) )
        #print ("下載時間:", localtime) 
    
        return data_uv[1]
    
       
    return download1("臺中市")

        
a=task()