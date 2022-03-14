import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import FLOAT
import write
import csv
import time

from Download_uv import task


def vd_value():
    adress=[]
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V440470")#德芳南路0
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V028800")#經貿路1
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003401")#臺灣大道-黎明路(往北)2

    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V017100")#中清路一段/進化北路口(往北近端號誌桿)(往北)3
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V017140")#中清路一段/進化北路口(往南近端號誌桿)(往南)4
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016940")#中清路一段(武昌路~漢口路間)(向南)5
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016700")#中清路二段(大連路~文心路間)(向北)6
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V015140")#中清路二段(文心路~大連路間)(向南)7
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003340")#中清路二段(經貿一路~大鵬路間)(向南)8
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V040600")#中清路二段(經貿一路~敦化路間)(向北)9
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016100")#中清路二段、經貿七路(向北)10
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016140")#中清路二段、經貿七路(向南)11
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V094800")#中清路二段、黎明路三段(向北)12
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016040")#中清路二段、經貿九路(向南)13

    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014820")#臺灣大道何厝街大墩路(向東)14
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014922")#臺灣大道-惠中路-慢車道(往東)15
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V053421")#臺灣大道-朝富路-慢車道(往東)16
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V053420")#臺灣大道-朝富路-快車道(往東)17
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014960")#臺灣大道-惠中路-快車道(往西)18
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V021461")#臺灣大道-河南路-慢車道(往西)19
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014900")#臺灣大道-惠中路-(往北)20
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014940")#臺灣大道-惠中路-(往南)21
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V021440")#臺灣大道-河南路-(往南)22
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V053400")#臺灣大道-朝富路(往北)23
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003461")#臺灣大道-黎明路(往西)24
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003401")#臺灣大道-黎明路(往北)25

    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V495460")#五權西路二段-萬和路二段(往北)26
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V058760")#五權西路-益豐路(往西)27
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V494820")#五權西路-龍富路(往東)28
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V116160")#五權西路-環中路(往東)29

    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V091960")#環中路一段、松竹路三段(向西)30
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V091900")#松竹路三段、環中路一段(向北)31
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V122760")#環中路一段、同榮東路(向西)32
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V117920")#環中路一段、中康街(向東)33
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V086360")#環中路一段、大雅交流道(向西)34
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V086320")#環中路一段、大雅交流道(向東)35
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V086620")#環中路一段、中清路二段(向東)36
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V087360")#環中路二段、中科路(向西)37
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V087220")#環中路二段、凱旋路(向東)38
    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V115901")#市政路-環中路橋外慢車道(往北)39

    adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/ShowForeignvd?id=nfbVD-T74-E-18.578-M-RS&source=nfb")#快速公路74號(崇德交流道到潭子交流道)40
    

    value=[]
    speed=[]
    #寫成i個陣列儲存
    for i in range(len(adress)):
        data=[]
        html = urllib.request.urlopen(adress[i]).read()
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup)

#下載關鍵字
        table = soup.find('table', {'class': 'table table-bordered table-striped table-hover table-condensed'})
        for elm in soup.select('tr'):
            if ("error" in elm):
                for tr in trs:
                    rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr('td')]) 
                    trs = table.find_all('tr')[1:]
                    continue
        rows=list

        str2=elm.get_text().split('\n')
        print(str2)


#存成陣列

        value.append(str2[3])
        speed.append(str2[2])

        sum=0
        for j in range(len(data)):
            sum = int(data[j])+sum
            print(sum)

    print("volume車流量:", value)
    print("speed車速", speed)

    '''
###
    value=[]
    
    #寫成i個陣列儲存
    for i in range(len(adress)):
        data=[]
        html = urllib.request.urlopen(adress[i]).read()
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup)

#下載關鍵字
        table = soup.find('table', {'class': 'table table-bordered table-striped table-hover table-condensed'})
        trs = table.find_all('tr')[1:]
        rows = list()

#用逗號分隔
        for tr in trs:
            rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr('td')])
            print(rows)
    
#判斷網址有幾筆車流，取該車流出來
            for i in range(len(rows)):
                data.append(rows[i][2])
                print('volume:',data)
    
#加總車流量
        sum=0
        for j in range(len(data)):
            sum = int(data[j])+sum
            print(sum)

#將車流量存成陣列
        value.append(sum)
        print('全部車流量:', value)
###
    '''
    
