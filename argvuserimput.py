#! /usr/bin/env python3
import math
import sys
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
def main():
    print('##', datetime.now().replace(microsecond=0).isoformat())
    dt = float(sys.argv[1])
    N0B = float(sys.argv[2])
    N0W = float(sys.argv[3])
    Prey_Growth_Rate = float(sys.argv[4])
    Prey_Side_Interaction_Rate = float(sys.argv[5])
    Predator_Side_Interaction_Rate = float(sys.argv[6])
    Predator_Death_Rate = float(sys.argv[7])
    NGen = int(sys.argv[8])
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

