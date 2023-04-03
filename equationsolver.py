#(-b +/- sqrt(b^2 - 4ac))/ 2a
import matplotlib.pyplot as plt
import numpy as np
import time
import os
from subprocess import call 
  
def clear(): 
    x = call('clear' if os.name =='posix' else 'cls') 

CRED = '\033[91m'
CGREEN  = '\33[32m'
CBLUE   = '\33[34m'
CEND = '\033[0m'

x1_up=0
x2_up=0

def mitternachts_formel(a,b,c):
    x1 = ((-b) + (b**2-(4*a*c))**(1/2))/2*a
    x2 = ((-b) - (b**2-(4*a*c))**(1/2))/2*a
    discriminant = b**2-(4*a*c)
    if b**2-(4*a*c) < 0:
        print("No Zeros on X Axis, because discriminant", discriminant,"is negative.")
        return ""
        
    x1_up = int(x1)
    x2_up = int(x2)
    return "Zeros on X Axis || x1: {} and x2: {}".format(x1,x2)

def vertex_formel(a,b,c):
    #Notizen zum Nachdenken 
    #(a/a*x**2 + b/a*x + (b/2)**2) + (c - ((b/2)**2))
    #(a + b)² = a² + 2ab + b²
    #(a/a + ((b/2)**2))**2)
    return 0

def main_func():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    clear()

    vortex_a = (a/a)
    vortex_b = (b/2)
    vortex_c = (c - (a*((b/2)**2)))

    vortex_a_1 = (a/a)
    vortex_b_1 = (b/2)/a
    vortex_c_1 = (c - (a*((b/2)**2)))/a

    #
    print("{}Standard Form: y = +({})x² +({})x +({}){}".format(CRED,a,b,c,CEND))
    
    
    if a == 1:
        print("{}Vertex Form: y = (x +({}))² +({}){}".format(CRED,vortex_b,vortex_c,CEND))
        
    else:
        print("{}Vertex Form: y = (x +({}))² +({}){}".format(CRED,vortex_b_1,vortex_c_1,CEND))
       
        

    print("{}Vertex/Scheitelpunkt: V(-({}) | +({})){}".format(CGREEN,vortex_b,vortex_c,CEND))
    
    print("{}MIN/MAX(a<0 = min / a>0 = max): {}{}".format(CGREEN,vortex_c,CEND))
    

    print("{}{}{}".format(CBLUE,mitternachts_formel(a, b, c),CEND))
  
        
    x = np.linspace(-10, 10, 1000)
    y = (a)*x**2 + (b)*x + (c)
    plt.grid()
    fig, ax = plt.subplots()
    ax.set_ylim(bottom=-30)
    ax.set_ylim(top=30)
    ax.yaxis.grid(True)
    ax.xaxis.grid(True)
    ax.ticklabel_format(useOffset=False)
    plt.plot(x, y, "g")
  
    timestr = time.strftime("%Y%m%d-%H%M%S")
    plt.savefig('{}.png'.format(timestr))
    print("Graph was created: ",'{}.png'.format(timestr))
    print("")


main_func()






