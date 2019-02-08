#Author: Andres Nava
#LDOM:2-7-19
#Course:CS 2302 Data Structures
#Lab 1
#TA:Anindita Nath
#Purpose: The purpose of this code is to make a main circle with 5 circle in the main circle and to keep doing that
#for as many layers as needed.
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
        
        centerLeft = [(center[0] -(2 * (radius / w))), center[1]]     #sets coords for left side circle and shrinks it by a third
        centerRight = [(center[0] + (2 * (radius / w))), center[1]]   #sets coords for right side circle and shrinks it by a third
        centerTop = [center[0], (center[1] + (2 * (radius / w)))]     #sets coords for top side circle and shrinks it by a third
        centerBottom = [center[0], (center[1] - (2 * (radius / w)))]  #sets coords for bottom side circle and shrinks it by a third
        
        x,y = circle(center,radius) 
        
        ax.plot(x,y,color='k') 
        
        draw_circles(ax, n - 1, center, radius / w,w)                 #makes main circle
        draw_circles(ax, n - 1, centerLeft, radius / w,w)             #makes left circle 
        draw_circles(ax, n - 1, centerRight, radius / w,w)            #makes right circle  
        draw_circles(ax, n - 1, centerTop, radius / w,w)              #makes top circle  
        draw_circles(ax, n - 1, centerBottom, radius / w,w)           #makes bottom circle          
        
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 2, [50,0], 100,3)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')


