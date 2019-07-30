#! /usr/bin/env python3
import math
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
def main():
    print(datetime.now().replace(microsecond=0).isoformat())
    dt = 0.001
    N0B = 2
    N0W = 2
    #Prey_Growth_Rate = 5
    Prey_Side_Interaction_Rate = 0.3
    Predator_Side_Interaction_Rate = 5000
    Predator_Death_Rate = 0.8
    NGen = 100
    NB_Previous = N0B
    NW_Previous = N0W
    Var_Range = 2
    print('#from variables:', 'dt=', dt, 'NOB=', N0B, 'NOW=', N0W, 'Prey-side interactionrate=',  Prey_Side_Interaction_Rate, 'Predator-side interaction rate=', Predator_Side_Interaction_Rate, 'Predator death rate',  Predator_Death_Rate, 'NGen =', NGen, 'range of prey growth rate=', Var_Range)

    #for i in range(Var_Range):
    #    Prey_Growth_Rate = i
    #    print(Prey_Growth_Rate)
    for i in range(Var_Range):
        Prey_Growth_Rate = i+1
        print(Prey_Growth_Rate)
        for z in range(NGen):
            dNB =(Prey_Growth_Rate * NB_Previous * dt) - (Prey_Side_Interaction_Rate * NB_Previous * NW_Previous * dt)
            NB_New = NB_Previous + dNB
            dNW = (Predator_Side_Interaction_Rate * NB_Previous * NW_Previous* dt) - (Predator_Death_Rate * NW_Previous * dt)
            NW_New = NW_Previous + dNW
            if NB_Previous <= 0:
                NB_New = 0
                #          print('prey died by', z+1, i+1)
            else:
                NB_Previous = NB_New
            if NW_Previous <= 0:
                NW_New = 0
                #         print('predators died by', z+1)
            else:
                NW_Previous = NW_New
            print(Prey_Growth_Rate, NB_New,NW_New)
            if NW_New  == 0 and NB_New == 0:
                print('both species died by generation', z+1, 'using a prey growth rate of', Prey_Growth_Rate)
                break
            #  if z == NGen:
        NB_Previous = N0B
        NW_Previous = N0W
           # print('at least this works')
            #break
        
        #should reset

main()

