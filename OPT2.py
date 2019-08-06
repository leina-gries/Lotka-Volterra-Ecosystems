#! /usr/bin/env python3
import math
from array import *
from datetime import datetime
import numpy as np
from scipy.optimize import minimize, rosen, rosen_der
datetime.now().replace(microsecond=0).isoformat()
def main():
    print('#',datetime.now().replace(microsecond=0).isoformat())
    def growth(Prey_Growth_Rate):
        
 
        dt = 0.01
        N0B = 20
        N0W = 2
        Prey_Growth_Rate = Prey_Growth_Rate
        Prey_Side_Interaction_Rate = 0.015
        Predator_Side_Interaction_Rate = 0.015
        Predator_Death_Rate = 0.5
        NGen = 30
        NB_Previous = N0B
        NW_Previous = N0W
        x = []
        y = []
       # print('#from variables:', 'dt=', dt, 'NOB=', N0B, 'NOW=', N0W, 'Prey-side interactionrate=',  Prey_Side_Interaction_Rate, 'Predator-side interaction rate=', Predator_Side_Interaction_Rate, 'Predator death rate',  Predator_Death_Rate, 'NGen =', NGen)
    
        for i in range(NGen):
           # x = []
           # y = []
            #print(i)
            dNB =(Prey_Growth_Rate * NB_Previous * dt) - (Prey_Side_Interaction_Rate * NB_Previous * NW_Previous * dt)
            NB_New = NB_Previous + dNB
            dNW = (Predator_Side_Interaction_Rate * NB_Previous * NW_Previous* dt) - (Predator_Death_Rate * NW_Previous * dt)
            NW_New = NW_Previous + dNW
            if NB_Previous <= 0:
                NB_New = 0
            else:
                NB_Previous = NB_New
            if NW_Previous <= 0:
                NW_New = 0
            else:
                NW_Previous = NW_New
            x.append(float(NB_New))
            y.append(float(NW_New))
            if NW_New  == 0 and NB_New == 0:
                break
            
        return(np.array(x),np.array(y))

        
    z=growth(0.5)
    growth(0.5)
#    print(z[1])

    def compare(Prey_Growth_Rate):
        guess = (growth(Prey_Growth_Rate))
        known = (growth(0.5))
        wo=sum(abs(np.subtract(known[1], guess[1])))
        bo=sum(abs(np.subtract(known[0], guess[0])))
        add = wo + bo
        return(add)
    
    bnds = [(0, 8)]
    compare(0.5)
    #print(compare(0.5))
    x0= 1.5
    res = minimize(compare, x0, method='SLSQP', bounds=bnds, tol=1e-6)
    print(res)

main()

