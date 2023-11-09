import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

C=[(1,6),(4,15),(7,7),(18,13),(11,6),(11,18),(12,10),(15,20),(16,6),(11,21),(18,3),(18,12),(19,25),(22,19)]
ps=np.array(C)
min=[]
max=[]
def f(point_1, point_2): 
  x1,y1=point_1
  x2,y2=point_2
  m=(y2-y1)/(x2-x1)
  b=y1-((y2-y1)/(x2-x1))*x1
  return lambda x: m*x+b

def ver_para_creer(VC):
  for i in range(0,len(VC)-1):
    if VC[i]!=VC[i+1]:
      return False
  return True 

def g(point_1,point_2):
 x=np.linspace(point_1[0],point_2[0],100)
 funcion=f(point_1,point_2)
 y=funcion(x)
 plt.plot(x,y,linestyle='-', color='blue')

def le(point_1,point_2,ps):
  a=point_2[0]-point_1[0]
  b=(point_1[1]-point_2[1])
  c=(point_2[1]*point_1[0]-point_2[0]*point_1[1])
  V=[]
  for i in range(0,len(ps)):
    if set(point_1)!=set(ps[i]) and set(point_2)!= set(ps[i]):
      v= (a*ps[i][1])+(b*ps[i][0])+c
      if v>0:
        max.append(ps[i])
      elif v<0:
        min.append(ps[i])

def leM(point_1,point_2,ps):
  a=point_2[0]-point_1[0]
  b=(point_1[1]-point_2[1])
  c=(point_2[1]*point_1[0]-point_2[0]*point_1[1])
  V=[]
  for i in range(0,len(ps)):
    if set(point_1)!=set(ps[i]) and set(point_2)!= set(ps[i]):
      v= (a*ps[i][1])+(b*ps[i][0])+c
      if v>0:
        V.append(1)
      elif v<0:
        V.append(-1)
  if ver_para_creer(V):
    return True
  return False


def recursion(LP,RP,ps,O, min, max):
  if O==True:
    min.clear()
    le(LP,RP,ps)
    mins= sorted(min, key= lambda t:(t[1],t[0]))
    F=mins[0]
    if(len(mins)<= 1):
      g(LP,F)
      g(F,RP)
    else:
      if leM(LP,F,mins) & leM(RP,F,mins):
        g(LP,F)
        g(F,RP)
      elif leM(LP,F,mins) or (not leM(RP,F,mins)):
        g(LP,F)
        recursion(F,RP,mins,True)
      elif (not leM(LP,F,mins)) or leM(RP,F,mins):
        g(RP,F)
        recursion(LP,F,mins,True)
      elif (not leM(LP,F,mins)) & (not leM(F,RP,mins)):
        recursion(LP,F,mins,False, min, max)
  else:
    max.clear()
    le(LP,RP,ps)
    maxs= sorted(max, key= lambda t:(t[1],t[0]))
    F=maxs[len(max)-1]
    if(len(maxs)<=1):
      g(LP,F)
      g(F,RP)
    else:
      if leM(LP,F,maxs) & leM(F,RP,maxs):
        g(LP,F)
        g(F,RP)
      elif leM(LP,F,maxs) or (not leM(F,RP,maxs)):
        g(LP,F)
        recursion(RP,F,maxs,False, max)
      elif (not leM(LP,F,maxs)) or leM(F,RP,maxs):
        g(F,RP)
        recursion(LP,F,maxs,False, min, max)
      elif (not leM(LP,F,maxs)) & (not leM(F,RP,maxs)):
        recursion(LP,F,maxs,False, min, max)

S=C[0]
E=C[len(C)-1]

x, y=np.array(C).transpose()
plt.plot(x,y, linestyle="",marker="*",color="red",markersize=12)
recursion(S,E,ps,True, min, max)
recursion(S,E,ps,False, min, max)
plt.show()
