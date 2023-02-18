
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import ast
import csv


def main():
    f = open('matrix.txt', 'r')
    final_list = []
    for line in f:
        list = [float(num) for num in line.split(' ')]
        final_list.append(list)

    matrix = np.matrix(final_list)
    G = nx.from_numpy_matrix(matrix)

    #result = nx.pagerank(G) #ahamaiyat

    #churn dar allx:
    lines = np.genfromtxt("userchurn1.csv", delimiter=",", dtype=None)
    my_dict = dict()
    for i in range(len(lines)):
        my_dict[lines[i][0]] = lines[i][1]

    allxx = str(my_dict)
    allx = allxx[0:1]+' '+allxx[1:]
    #allx = "{ 0:0, 1:1, 2:0, 3:1, 4:0, 5:1, 6:0}"


    for x in range(1, 3):
        f = str(x)+': 0'
        p = ' '+ str(x)+ ':'
        posfirst = allx.index(p)
        posfirst = posfirst+1
        possec= allx.index(',' , posfirst)
        allx2 = allx[0:posfirst] + f + allx[possec:]
        print (allx2)
        result2 = nx.pagerank(G,personalization= ast.literal_eval(allx2))

        print(str(x) +':'+str(result2[x]))


        #sabr dar db result2[x]
        #with open('people1.csv', 'a') as csvFile:
       #     writer = csv.writer(csvFile)
        #    writer.writerow(result2[x])
      #  csvFile.close()




    G2 = nx.DiGraph()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, )
    #view graph(
    plt.show()


if __name__ == '__main__':
    main()
