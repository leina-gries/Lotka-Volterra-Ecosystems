# This is a set of programs designed to model predator prey interactions through the Lotka-Volterra equations. Each program represents a distinct step in the process- most are not a complete modeling program, but do serve a distinct and potentially useful purpose. 
The steps are as follows:
1. basic_exp_growth.py is a simple program that takes an input value and grows it exponentially, using the definition of the exponential function to do so.
2. single_species.py is a simple model of the growth of one species in unlimited conditions. Several variables can be edited inside the program to produce different rates of growth.
3. CONCISE_BASIC.py is the basic program that models two species growth based on the Lotka-Volterra equations. Each variable can be changed to see the impact, and the output of the program is automatically printed into the terminal.
4. user_input.py is a program that takes in input from the command line for each of the values, and gives suggested values which keep both species alive and grow their numbers consistantly.
5. VARIABLE_PREY_GROWTH.py cycles through a set number of different prey growth rates, peforming a set number of generations for each and printing key information about each growth rate, and the population of each species at each generation.
6. graphable_output_variablep.py is the same as 5, but it only prints the prey growth rate and the generation number at which the first species hit zero. It also prints a 1, 2, or 3 to signify which species' population reached 0, or if both species survived until the final generation (3).


Many of these programs produce printed output. This can be funneled into a .txt file and graphed using gnuplot. 