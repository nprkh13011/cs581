# Nidhi Parekh
# I pledge my honor that I have abided by the Stevens Honor System.

# Assignment 4: Graphs
# To run from terminal window:   python3 parekh.py

"""
DESCRIPTION:
The idea of this assignment is using the data from epinions.com,
    parekh.py processes an input file and produces an undirected, signed graph, 
    and identifies all triads given a epinions-csv file.
It searches for the weights of the edges in the triangle formed by 3 nodes in the triad.
For each triad that is formed, it figures out which type of triad it is,
    given that there are four types
The program also keeps track of the number of triangles formed,
    the number of edges(positive and negative) used to identify triads,
    as well as the probability that an edge will be either positive or negative.
The expected distribution and actual distributions are also included in the program output.
"""
import csv
import time
import networkx as nx
print("\n----------------------------------------------ASSIGNMENT 4: GRAPHS---------------------------------------------------\n")

# method that processes file to identifies triads
def process_file(file):
    start_time= time.time()
    G= nx.Graph()
    count_edge = 0
    count_trust=0
    count_distrust =0
    with open(file, 'r') as f: #first step is opening and reading the file
        reader = csv.reader(f)
        for row in reader:      
            node1 = int(row[0]) #meant to be a column but did not have time to change (first column of nodes)
            node2 = int(row[1]) # second column of nodes
            G.add_node(node1)   # create nodes
            G.add_node(node2)
            if (int(row[2]) == -1):
                G.add_edge(node1, node2, weight=-1) # creates edge between 2 nodes
                count_edge += 1         #keep count on number of edges & number of distrust edges
                count_distrust +=1
            else:
                G.add_edge(node1, node2, weight=1)
                count_edge += 1         # keep count on number of edges & number of trust edges
                count_trust += 1
    
    count_triad = 0 # total number of triads formed
    TTT = 0 # TTT,TTD...
    TTD = 0
    TDD = 0
    DDD = 0
    #x is each list inside the new list that is returned when enumerating G
    for x in list(nx.enumerate_all_cliques(G)): # returns all cliques in list of lists --> [[node1, node2], [node1, node2, node3]]
        if (len(x) == 3):   #triads are length of 3 
            count_triad += 1
            weight1=G[x[0]][x[1]]["weight"]
            weight2=G[x[1]][x[2]]["weight"]
            weight3=G[x[0]][x[2]]["weight"]
            if (weight1 + weight2 + weight3 == 3): 
                TTT += 1
            elif (weight1 + weight2 + weight3 == 1):
                TTD += 1
            elif (weight1 + weight2 + weight3 == -1):
                TDD += 1
            elif (weight1 + weight2 + weight3 == -3):
                DDD += 1
    #prints all the outcomes
    print("\n*** START ***\n")
    print("triangles:", count_triad)
    print("TTT:", TTT)
    #probability of trust edge - positive/total
    print("TTD:", TTD, "             trust edges:    ", count_trust,
          "                probability %: ", "{:.2%}".format(count_trust/count_edge)) 
    #probability of distrust edge - negative/total
    print("TDD:", TDD, "             distrust edges: ", count_distrust,
          "                probability %: ", "{:.2%}".format(count_distrust/count_edge))
    print("DDD:", DDD, "             total:          ", count_edge,
          "                               ", "{:.2%}".format((count_trust/count_edge)+(count_distrust/count_edge)))
    #percent part of expect distribution - what we expect the number of triad types to be
    TTT_exp_dist = (count_trust/count_edge) * (count_trust/count_edge) * (count_trust/count_edge) * 100
    TTD_exp_dist = 3 * (count_trust/count_edge) * (count_trust/count_edge) * (count_distrust/count_edge) * 100
    TDD_exp_dist = 3 * (count_trust/count_edge) * (count_distrust/count_edge) * (count_distrust/count_edge) * 100
    DDD_exp_dist = (count_distrust/count_edge) * (count_distrust/count_edge) * (count_distrust/count_edge) * 100

    # multiply original percentage (before converting) by total number of triangles
        # ex: for TTT 35% of the total number of triangles is 9.6...
    TTT_exp_num = (count_trust/count_edge) * (count_trust/count_edge) * (count_trust/count_edge) * count_triad
    TTD_exp_num = 3 * (count_trust/count_edge) * (count_trust/count_edge) * (count_distrust/count_edge) * count_triad
    TDD_exp_num = 3 * (count_trust/count_edge) * (count_distrust/count_edge) * (count_distrust/count_edge) * count_triad
    DDD_exp_num = (count_distrust/count_edge) * (count_distrust/count_edge) * (count_distrust/count_edge) * count_triad 
    
    #percent part of actual distribution -- calculated the number into percentages
    TTT_act_dist = (TTT/count_triad) * 100
    TTD_act_dist = (TTD/count_triad) * 100
    TDD_act_dist = (TDD/count_triad) * 100
    DDD_act_dist = (DDD/count_triad) * 100

    #number part of distribution -- since its the actual number we get given the dataset
    TTT_act_num = TTT
    TTD_act_num = TTD
    TDD_act_num = TDD
    DDD_act_num = DDD

    
    #print the Expected and Actual Distribution
    print("\nExpected Distribution                Actual Distribution")
    print("       Percent " , "   Number ", "         Percent " , "         Number ")
    print(" TTT: ", "{:.2f}".format(TTT_exp_dist), "       ", "{:.2f}".format(TTT_exp_num),
          "          TTT: ", "{:.2f}".format(TTT_act_dist), "         ", TTT_act_num)
    print(" TTD: ", "{:.2f}".format(TTD_exp_dist), "      ", "{:.2f}".format(TTD_exp_num),
          "          TTD: ", "{:.2f}".format(TTD_act_dist), "          ", TTD_act_num)
    print(" TDD: ", "{:.2f}".format(TDD_exp_dist), "       ", "{:.2f}".format(TDD_exp_num),
          "          TDD: ", "{:.2f}".format(TDD_act_dist), "          ", TDD_act_num)
    print(" DDD: ", "{:.2f}".format(DDD_exp_dist), "        ", "{:.2f}".format(DDD_exp_num),
          "          DDD: ", "{:.2f}".format(DDD_act_dist), "           ", DDD_act_num)
    print(" Total: ", "{:.2f}".format(TTT_exp_dist + TTD_exp_dist + TDD_exp_dist + DDD_exp_dist), "   ",
          "{:.2f}".format(TTT_exp_num + TTD_exp_num + TDD_exp_num + DDD_exp_num),
          "         Total: ", "{:.2f}".format(TTT_act_dist + TTD_act_dist + TDD_act_dist + DDD_act_dist),
                         "        ", (TTT_act_num + TTD_act_num + TDD_act_num + DDD_act_num))
    #https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
    print("\nDuration: %s seconds " % (time.time() - start_time))
    print("\n*** END ***\n")
 
# output
def main():
    #input
    file = input("What file should I process? ")
    process_file(file)


if __name__ == "__main__":
    main()