#抓取陣列
    a=value[3]
    print('中清路一段/進化北路口(往北近端號誌桿)(往北):', a)
    b=value[4]
    print('中清路一段/進化北路口(往北近端號誌桿)(往南):', b)
    c=value[5]
    print('中清路一段(武昌路~漢口路間)(向南):', c)
    d=value[6]
    print('中清路二段(大連路~文心路間)(向北):', d)
    e=value[7]
    print('中清路二段(文心路~大連路間)(向南):', e)
    f=value[8]
    print("中清路二段(經貿一路~大鵬路間)(向南):", f)
    h=value[9]
    print("中清路二段(經貿一路~敦化路間)(向北):", h)
    i=value[10]
    print("中清路二段、經貿七路(向北):", i)
    j=value[11]
    print("中清路二段、經貿七路(向南):", j)
    k=value[12]
    print("中清路二段、黎明路三段(向北):", k)
    l=value[13]
    print("中清路二段、經貿九路(向南):", l)
    m=value[14]
    print("臺灣大道何厝街大墩路(向東):", m)
    n=value[15]
    print("臺灣大道-惠中路-慢車道(往東):", n)
    o=value[16]
    print("臺灣大道-朝富路-慢車道(往東):", o)
    p=value[17]
    print("臺灣大道-朝富路-快車道(往東):", p)
    q=value[18]
    print("臺灣大道-惠中路-快車道(往西):", q)
    r=value[19]
    print("臺灣大道-河南路-慢車道(往西):",r)
    s=value[20]
    print("臺灣大道-惠中路-(往北):", s)
    u=value[21]
    print("臺灣大道-惠中路-(往南):", u)
    w=value[22]
    print("臺灣大道-河南路-(往南):", w)
    x=value[23]
    print("臺灣大道-朝富路(往北):", x)
    y=value[24]
    print("臺灣大道-黎明路(往西):", y)
    z=value[25]
    print("臺灣大道-黎明路(往北):", z)
    aa=value[26]
    print("五權西路二段-萬和路二段(往北):", aa)
    bb=value[27]
    print("五權西路-益豐路(往西):", bb)
    cc=value[28]
    print("五權西路-龍富路(往東):", cc)
    dd=value[29]
    print("五權西路-環中路:", dd)
    ee=value[30]
    print("環中路一段、松竹路三段(向西):", ee)
    gg=value[31]
    print("松竹路三段、環中路一段(向北):", gg)
    hh=value[32]
    print("環中路一段、同榮東路(向西):", hh)
    ii=value[33]
    print("環中路一段、中康街(向東):" ,ii)
    jj=value[34]
    print("環中路一段、大雅交流道(向西):", jj)
    kk=value[35]
    print("環中路一段、大雅交流道(向東):", kk)
    ll=value[36]
    print("環中路一段、中清路二段(向東):", ll)
    mm=value[37]
    print("環中路二段、中科路(向西):", mm)
    nn=value[38]
    print("環中路二段、凱旋路(向東):", nn)
    pp=value[39]
    print("市政路-環中路橋外慢車道(往北):", pp)
    qq=value[40]
    print("快速公路74號(崇德交流道到潭子交流道):", qq)
    


    
    #輸入aermod.inp檔案
    f = open("aermod.inp", "w")

    # 寫入資料
    f.write("CO STARTING\n")
    f.write("   TITLEONE AERMOD Model\n")
    f.write("   MODELOPT DFAULT CONC\n")
    f.write("   AVERTIME 1 PERIOD\n")
    f.write("   URBANOPT 2000000 TC\n")
    f.write("   POLLUTID CO\n")
    f.write("   RUNORNOT RUN\n")
    f.write("   ERRORFIL ERROR.OUT\n")
    f.write("CO FINISHED\n")
    f.write("\n")
    f.write("SO STARTING\n")
    f.write("** Point Source         UTM_E  UTM_N  ZS\n")
    f.write("   LOCATION CO0003 VOLUME 216945 2673090 9.0\n")
    f.write("   LOCATION CO0004 VOLUME 216915 2673138 9.0\n")
    f.write("   LOCATION CO0005 VOLUME 216743 2673758 9.0\n")
    f.write("   LOCATION CO0006 VOLUME 216592 2674394 9.0\n")
    f.write("   LOCATION CO0007 VOLUME 216511 2674550 9.0\n")
    #f.write("   LOCATION CO0008 VOLUME 216268 2674900 9.0\n")
    f.write("   LOCATION CO0010 VOLUME 215904 2675562 9.0\n")
    f.write("   LOCATION CO0011 VOLUME 215500 2676326 9.0\n")
    f.write("   LOCATION CO0012 VOLUME 215378 2676440 9.0\n")
    f.write("   LOCATION CO0013 VOLUME 215237 2676797 9.0\n")
    f.write("   LOCATION CO0014 VOLUME 215115 2676979 9.0\n")
    f.write("   LOCATION CO0015 VOLUME 214729 2672879 9.0\n")
    f.write("   LOCATION CO0016 VOLUME 214029 2673307 9.0\n")
    f.write("   LOCATION CO0017 VOLUME 213319 2673808 9.0\n")
    f.write("   LOCATION CO0018 VOLUME 213309 2673796 9.0\n")
    f.write("   LOCATION CO0019 VOLUME 214080 2673269 9.0\n")
    f.write("   LOCATION CO0020 VOLUME 213542 2673665 9.0\n")
    f.write("   LOCATION CO0021 VOLUME 214039 2673249 9.0\n")
    f.write("   LOCATION CO0022 VOLUME 214070 2673317 9.0\n")
    f.write("   LOCATION CO0023 VOLUME 213522 2673695 9.0\n")
    f.write("   LOCATION CO0024 VOLUME 213329 2673765 9.0\n")
    f.write("   LOCATION CO0025 VOLUME 213066 2673975 9.0\n")
    f.write("   LOCATION CO0026 VOLUME 213096 2674050 9.0\n")
    f.write("   LOCATION CO0027 VOLUME 213453 2670692 9.0\n")
    f.write("   LOCATION CO0028 VOLUME 212276 2671440 9.0\n")
    f.write("   LOCATION CO0029 VOLUME 211982 2671536 9.0\n")
    f.write("   LOCATION CO0030 VOLUME 211779 2671635 9.0\n")
    f.write("   LOCATION CO0031 VOLUME 216721 2677369 9.0\n")
    f.write("   LOCATION CO0032 VOLUME 216569 2677242 9.0\n")
    f.write("   LOCATION CO0033 VOLUME 216000 2677372 9.0\n")
    f.write("   LOCATION CO0034 VOLUME 215603 2677298 9.0\n")
    f.write("   LOCATION CO0035 VOLUME 215177 2677293 9.0\n")
    f.write("   LOCATION CO0036 VOLUME 215065 2677203 9.0\n")
    f.write("   LOCATION CO0037 VOLUME 214933 2677113 9.0\n")
    f.write("   LOCATION CO0038 VOLUME 214770 2677106 9.0\n")
    f.write("   LOCATION CO0039 VOLUME 214190 2676776 9.0\n")
    f.write("   LOCATION CO0040 VOLUME 212291 2673082 9.0\n")
    f.write("** Volume Source    QS hgt \n")
    f.write("** Parameters:     ---- ---- ----  ---- \n")
    f.write("** SRCPARAM PM25 0.0572 0.0 500 3.0\n")
    f.write(f"   SRCPARAM CO0003 {((0.7990*int(a)/200))} 0.0 500 0.3\n") #使用teds11.0作為排放係數來源
    f.write(f"   SRCPARAM CO0004 {((0.7990*int(b)/200))} 0.0 500 0.3\n") #V.K.T單位為(KM/年)
    f.write(f"   SRCPARAM CO0005 {((0.7990*int(c)/200))} 0.0 500 0.3\n") #所以排放係數(g/vkt*輛)
    f.write(f"   SRCPARAM CO0006 {((0.7990*int(d)/200))} 0.0 500 0.3\n") #排放率(g/s)=排放係數(g/vkt*輛)*V.K.T(KM/年)*車流量(輛/5min)
    f.write(f"   SRCPARAM CO0007 {((0.7990*int(e)/200))} 0.0 500 0.3\n") #KM/年=1000M/60*24*365min=1.9025*0.001m/min=3.1709*0.00001m/s
    #f.write(f"  SRCPARAM CO0008 {((0.7990*int(f)/200))} 0.0 500 0.3\n") #乘上每個網格50公尺/5(每分鐘多少台車子)
    f.write(f"   SRCPARAM CO0010 {((0.7990*int(h)/200))} 0.0 500 0.3\n") #車流量換算成(輛/S)=輛/300s
    f.write(f"   SRCPARAM CO0011 {((0.7990*int(i)/200))} 0.0 500 0.3\n")  #=1.9025*0.001m/min
    f.write(f"   SRCPARAM CO0012 {((0.7990*int(k)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0013 {((0.7990*int(l)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0014 {((0.7990*int(m)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0015 {((0.7990*int(n)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0016 {((0.7990*int(o)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0017 {((0.7990*int(p)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0018 {((0.7990*int(q)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0019 {((0.7990*int(r)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0020 {((0.7990*int(s)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0021 {((0.7990*int(u)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0022 {((0.7990*int(w)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0023 {((0.7990*int(x)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0024 {((0.7990*int(y)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0025 {((0.7990*int(z)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0026 {((0.7990*int(aa)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0027 {((0.7990*int(bb)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0028 {((0.7990*int(cc)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0029 {((0.7990*int(dd)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0030 {((0.7990*int(ee)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0031 {((0.7990*int(gg)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0032 {((0.7990*int(hh)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0033 {((0.7990*int(ii)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0034 {((0.7990*int(jj)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0035 {((0.7990*int(kk)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0036 {((0.7990*int(ll)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0037 {((0.7990*int(mm)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0038 {((0.7990*int(nn)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0039 {((0.7990*int(pp)/200))} 0.0 500 0.3\n")
    f.write(f"   SRCPARAM CO0040 {((0.7990*int(qq)/200))} 0.0 500 0.9\n")
    f.write("**   EMISUNIT 8750 g/sec ppm\n")
    f.write("   EMISUNIT 54687 g/sec ppm\n")
    f.write("   URBANSRC ALL\n")
    f.write("   SRCGROUP ALL\n")
    f.write("SO FINISHED\n")
    f.write(" \n")
    f.write("RE STARTING\n")
    f.write("   GRIDCART CO STA\n")
    f.write("            XYINC 211044 217 50 2669728 157 50\n")
    f.write("            CO END\n")
    f.write("RE FINISHED\n")
    f.write(" \n")
    f.write("ME STARTING\n")
    f.write("   SURFFILE Output.sfc\n")
    f.write("   PROFFILE Output.pfl\n")
    f.write("   SURFDATA 467490 2021 Taichung\n")
    f.write("   UAIRDATA 466920 2021 Taipei\n")
    f.write("   PROFBASE 84.0\n")
    f.write("ME FINISHED\n")
    f.write(" \n")
    f.write("OU STARTING\n")
    f.write("   RECTABLE ALLAVE FIRST\n")
    f.write("   DAYTABLE ALLAVE\n")
    f.write("   MAXTABLE ALLAVE 50\n")
    f.write("   POSTFILE 1 all plot CO.csv\n")
    f.write("OU FINISHED\n")


vd_value()
   
    


#錯誤示範    
"""
    for i in range(len(rows)):
        if len(rows[i])<=1:
            data.append(rows[i][2])
        elif len(rows[i])>=2:
            data.append(rows[i][2])
    print(data)
"""