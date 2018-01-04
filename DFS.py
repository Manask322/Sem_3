import sys

class List_Node :
    def __init__(self,data=None,nxt=None) :
        self.data = data
        self.nxt = []
        self.color = 'white'
        self.start = None 
        self.end = None 
        self.pre = None

class DFS_in_Graph :
    def __init__(self,index) :
        self.time = 1 
        self.n=index
        self.List=[ List_Node(i) for i in range(index) ]
        
    def Assign_Values(self) :
        print("enter the edges (enter -1 as edges to interrupt) :") 
        a,b = map(int,sys.stdin.readline().split())
        while a is not -1 :
            self.List[a].nxt.append(self.List[b])
            self.List[a].data=a
            self.List[b].nxt.append(self.List[a])
            self.List[b].data=b
            a,b = map(int,sys.stdin.readline().split())

    def DFS(self,source) :
        self.List[source].color = 'grey'
        self.List[source].start = self.time
        self.time += 1
        for i in range(len(self.List[source].nxt)) :
            if self.List[source].nxt[i].color == 'white' :
                self.List[source].nxt[i].pre = self.List[source]
                self.DFS(self.List[source].nxt[i].data)
                # self.List[source].nxt[i].pre = self.List[source]
            else :
                if self.List[source].pre != self.List[source].nxt[i] :
                    y = self.List[source]
                    while y != self.List[source].nxt[i] :
                        print(y.data)
                        y = y.pre
                    break
        self.List[source].color = 'black'
        self.List[source].end = self.time
        self.time += 1
    def Print_Graph(self,n) :
        for i in range(n) :
            print(" Node :{} , [{},{}]".format(self.List[i].data,self.List[i].start,self.List[i].end)) 

def main() :
    print("number of Nodes :",end = " ")
    num = int(input())
    D = DFS_in_Graph(num)
    D.Assign_Values()
    D.DFS(0)
    D.Print_Graph(num)

if __name__ == '__main__':
    main()

