import sys
from queue import *

class List_Node :
	def __init__(self,data=None,nxt=None) :
		self.data=data
		self.nxt=[]
		self.color='white'
		self.dist=-1
		self.pre=None


class Graph :
	def __init__(self,index) :
		self.matrix=[ [0]*index for i in range(index) ]
		self.n=index
		self.List=[ List_Node(i) for i in range(index) ]
		self.source=0

	def Assign_Values(self) :
		print("enter the edges (enter -1 as edges to interrupt) :")	
		a,b = map(int,sys.stdin.readline().split())
		while a is not -1 :
			self.matrix[a][b]=1
			self.matrix[b][a]=1
			self.List[a].nxt.append(self.List[b])
			self.List[a].data=a
			self.List[b].nxt.append(self.List[a])
			self.List[b].data=b
			a,b = map(int,sys.stdin.readline().split())
			

	def Print_Matrix(self) :
		for i in range(self.n) :
			for j in range(self.n) :
				print(self.matrix[i][j],end=" ")
			print(" ")
	def Print_List(self) :
		for i in range(self.n) :
			print("Vertex ",i,":",end=" ")
			for j in range(len(self.List[i].nxt)) :
				print(self.List[i].nxt[j].data,end=" ")
			print(" ")
	def Adjacency_Matrix(self) :
		self.Assign_Values()
		self.Print_Matrix()
	def Adjacency_List(self) :
		self.Print_List()

	def BFG(self,s) :
		self.List[s].dist=0
		self.List[s].color='grey'
		Q=Queue()
		Q.enque(s)
		while Q.isEmpty() :
			u=Q.deque()
			print("Node: {} dist: {}".format(self.List[u].data,self.List[u].dist))
			for i in range(len(self.List[u].nxt)) :
				if ( self.List[u].nxt[i].color == 'white' ) :
					self.List[u].nxt[i].dist=self.List[u].dist + 1
					self.List[u].nxt[i].color='grey'
					self.List[u].nxt[i].pre=self.List[u]
					Q.enque(self.List[u].nxt[i].data)
			self.List[u].color='black'


#					self.List[u].


def main() :
	num=int(input("enter number of vertices :"))
	G=Graph(num)
	G.Adjacency_Matrix()
	G.Adjacency_List()
	G.BFG(1	)
if __name__ == '__main__':
	main()


