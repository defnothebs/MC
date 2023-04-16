import re

def decimal(r):
    r1=[]
    for roman in r:
        list=re.findall('\w',roman)
        x=0
        for index in range(len(list)):
            if list[index] == 'I':
                list[index]=1
            if list[index] == 'V':
                list[index]=5
            if list[index] == 'X':
                list[index]=10
            if list[index] == 'L':
                list[index]=50
            if list[index] == 'C':
                list[index]=100
            if list[index] == 'D':
                list[index]=500
            if list[index] == 'M':
                list[index]=1000

        for index in range(len(list)-1):
            if list[index]<list[index+1]:
                x-=list[index]
            else:
                x+=list[index]

        if list[index-1]>=list[index]:
            x+=list[len(list)-1]
        else:
            x-=list[len(list)-1]

        r1.append(str(x))

    return r1

def roman(d):
    d1=[]
    for n in d:
        decimal=int(n)
        x=''
        while decimal>=1000:
            x+='M'
            decimal-=1000
        while decimal>=900:
            x+='CM'
            decimal-=900
        while decimal>=500:
            x+='D'
            decimal-=500
        while decimal>=400:
            x+='CD'
            decimal-=400
        while decimal>=100:
            x+='C'
            decimal-=100
        while decimal>=90:
            x+='XC'
            decimal-=90
        while decimal>=50:
            x+='L'
            decimal-=50
        while decimal>=40:
            x+='XL'
            decimal-=40
        while decimal>=10:
            x+='X'
            decimal-=10
        while decimal>=9:
            x+='IX'
            decimal-=9
        while decimal>=5:
            x+='V'
            decimal-=5
        while decimal>=4:
            x+='IV'
            decimal-=4
        while decimal>=1:
            x+='I'
            decimal-=1
        d1.append(x)
    
    return d1

def replace(s,og,new):
    while(og!=[]):
        max=0
        for i in range(len(og)):
            if len(og[i])>len(og[max]):
                max=i
                    
        s=s.replace(og[max],new[max])
        og.remove(og[max])
        new.remove(new[max])
    return s

x='1100 since V/III/MCMLXXXV'
r=re.findall('[IVXCML]+',x)
d=re.findall('[\d]+',x)
r1=decimal(r)
d1=roman(d)
x=replace(x,r,r1)
x=replace(x,d,d1)

print(x)