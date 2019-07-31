#! /usr/bin/env python3
import math
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
def main():
    print('##', datetime.now().replace(microsecond=0).isoformat())
    dt = 0.001
    N0B = 2
    N0W = 2
    #Prey_Growth_Rate = 5
    Prey_Side_Interaction_Rate = 0.3
    Predator_Side_Interaction_Rate = 0.5
    Predator_Death_Rate = 0.8
    NGen = 87
    NB_Previous = N0B
    NW_Previous = N0W
    Var_Range = 400
    print('#from variables:', 'dt=', dt, 'NOB=', N0B, 'NOW=', N0W, 'Prey-side interactionrate=',  Prey_Side_Interaction_Rate, 'Predator-side interaction rate=', Predator_Side_Interaction_Rate, 'Predator death rate',  Predator_Death_Rate, 'NGen =', NGen, 'range of prey growth rate=', Var_Range)
    for i in range(Var_Range):
        Prey_Growth_Rate = i+1
        for z in range(NGen):
            dNB =(Prey_Growth_Rate * NB_Previous * dt) - (Prey_Side_Interaction_Rate * NB_Previous * NW_Previous * dt)
            NB_New = NB_Previous + dNB
            dNW = (Predator_Side_Interaction_Rate * NB_Previous * NW_Previous* dt) - (Predator_Death_Rate * NW_Previous * dt)
            NW_New = NW_Previous + dNW
            if NB_Previous <= 0:
                NB_New = 0
                print(Prey_Growth_Rate, z+1, '1')
                #  x = Prey_Growth_Rate
                #  y = z+1
                #  print(x, y)
                break
            else:
                NB_Previous = NB_New
            if NW_Previous <= 0:
                NW_New = 0
                print(Prey_Growth_Rate, z+1, '2')
                break
            else:
                NW_Previous = NW_New
            if z+1 == NGen:
                print(Prey_Growth_Rate, z+1, '3')
                break
        NB_Previous = N0B
        NW_Previous = N0W
    

main()

