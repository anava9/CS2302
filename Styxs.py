#Author: Andres Nava
#LDOM:2-7-19
#Course:CS 2302 Data Structures
#Lab 1
#TA:Anindita Nath
#Purpose: The purpose for this code is to make a tree that makes more layers on the previous end point
#without it crossing another tree.

import numpy as np
import matplotlib.pyplot as plt
 

def draw_styxs(ax,n,p):
    if n>0:
        i1 = [0,1,2]
        
        q1 = p[i1] - (orig_size)                            #makes tree on left side starting point
        q1[i1,0] = q1[i1,0] / 2
        
        q2 = p[i1]
        q2[i1,1]=(q2[i1,1] - orig_size)                     #makes tree on right side starting point
        q2[i1,0]=(q2[i1,0] + orig_size)/2 + orig_size
        
        
        ax.plot(p[:,0],p[:,1],color='k')                    #makes main tree
        
        draw_styxs(ax,n-1,q1)
        draw_styxs(ax,n-1,q2)







plt.close("all") 
orig_size = 200
p = np.array([[0,0],[orig_size,orig_size],[orig_size*2,0]])
fig, ax = plt.subplots()
draw_styxs(ax,5,p)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('styxs.png')