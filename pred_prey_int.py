def main():
    import math
#terms and coefficients#
dt = 0.001
#^change in time#
N0 = 2
#^original population#
Growth_Rate = 0.20
NGen = 50000
N_Previous = N0
for i in range(NGen):
    dN = Growth_Rate * N_Previous * dt
    N_New = N_Previous + dN
    print(N_New)
    N_Previous = N_New
#successful graphing of a single species exp growth model##
##editing editing wiorkkkkkk#####
