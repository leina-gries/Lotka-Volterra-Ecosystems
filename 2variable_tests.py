#! /usr/bin/env python3
import math
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
def main():
    print('##', datetime.now().replace(microsecond=0).isoformat())
    dt = 0.01
    N0B = 20
    N0W = 2
    #Prey_Growth_Rate = 5
    Prey_Side_Interaction_Rate = 0.015
    #Predator_Side_Interaction_Rate = 0.5
    Predator_Death_Rate = 0.5
    NGen = 4500
    NB_Previous = N0B
    NW_Previous = N0W
    Prey_Var_Range = 1000
    Predator_Var_Range = 1000
    print('#from variables:', 'dt=', dt, 'NOB=', N0B, 'NOW=', N0W, 'Prey-side interactionrate=',  Prey_Side_Interaction_Rate, 'Predator death rate',  Predator_Death_Rate, 'NGen =', NGen, 'range of prey growth rate=', Prey_Var_Range)

    
    for i in range(Prey_Var_Range):
        Prey_Growth_Rate = (i+1)/100
        for n in range(Predator_Var_Range):
            Predator_Side_Interaction_Rate = (n+1)/100
            for z in range(NGen):
                dNB =(Prey_Growth_Rate * NB_Previous * dt) - (Prey_Side_Interaction_Rate * NB_Previous * NW_Previous * dt)
                NB_New = NB_Previous + dNB
                dNW = (Predator_Side_Interaction_Rate * NB_Previous * NW_Previous* dt) - (Predator_Death_Rate * NW_Previous * dt)
                NW_New = NW_Previous + dNW
                if NB_Previous <= 0:
                    NB_New = 0
                    print(Prey_Growth_Rate, Predator_Side_Interaction_Rate, '1')
                    break
                else:
                    NB_Previous = NB_New
                if NW_Previous <= 0:
                    NW_New = 0
                    print(Prey_Growth_Rate, Predator_Side_Interaction_Rate, '2')
                    break
                else:
                    NW_Previous = NW_New
                if z+1 == NGen:
                    print(Prey_Growth_Rate,  Predator_Side_Interaction_Rate, '3')
                    break
            NB_Previous = N0B
            NW_Previous = N0W
    

main()

