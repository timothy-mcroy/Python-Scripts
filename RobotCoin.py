Table =[
    [0,1,0,0,1],
    [0,0,0,1,0],
    [1,0,0,1,0],
    [0,0,1,0,0],
    [1,0,0,0,1]
    
    ]

def F(Table):
    m = len(Table[0])  #Row length
    n = len(Table)     #Column Length
    mTable =[[0 for i in range(m)] for i in range(n)]         #Memoization Table
    mTable[0][0]=Table[0][0]
    for j in range(1,m):
        mTable[0][j]=mTable[0][j-1]+Table[0][j]  #First row
    for i in range(1,n):
        mTable[i][0]=mTable[i-1][0]+Table[i][0]  #First Column
        for  j in range(1,m):
            mTable[i][j]=max(mTable[i-1][j],mTable[i][j-1]) + Table[i][j]
            #mTable[i-1][j] is the element to the left
            #mTable[i][j-1] is the element above
    return mTable
for i in F(Table):
    print(i)

