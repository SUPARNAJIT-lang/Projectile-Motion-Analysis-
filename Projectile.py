#Taking input from user for the initial velocity and angle of projection

import math 
import matplotlib.pyplot as plt
import numpy as np

print("Welcome to the projectile motion simulation!")

vi=float(input("Enter the initial velocity (in m/s): "))
h=float(input("From which hight do you want to launch?"))
a=float(input("Enter the angle of projection (in degrees): "))
#Converting angle to radians
a=math.radians(a)

def pm_e(m,n,h2): #projectile motion elements

    g=9.81
    vx=m*np.cos(n)
    vy=m*np.sin(n)

    t=(vy)/g
    T=(2*t)+((math.sqrt((vy**2)+2*g*h2)-vy)/g) 
    return vx,vy,t,T,g
(vx,vy,t,T,g)=pm_e(vi,a,h)

def rp(a,b,c,d,a1,v1,g1,h1):
    r=float(a*d)
    x=np.linspace(0,r,1000)
    y=h1+(x*np.tan(a1))-((0.5*(g1)*(x**2))/((v1**2)*((np.cos(a1))**2)))
    l=(b**2)/(2*g1)
    
    H_max=h1+l
    print("The range of the projectile is:",r)
    print("The H-max of the projectile from ground is:",H_max)
    print("The Time of Flight is:",T)

    return r,l,x,y

(r,l,x,y)=rp(vx,vy,t,T,a,vi,g,h)


#Plotting the graph

u=input("Do you want to see the Trajectory? (yes/no): ")

if u=="yes":
    k=input("Enter name of the file with extension: ")
    plt.plot(x,y)
    plt.xlim(0,r+10)
    plt.ylim(0,(h+l+10))
    plt.grid(True)
    plt.savefig(k)
else:
    print("Thanks for using Projectile.py")
    

#Parameter based simulation

q=input("On what parameter you want to work on ? (time,x,y)")

if q=="time":
    t=float(input("Input the time(s): "))
    xt=int(vx*t)
    yt=int((vy*t)-(0.5*g*(t**2)))
    print(xt,yt+h)

elif q=="x":
    xt1=float(input("Input the x coordinate: "))
    yt1=h+(xt1*np.tan(a))-((0.5*(g)*(xt1**2))/((vi**2)*((np.cos(a))**2)))
    t1=xt1/vx
    print("Coordinate of the projectile is:",xt1,",",yt1)
    print("Projectile will reach to your given coordinate at t=",t1)
elif q=="y":
    yt2=float(input("Input the y coordinate: "))
    m=(g/((vi*np.cos(a))**2))
    n=np.tan(a)

    xt2_1=((n+math.sqrt((n**2)-(2*m*(yt2-h))))/m)
    xt2_2=((n-math.sqrt((n**2)-(2*m*(yt2-h))))/m)

    t2_1=xt2_1/vx
    t2_2=xt2_2/vx

    print("The x coordinate(s) of the projectile is:",xt2_1,"and",xt2_2)
    print("Projectile will reach to your given x-coordinate at t=",t2_1,"and",t2_2)

else:
    print("Invalid input")
    print("Thanks for using Projectile.py")
#End of the code        




    




    






