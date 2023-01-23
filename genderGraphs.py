import numpy
import random
import matplotlib.pyplot as plt
import math

Jan = random.randint(300000,345000)
Feb = random.randint(300000,345000)
Mar = random.randint(300000,345000)
Apr = random.randint(300000,345000)
May = random.randint(300000,345000)
Jun = random.randint(300000,345000) 
Jul = random.randint(300000,345000)
Aug = random.randint(300000,345000) 
Sep = random.randint(300000,345000)
octo = random.randint(300000,345000)
Nov = random.randint(300000,345000)
Dec = random.randint(300000,345000)

malePercentage = round(random.uniform(40.00,42.00),2)
femalePercentage = 100.00-malePercentage 
malePercentage = round((malePercentage/100.00),2)
femalePercentage = round((femalePercentage/100.00),2)


JanMale = round((Jan*malePercentage),0)
JanFemale = Jan - JanMale
FebMale = round((Feb*malePercentage),0)
FebFemale = Feb - FebMale
MarMale = round((Mar*malePercentage),0)
MarFemale = Mar - MarMale
AprMale = round((Apr*malePercentage),0)
AprFemale = Apr - AprMale
MayMale = round((May*malePercentage),0)
MayFemale = May - MayMale
JunMale = round((Jun*malePercentage),0)
JunFemale = Jun - AprMale
JulMale = round((Jul*malePercentage),0)
JulFemale = Jul - JulMale
AugMale = round((Aug*malePercentage),0)
AugFemale = Aug - AugMale
SepMale = round((Sep*malePercentage),0)
SepFemale = Sep - SepMale
OctoMale = round((octo*malePercentage),0)
OctoFemale = octo - OctoMale
NovMale = round((Nov*malePercentage),0)
NovFemale = Nov - NovMale
DecMale = round((Dec*malePercentage),0)
DecFemale = Dec - DecMale
janGenderBoyNum = 0
janGenderGirlNum = 0 
febGenderBoyNum = 0
febGenderGirlNum = 0
marGenderBoyNum = 0
marGenderGirlNum = 0
aprGenderBoyNum = 0
aprGenderGirlNum = 0
mayGenderBoyNum = 0
mayGenderGirlNum = 0
junGenderBoyNum = 0
junGenderGirlNum = 0
julGenderBoyNum = 0
julGenderGirlNum = 0
augGenderBoyNum = 0
augGenderGirlNum = 0
sepGenderBoyNum = 0
sepGenderGirlNum = 0
octGenderBoyNum = 0
octGenderGirlNum = 0
novGenderBoyNum = 0
novGenderGirlNum = 0
decGenderBoyNum = 0
decGenderGirlNum = 0
for i in range(0,100):           
    janGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if janGender == 1:
        janGenderFinding = 'Boy'
        janGenderBoyNum += 1    
    elif janGender != 1:
        janGenderFinding = 'Girl'
        janGenderGirlNum += 1
    febGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if febGender == 1:
        febGenderFinding = 'Boy'
        febGenderBoyNum += 1    
    elif febGender != 1:
        febGenderFinding = 'Girl'
        febGenderGirlNum += 1
    marGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if marGender == 1:
        marGenderFinding = 'Boy'
        marGenderBoyNum += 1
    elif marGender != 1:
        marGenderFinding = 'Girl'
        marGenderGirlNum += 1
    aprGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if aprGender == 1:
        aprGenderFinding = 'Boy'
        aprGenderBoyNum +=1
    elif aprGender != 1:
        aprGenderFinding = 'Girl'
        aprGenderGirlNum +=1
    mayGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if mayGender == 1:
        mayGenderFinding = 'Boy'
        mayGenderBoyNum += 1
    elif mayGender != 1:
        mayGenderFinding = 'Girl'
        mayGenderGirlNum +=1

    junGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if junGender == 1:
        junGenderFinding = 'Boy'
        junGenderBoyNum += 1
    elif junGender != 1:
        junGenderFinding = 'Girl'
        junGenderGirlNum += 1
    julGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if julGender == 1:
        julGenderFinding = 'Boy'
        julGenderBoyNum += 1
    elif julGender != 1:
        julGenderFinding = 'Girl'
        julGenderGirlNum += 1
    augGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if augGender == 1:
        augGenderFinding = 'Boy'
        augGenderBoyNum += 1
    elif augGender != 1:
        augGenderFinding = 'Girl'
        augGenderGirlNum += 1
    sepGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if sepGender == 1:
        sepGenderFinding = 'Boy'
        sepGenderBoyNum += 1
    elif sepGender != 1:
        sepGenderFinding = 'Girl'
        sepGenderGirlNum += 1
    octGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if octGender == 1:
        octGenderFinding = 'Boy'
        octGenderBoyNum += 1
    elif octGender != 1:
        octGenderFinding = 'Girl'
        octGenderGirlNum += 1
    novGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if novGender == 1:
        novGenderFinding = 'Boy'
        novGenderBoyNum +=1
    elif novGender != 1:
        novGenderFinding = 'Girl'
        novGenderGirlNum += 1
    decGender = math.floor(random.uniform(0,1/(1-malePercentage)))
    if decGender == 1:
        decGenderFinding = 'Boy'
        decGenderBoyNum +=1
    elif decGender != 1:
        decGenderFinding = 'Girl'
        decGenderGirlNum +=1
f1 = plt.figure(1)
a=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
b1=[janGenderBoyNum,febGenderBoyNum,marGenderBoyNum,aprGenderBoyNum,mayGenderBoyNum,junGenderBoyNum,julGenderBoyNum,augGenderBoyNum,sepGenderBoyNum,octGenderBoyNum,novGenderBoyNum,decGenderBoyNum]
b2=[janGenderGirlNum,febGenderGirlNum,marGenderGirlNum,aprGenderGirlNum,mayGenderGirlNum,junGenderGirlNum,julGenderGirlNum,augGenderGirlNum,sepGenderGirlNum,octGenderGirlNum,novGenderGirlNum,decGenderGirlNum]
m1 = plt.bar(a,b1,color='b')
m2 = plt.bar(a,b2,color='r',bottom=b1)
f2 = plt.figure(2)
x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
y1=[JanMale,FebMale,MarMale,AprMale,MayMale,JunMale,JulMale,AugMale,SepMale,OctoMale,NovMale,DecMale]
y2=[JanFemale,FebFemale,MarFemale,AprFemale,MayFemale,JunFemale,JulFemale,AugFemale,SepFemale,OctoFemale,NovFemale,DecFemale]
p1 = plt.bar(x,y1,color='b')
p2 = plt.bar(x,y2,color='r',bottom=y1)
plt.legend((p1[0],p2[0]),('Boys','Girls'))
plt.show()
