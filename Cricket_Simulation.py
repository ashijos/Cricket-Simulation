#!/usr/bin/env python
# coding: utf-8

# In[2]:


## match without rating
ball_wicket=[]
ball=[]
n=1
ball.append(n)
base=30
bat=12
main=[]
bowler=[]
for i in range(bat):
    if len(ball)==120:
        break
    else:
        list1=[]
        runs = [0, 1, 2, 3, 4,6]
        avg=float(input("enter avg :"))
        sr=float(input("enter your sr :"))    
        p = 0.075 + (0.0002 * (base - avg)) if avg < base else 0.075 - (0.0007 * (avg - base))
        for k in range(1,5):
            if n==1:
                eco=float(input("enter bowler's economy :"))        
            for j in range(1,120):
                if n%6==1:
                    eco=float(input("enter bowler's economy :"))
                from scipy.stats import *
                result=bernoulli.rvs(p,size=1)
                print("out =",result)
                import random
                if result==0:
                    p=p-0.0005
                    if n%2==0:                
                        if sr<100:
                            weights=[0.45,0.35,0.15,0.05,0,0]     
                        elif 100<=sr<110:
                            weights=[0.4,0.4,0.1,0.05,0.05,0]
                        elif 110<=sr<120:
                            weights=[0.35,0.3,0.15,0.05,0.1,0.05]
                        elif 120<=sr<130:
                            weights=[0.3,0.25,0.2,0.05,0.1,0.1]
                        elif 130<=sr<140:
                            weights=[0.25,0.25,0.2,0.05,0.15,0.1]
                        elif 140<=sr<150:
                            weights=[0.2,0.2,0.2,0.05,0.2,0.15]
                        elif 150<=sr<165:
                            weights=[0.1,0.15,0.25,0.1,0.2,0.2]
                        else :
                            weights=[0.1,0.15,0.2,0.05,0.3,0.2]
                        run = random.choices(runs, weights=weights)    
                        print("runs scored on",n," th ball",run)
                        list1.append(run)
                        bowler.append(run)
                    else:
                        if eco<=5:
                            p=p+0.1
                            weights=[0.45,0.38,0.12,0.05,0,0]
                        if 5<eco<=6:
                            p=p+0.05
                            weights=[0.41,0.34,0.17,0.06,0.02,0]                       
                        elif 6<eco<=7:
                            p+0.025
                            weights=[0.4,0.3,0.15,0.05,0.07,0.03]
                        elif 7<eco<=8.5:
                            weights=[0.34,0.29,0.15,0.05,0.1,0.07]
                        elif 8.5<eco<=9.3:
                            weights=[0.25,0.2,0.25,0.05,0.15,0.1]
                        elif 9.3<eco<=10:
                            weights=[0.2,0.2,0.25,0.05,0.15,0.15]                       
                        elif 10<eco<=11:
                            weights=[0.17,0.2,0.23,0.05,0.2,0.15]
                        else:
                            weights=[0.1,0.2,0.25,0.05,0.2,0.2]
                        run = random.choices(runs, weights=weights)     
                        print("runs scored for",n," th ball",run)
                        list1.append(run)
                        bowler.append(run)
                    a=sum(list1,[])
                    g=sum(bowler,[])
                    if n%6==0:
                        print("this bowler gave ",sum(g),"amount of runs")
                        bowler.clear()
                    n=n+1
                    ball.append(n)            
                    if n==120 :
                        print("innings finish ")
                        break
                else :
                    print("player out at",n,"th ball")            
                    run=random.choices(runs,weights=[0.55,0.4,0.05,0,0,0])
                    list1.append(run)
                    bowler.append(run)
                    a=sum(list1,[])
                    print("runs scored on ",n," th ball",run)
                    g=sum(bowler,[])
                    if n%6==0:
                        print("this bowler gave ",sum(g),"amount of runs")
                        bowler.clear()
                    n=n+1
                    ball.append(n)
                    break
            break  
        ball_wicket.append(n)
        a=sum(list1,[])
        print("runs scored on each ball",a)
        b=sum(a)
        f=sum(g)    
        print("batsman scored : ",b," runs in ",len(a)," balls")
        main.append(b)
d=sum(main)
c=sum(a)
print("Number of runs scored by every batsman ",main)
print("total runs  ",max(d,c))
print("total number of balls ",n)       
print("wickets at ball is ",ball_wicket)


# In[ ]:




