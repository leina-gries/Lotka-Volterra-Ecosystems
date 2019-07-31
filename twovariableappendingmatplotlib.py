#! /usr/bin/env python3
import math
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
import matplotlib.pyplot as plt
def main():
    print('##', datetime.now().replace(microsecond=0).isoformat())
    dt = 0.01
    N0B = 2
    N0W = 2
    #Prey_Growth_Rate = 5
    Prey_Side_Interaction_Rate = 0.015
    #Predator_Side_Interaction_Rate = 0.5
    Predator_Death_Rate = 0.5
    NGen = 4500
    NB_Previous = N0B
    NW_Previous = N0W
    Prey_Var_Range = 100
    Predator_Var_Range = 100
    print('#from variables:', 'dt=', dt, 'NOB=', N0B, 'NOW=', N0W, 'Prey-side interactionrate=',  Prey_Side_Interaction_Rate, 'Predator death rate',  Predator_Death_Rate, 'NGen =', NGen, 'range of prey growth rate=', Prey_Var_Range)

    x1_data_list = []
    y1_data_list = []
    x2_data_list = []
    y2_data_list = []
    x3_data_list = []
    y3_data_list = []
   # color_list = []
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
                    x1_data_list.append((Prey_Growth_Rate))
                    y1_data_list.append((Predator_Side_Interaction_Rate))
                    #color_list.append('1')
                    #print(Prey_Growth_Rate, Predator_Side_Interaction_Rate, '0.1')
                   # plt.scatter(Prey_Growth_Rate, Predator_Side_Interaction_Rate)
                    break
                else:
                    NB_Previous = NB_New
                if NW_Previous <= 0:
                    NW_New = 0
                    x2_data_list.append((Prey_Growth_Rate))
                    y2_data_list.append((Predator_Side_Interaction_Rate))
                    color_list.append('2')
                    #print(Prey_Growth_Rate, Predator_Side_Interaction_Rate, '0.15')
                    #plt.scatter(Prey_Growth_Rate, Predator_Side_Interaction_Rate)
                    break
                else:
                    NW_Previous = NW_New
                if z+1 == NGen:
                    x3_data_list.append((Prey_Growth_Rate))
                    y3_data_list.append((Predator_Side_Interaction_Rate))
                    #color_list.append('3')
                   # print(Prey_Growth_Rate,  Predator_Side_Interaction_Rate, '0.2')
                    #plt.scatter(Prey_Growth_Rate, Predator_Side_Interaction_Rate)
                    break
            NB_Previous = N0B
            NW_Previous = N0W
    plt.scatter(x1_data_list, y1_data_list, color = 'red')
    plt.scatter(x2_data_list, y2_data_list, color = 'yellow')
    plt.scatter(x3_data_list, y3_data_list, color = 'green')
 #   for suffix in ('png', 'pdf', 'svg'):
    plot_fname = 'twovar_output_%f_%f.png' % (Predator_Death_Rate, Prey_Side_Interaction_Rate)
    #+suffix
    plt.savefig(plot_fname)
    plt.show()
main()

