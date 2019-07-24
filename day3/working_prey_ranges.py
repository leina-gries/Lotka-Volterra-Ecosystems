def main():
    import math
import matplotlib.pyplot as plt
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

