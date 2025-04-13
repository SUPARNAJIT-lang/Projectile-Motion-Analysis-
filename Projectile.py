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
    y1=(x*np.tan(a1))-((0.5*(g1)*(x**2))/((v1**2)*((np.cos(a1))**2)))
    y=y1+h1 

    l=(b**2)/(2*g1)

    plt.plot(x,y)
    plt.xlim(0,r+10)
    plt.ylim(0,(h1+l+10))
    plt.grid(True)
    plt.savefig("boom.pdf")
    print("The range of the projectile is:",r)
    print("The H-max of the projectile from ground is:",h1+l)
    print("The Time of Flight is:",d)
rp(vx,vy,t,T,a,vi,g,h)


