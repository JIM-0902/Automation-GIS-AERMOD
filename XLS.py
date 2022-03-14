import write
import csv
import numpy as np
import xlwt
from xlwt.Style import add_palette_colour
import pandas as pd

def XLS():
    with open('CO.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
        #print(column)
        #print(len(column))
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        g=[]
        h=[]
        k=[] 
        l=[]
        a.append('x')
        b.append('y')
        c.append('AVERAGE CONC')
        d.append('ZELEV')
        e.append('ZHILL')   
        f.append('ZFLAG') 
        g.append('AVE') 
        h.append('GRP')   
        k.append('DATE')
        l.append('NET ID')
        
        
        for i in range(8,len(column)):
            str2 = column[i][0].split()
            #print(str2)
            
            a.append(float(str2[0]))
            b.append(float(str2[1]))
            c.append(float(str2[2]))
            d.append(float(str2[3]))
            e.append(float(str2[4]))
            f.append(float(str2[5]))
            g.append(str2[6])
            h.append(str2[7])
            k.append(float(str2[8]))
            l.append(str2[9])
        
            
    
            workbook = xlwt.Workbook(encoding='utf-8')
            worksheet = workbook.add_sheet('Worksheet')
        #print(len(a))
        for j in range((len(column)-7)):
            #print(j)
            worksheet.write(j, 0,a[j])
            worksheet.write(j, 1,b[j])
            worksheet.write(j, 2,c[j])
            worksheet.write(j, 3,d[j])
            worksheet.write(j, 4,e[j])
            worksheet.write(j, 5,f[j])
            worksheet.write(j, 6,g[j])
            worksheet.write(j, 7,h[j])
            worksheet.write(j, 8,k[j])
            worksheet.write(j, 9,l[j])
        workbook.save('Excel_test.xls')
    print('Funtion working good')
         
    
    with open('zhongming_co.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([a[9374],b[9374],c[9374],k[9374]])

    with open('Xitun_co.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([a[15285],b[15285],c[15285],k[15285]])

    with open('Taiping_co.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([a[4018],b[4018],c[4018],k[4018]])

    

XLS()





