Table =[
    [0,1,0,0,1,0,1],
    [0,0,0,1,0,1,0],
    [1,0,0,"x",0,0,0],
    ["x","x",1,1,0,0,0],
    [1,1,1,"x",1,1,1]
    
    ]
print("Map is ...")
for i in Table:
    print(" ".join([str(j)for j in i]))
print("Best path is shown by ...")


def RobotCoin(Table,badValue="x"):
    """Input should be constrained to a list containing integers and one value denoted as a "badValue".
        When the program encounters badValue, it will treat that index as inaccessible.
        Assumes that all rows be the same length."""
    
    m = len(Table[0])  #Row length
    assert all([len(Table[0])==len(row) for row in Table]) #Rows must be same length
    assert all([(type(element)==int or element==badValue) for row in Table for element in row]) #Items in path should be integers or badValue
    n = len(Table)     #Column Length       
    for j in range(1,m):
        if Table[0][j-1] !=badValue and Table[0][j]!=badValue:
            Table[0][j]=Table[0][j-1]+Table[0][j]  #First row
        else:
            Table[0][j]=badValue
    for i in range(1,n):
        if Table[i][0] !=badValue and Table[i-1][0]!=badValue:
            Table[i][0]=Table[i-1][0]+Table[i][0]  #First Column
        else:
            Table[i][0] = badValue
        for  j in range(1,m):
            #Table[i-1][j] is the element to the left
            #Table[i][j-1] is the element above
            if Table[i][j] ==badValue or (Table[i-1][j] ==badValue and Table[i][j-1] == badValue): #All of the cases where badValue is placed
                Table[i][j]=badValue
            elif Table[i-1][j] ==badValue:
                Table[i][j]=Table[i][j-1] +Table[i][j]  #only option is from above
            elif Table[i][j-1] ==badValue:
                Table[i][j]=Table[i-1][j] +Table[i][j]  #Only option is from the left
            else:
                Table[i][j]=max(Table[i-1][j],Table[i][j-1]) + Table[i][j]
    return Table
for i in RobotCoin(Table):
    print(" ".join([str(j)for j in i]))
