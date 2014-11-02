"""FloydWarshall completed  by Timothy McRoy. 
This program performs the FloydWarshall Algorithm to solve the all-pairs shortest path problem.
The random module is used to generate a graph based on a specific seed.

"""



from graph import Graph
def floydWarshall(G):
    # apply Warshall's alg to graph G
    kList = [k for k in G.getVertices()]
    # list of vertex keys
    n = len(kList)
    # create adjacency matrix for graph G
    mat = [None]*n
    # create n x n matrix
    for i in range(n):
        mat[i] = [None]*n    #We needed to change this from False to None, because a weight of zero is allowed for the case of a vertexes path to itself. 
    # for every i,j where there is an edge set to the appropriate weight
    for i in range(n):
        c1 = kList[i]
        nbrs = [(v.id, G.getVertex(c1).getWeight(v)) for v in G.getVertex(c1).getConnections()]
        for c2 in nbrs:
            j = kList.index(c2[0])
            mat[i][j] = c2[1]
        mat[i][i] = 0  #It is given that the shortest path from a matrix to itself is 0.
    # print out initial matrix
    for i in range(len(mat)):
        print(mat[i])
        # main loop (Warshall Algorithm)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][k] and mat[k][j] and ( mat[i][j]==None):  #Any nonzero integer is interpreted as True
                    mat[i][j] = mat[i][k] + mat[k][j]                          # We want to replace any None values with the sum, so long as the other values can be added 
                elif all([mat[i][j],mat[i][k],mat[k][j]]):                     # This line checks to see if every item is an integer.  On paper, we just say "infinity" instead of None. 
                    mat[i][j] = min(mat[i][j] , (mat[i][k] + mat[k][j])) 
    return kList, mat

if __name__ == "__main__":
    G = Graph()
    alphabet = 'abcdefg'
    for c in alphabet:
        G.addVertex(c)
    kList = [v for v in G.getVertices()]
    print(kList)
    n = len(kList) # number of vertices
    # create random graph with degree <=2 for each vertex
    import random
    import time
    random.seed(23472578)
    for c1 in kList:
        for i in range(2):
            c2 = kList[random.randrange(n)]
            G.addEdge(c1,c2, cost = random.randint(1,10))   #Small change here
    # printing the original graph just created
    for c1 in kList:
        print('Vertex:',c1,'AdjList:', [(v.id+ "->" + str(G.getVertex(c1).getWeight(v))) for v in G.getVertex(c1).getConnections()])   # I changed this line as well, since we want to know what the weights were beforehand
    wList,mat = floydWarshall(G)
    # printing vertices and matrix for graph after Warshall
    print('wList =',wList)
    for i in range(len(mat)):
        print(mat[i])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    