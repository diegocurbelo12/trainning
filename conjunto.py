# This class define SET type.
class Conjunto:
       
    def __init__(self):
        self.setValues = [];

    def __sub__(self, setA):
        set_diference = Conjunto();
        for x in self.setValues:
            if x not in setA.setValues:
                set_diference.add(x);
                
        return set_diference;

    def __mul__(A, B):
        list = [];
        for a in A.setValues :
            for b in B.setValues:
                list.append((a,b));
        return list;            

    def __contains__(t, self):
        for x in self.setValues:
            print(x)
            if x not in t.setValues:             
                return False;
            
        return True;

    # adds the element x, if it is not present already.
    def add(self, x):
        if x not in self.setValues:
            self.setValues.append(x);
        
    # removes the element x from S, if it is present.
    def remove(self, x):
        self.setValues.remove(x);

    #returns the intersection of sets S and T.
    def intersection(self,t):
        intersecctionSet = Conjunto();
        for x in self.setValues:            
            if x in self.setValues and x in t.setValues:
                intersecctionSet.add(x);
        return intersecctionSet;

    def union(self, t):
        conjuntoUnion = self;
        for x in t.setValues:
            conjuntoUnion.add(x);
        return conjuntoUnion;

    def diferenciaSimetrica(self, t):
        difSimetrica = (self - t).union(t-self);
        return difSimetrica;
    
    def show(self, printObject):
        for x in self.setValues:
            printObject(x);
