import math
def main():
    dt = input('dt? must be a decimal. suggested: 0.001     ')
    dt = float(dt)
    N0B = input('starting population of prey? integer value only. suggested: 2      ')
    N0B = int(N0B)
    N0W = input('starting population of predators? integer value only. suggested: 2     ')
    N0W = int(N0W)
    Prey_Growth_Rate = input('prey growth rate? suggested: 5.0. Must include a decimal value.     ')
    Prey_Growth_Rate = float(Prey_Growth_Rate)
    Prey_Side_Interaction_Rate = input('Rate of interaction: prey with predators: Suggested: 0.3. Must include decimal value.      ')
    Prey_Side_Interaction_Rate = float(Prey_Side_Interaction_Rate)
    Predator_Side_Interaction_Rate = input('Rate of interaction: predators with prey. Suggested:0.5. Must include decimal value!     ')
    Predator_Side_Interaction_Rate = float(Predator_Side_Interaction_Rate)
    Predator_Death_Rate = input('predator death rate? suggested: 0.8. Must include a decimal value.     ')
    Predator_Death_Rate = float(Predator_Death_Rate)
    NGen = input('how many generations? integer value')
    NGen = int(NGen)
    NB_Previous = N0B
    NW_Previous = N0W

    for i in range(NGen):
        dNB =(Prey_Growth_Rate * NB_Previous * dt) - (Prey_Side_Interaction_Rate * NB_Previous * NW_Previous * dt)
        NB_New = NB_Previous + dNB
        #NB_Previous = NB_New
        dNW = (Predator_Side_Interaction_Rate * NB_Previous * NW_Previous* dt) - (Predator_Death_Rate * NW_Previous * dt)
        NW_New = NW_Previous + dNW
        # NB_Previous = NB_New
        # NW_Previous = NW_New
        #rint(        NB_New     ,        NW_New)
        if NB_Previous <= 0:
            NB_New = 0
        else:
            NB_Previous = NB_New
        if NW_Previous <= 0:
            NW_New = 0
        else:
            NW_Previous = NW_New    
        print(        NB_New     ,        NW_New)
        if NW_New      == 0 and NB_New      == 0:
            break
                
   #print(NW_New)
main()

