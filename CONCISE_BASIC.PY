#! /usr/bin/env python3
import math
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
def main():
    print(datetime.now().replace(microsecond=0).isoformat())
    dt = 0.001
    N0B = 20
    N0W = 2
    Prey_Growth_Rate = 2.1
    Prey_Side_Interaction_Rate = 0.5
    Predator_Side_Interaction_Rate = 0.7
    Predator_Death_Rate = 1.0
    NGen = 10
    NB_Previous = N0B
    NW_Previous = N0W
    print('#from variables:', 'dt=', dt, 'NOB=', N0B, 'NOW=', N0W, 'Prey-side interactionrate=',  Prey_Side_Interaction_Rate, 'Predator-side interaction rate=', Predator_Side_Interaction_Rate, 'Predator death rate',  Predator_Death_Rate, 'NGen =', NGen)


    for i in range(NGen):
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
        print(NB_New,NW_New)
        if NW_New  == 0 and NB_New == 0:
            break
main()

