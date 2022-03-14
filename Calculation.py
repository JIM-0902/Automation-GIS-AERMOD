import math
import csv

#計算露點溫度
def td(T,RH):
    r=(17.27*T/(237.7+T)+math.log(RH/100))
    Td=237.7*r/(17.27-r)
    return Td
'''
Td=td(26.1,76)
print(Td)
'''
#計算pasquall大氣穩定度分類
def Uv_value(uv,Uz):
    grade=None
    num=0
    if uv>float(0.8) and Uz<float(2):
        grade='等級A'

    elif uv>float(0.8) and float(2)<=Uz<=float(5):
        grade='等級B'
    elif uv>float(0.8) and Uz>float(5):
        grade='等級C'
    elif float(0.4)<uv<=float(0.8) and Uz<float(3):
        grade='等級B'
    elif float(0.4)<uv<=float(0.8) and float(3)<=Uz<=float(5):
        grade='等級C'
    elif float(0.4)<uv<=float(0.8) and Uz>float(5):
        grade='等級D'
    elif float(0.1)<uv<=float(0.4)and Uz<float(2):
        grade='等級B'
    elif float(0.1)<uv<=float(0.4)and float(2)<=Uz<=float(5):
        grade='等級C'
    elif float(0.1)<uv<=float(0.4)and Uz>float(5):
        grade='等級D'
    elif uv<float(0.1)and Uz<float(2):
        grade='等級F'
    elif uv<float(0.1)and float(2)<=Uz<=float(3):
        grade='等級E'
    elif uv<float(0.1)and Uz>float(3):
        grade='等級D'
    else:
        print('Error')
    

    if (grade=="等級A"):
        num=1
    if (grade=="等級B"):
        num=2
    if (grade=="等級C"):
        num=3
    if (grade=="等級D"):
        num=4
    if (grade=="等級E"):
        num=5
    if (grade=="等級F"):
        num=6

    return num
'''
print(Uv_value(0.1,0.9))
'''
#計算混合層高
def Mechanical_mixing_height(T,Td,Pasquill,Uz,Z,Z0):
    mechanical_mixing_height=(121/6)*(6-Pasquill)*(T-Td)+(0.169*Pasquill*(Uz+0.257)/(12*0.0000579*math.log(Z/Z0)))
    return mechanical_mixing_height

'''
print(Mechanical_mixing_height(26.1,Td,2,0.9,10,1.2))
'''








