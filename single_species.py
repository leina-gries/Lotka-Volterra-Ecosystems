#! /usr/bin/env python3
import math
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
def main():
    print(datetime.now().replace(microsecond=0).isoformat())
    dt = 0.001
    N0 = 2
    Growth_Rate = 0.20
    NGen = 50
    N_Previous = N0
    print('dt=', dt, 'N0=', N0, 'Growth Rate=', Growth_Rate, 'NGen=', NGen)
    for i in range(NGen):
        dN = Growth_Rate * N_Previous * dt
        N_New = N_Previous + dN
        print(N_New)
        N_Previous = N_New
main()
#successful graphing of a single species exp growth model##
