import math
def main():
    dt = 0.001
    N0 = 2
    Growth_Rate = 0.20
    NGen = 50000
    N_Previous = N0
    for i in range(NGen):
        dN = Growth_Rate * N_Previous * dt
        N_New = N_Previous + dN
        print(N_New)
        N_Previous = N_New
main()
#successful graphing of a single species exp growth model##
