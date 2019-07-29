import math
def main():

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

