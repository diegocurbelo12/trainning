from collections.abc import Sequence
class Matriz(Sequence):
    M = [[]]
    def __init__(self, m, n):
        self.m =m;
        self.n = n;
        self.M = [[0]*n for x in range(m)]
       
    def __getDimension(self):
        return (self.m, self.n);

    def __add__(self, B):
        if(self.__getDimension() != B.__getDimension()):
            raise Exception("invalid dimensions");
        value = Matriz(self.m, self.n);
        for x in range(self.m):
            row = [sum(e) for e in zip(self[x], B[x])]
            value[x] = row;
        return value;



    def __mul__(self, a):
        if(isinstance(a,int)):
            return self.__mulScalar(a);
        else:
            return self.__mulMatrix(a);
           
    def __mulScalar(self, a):
        newMatrix = Matriz(self.m, self.n);
        for x in range(self.m):
            row = [e*a for e in self[x]]
            newMatrix[x] = row;
        return newMatrix;

    def transpuesta(self):
        newMatrix = Matriz(self.n, self.m);
        r =  [list(x) for x in zip(*self.M)]
        newMatrix.M = r;
        return newMatrix;
            
        
    def __mulMatrix(self, A):
        dim_A = A.__getDimension();
        if(self.n != A.m):
            raise Exception("invalid dimensions");
        
        newMatrix = Matriz(self.m, A.n);
        a_t = A.transpuesta();
        for x in range(self.m):
            for y in range(A.m):
                newMatrix[x][y] = sum([e[0]*e[1] for e in zip(self[x], a_t[y])])
        return newMatrix;

    def __iter__(self):
        return self.M;
    def __getitem__(self, i):
        return self.M[i]
    def __setitem__(self, idx, item):
        self.M[idx] = item
    def __len__(self):
        return len(self.M)

m = Matriz(3,4);
m[0][0] = 1;
m[0][1] = 2;
m[0][2] = 3;

m2 = Matriz(3,4);
m2[0][0] = 1;
m2[0][1] = 2;
m2[0][2] = 3;

m2[1][0] = 1;
m2[1][1] = 2;
m2[1][2] = 3;

suma = m + m2;


print(m.M);
print("m2");
print(m2.M);
print(suma.M);

print("Producto por escalar");
p = m*3;
print(p.M);

print("Transpuesta")
print(m.M);
m_t = m.transpuesta();
print(m_t.M);

print("Producto AxB")
A = Matriz(3,3)
B = A = Matriz(3,3)

A[0][0] = 2;
A[0][1] = 0;
A[0][2] = 1;
A[1][0] = 3;
A[1][1] = 0;
A[1][2] = 0;
A[2][0] = 5;
A[2][1] = 1;
A[2][2] = 1;

B[0][0] = 1;
B[0][1] = 0;
B[0][2] = 1;
B[1][0] = 1;
B[1][1] = 2;
B[1][2] = 1;
B[2][0] = 1;
B[2][1] = 1;
B[2][2] = 0;

print(A.M);
B_T = B.transpuesta();
print(B_T.M);

C = A*B
print(C.M);

        