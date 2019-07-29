import math

def main():
    dt = 0.001
    N0B = 20
    N0W = 2
    Prey_Growth_Rate = 2
    Prey_Side_Interaction_Rate = 0.3
    Predator_Side_Interaction_Rate = 0.5
    Predator_Death_Rate = 0.8
    NGen = 100
    NB_Previous = N0B
    NW_Previous = N0W

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

