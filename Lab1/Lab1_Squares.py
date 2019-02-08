#Author: Andres Nava
#LDOM:2-7-19
#Course:CS 2302 Data Structures
#Lab 1
#TA:Anindita Nath
#Purpose: The purpose of this program is to make a main square and then make 
#square that have the center of it on each of the conrners and this has to work for any amount of 
#layers that is inputed.



import numpy as np
import matplotlib.pyplot as plt
 

def draw_squares(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]
        q1 =(p[i1]*(1-w)) - (orig_size/4)               #this makes the another square 1/4 of the size and 
                                                        #moves it to the bottom left       
        q2 =(p[i1]*(1-w)) + (orig_size/2) + orig_size/4 
                                                        #this does the same as the frst but moves it to the top right        
        q3=p[i1]
        q3[i1,0]= q3[i1,0] + orig_size + orig_size/2
        q3[i1,1]= q3[i1,1] - orig_size/2                #this does the same as the frst but moves it to the bottom right
        q3 = q3[i1]*(1-w) 
        
        q4=p[i1]
        q4[i1,1]= q4[i1,1] + orig_size * 2 - orig_size/2
        q4[i1,0]= q4[i1,0] - orig_size /2               #this does the same as the frst but moves it to the bottom left
        q4 = q4[i1]*(1-w)
        
        ax.plot(p[:,0],p[:,1],color='k')
        
        draw_squares(ax,n-1,q1,w)
        draw_squares(ax,n-1,q2,w)
        draw_squares(ax,n-1,q3,w)
        draw_squares(ax,n-1,q4,w)

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,2,p,.5)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')


