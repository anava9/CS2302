#Author: Andres Nava
#LDOM:2-7-19
#Course:CS 2302 Data Structures
#Lab 1
#TA:Anindita Nath
#Purpose: The purpose of this code is to make a circle with more circles in it but they are all to the left.

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x+radius,y,color='k') #this moves it to the left 
        
        draw_circles(ax,n-1,center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 20, [200,0], 50,.7)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')

