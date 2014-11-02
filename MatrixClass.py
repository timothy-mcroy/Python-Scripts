class Matrix:
    def __init__(self):
        self.data = []
    def product(self, B):
        assert type(B)==type(self) , "B is not a Matrix"
        assert len(self.data)>0 and len(B.data)>0, "Matrix is empty"
        assert len(self.data[0]) == len(B.data), "Matrices are not MxN and NxP"
        result = Matrix()
        A=self.data
        B=B.data
        result.set_data([[ 
    sum(x*y for x,y in zip(A[m], [i[p] for i in B]))
    
    for p in range(len(B[0]))
    ] for m in range(len(A))
 ])
        return result
    def add(self, B):
        """A.sum(B) returns matrix A+B"""
        assert type(B)==type(self) , "B is not a Matrix"
        assert len(self.data)>0 and len(B.data)>0, "Matrix is empty"
        assert len(self.data[0]) == len(B.data[0]) and len(self.data)==len(B.data), "Matrices are not same size"
        result=Matrix()
        for m in range(len(self.data)):
            row =[]
            for n in range(len(B.data)):
                row.append(self.data[m][n] +B.data[m][n])
            result.data.append(row)
        return result
    def difference(self, B):
        """A.difference(B) returns matrix A-B"""
        assert type(B)==type(self) , "B is not a Matrix"
        assert len(self.data)>0 and len(B.data)>0, "Matrix is empty"
        assert len(self.data[0]) == len(B.data[0]) and len(self.data)==len(B.data), "Matrices are not same size"
        result=Matrix()
        for m in range(len(self.data)):
            row =[]
            for n in range(len(B.data)):
                row.append(self.data[m][n] -B.data[m][n])
            result.data.append(row)
        return result
    
    
        



    
    def set_data(self,g):
        self.data=g
        
             
if __name__ =="__main__":  
    A=Matrix()
    A.set_data([[1,2,3],[2,4,5],[3,5,6]])
    B=Matrix()
    B.set_data([[5,0,0],[0,3,0],[0,0,2]])
         
             
