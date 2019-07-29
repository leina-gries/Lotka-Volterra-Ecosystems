#! /usr/bin/env python3


def main():
    
    import math
    A = input("starting population?")
    int_A = int(A)
    print(int_A)

    for i in range(20):
        y = pow(int_A, i)
        print(i, ';', y)

main()
