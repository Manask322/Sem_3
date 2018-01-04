class MaxHeap(object):
	"""docstring for MaxHeap"""
	def __init__(self):
		self.array=[ None for i in range(1)]
		self.size=0
	def increment(self,i):
		i=i+1
	def insert(self,x):
		self.array.append(x)
		self.size=self.size+1
		i=self.size
		while i > 0 :
			if int(i/2) > 0 :
				if self.array[int(i/2)] < self.array[i] :
					temp=self.array[int(i/2)]
					self.array[int(i/2)]=self.array[i]
					self.array[i]=temp
			i=int(i/2)
	def maximum():
		return array[0]
	def Swap(self,i):
		temp=self.array[i]
		self.array[i]=self.array[2*i]
		self.array[2*i] = temp
	def Swap1(self,i):
		temp=self.array[i]
		self.array[i]=self.array[2*i + 1]
		self.array[ 2*i +1 ]=temp
	def heapify(self,i):
		if i == 0 :
			self.increment(i)
		if 2*i <= self.size and 2*i+1 <= self.size :
			while (2*i + 1) <= self.size  :
				if self.array[2*i] >= self.array[i] or self.array[2*i + 1] >= self.array[i] :
					if i <= self.size :
						if self.array[2*i] > self.array[2*i + 1] :
							if self.array[2*i] > self.array[i] :
								self.Swap(i)
								i = 2*i
						else :
							if self.array[2*i + 1] > self.array[i] :
								self.Swap1(i)
								i = 2*i + 1
				else :
					break
		if 2*i <= self.size and 2*i+1 > self.size :
			self.Swap(i)

	def buildHeap(self):
		for i in range(int(self.size/2),0,-1):
			self.heapify(i)
	def ExtractMax(self):
		n=self.size
		temp=self.array[n]
		self.array[n]=self.array[1]
		self.array[1]=temp
		k=self.array[n]
		self.size-=1
		self.heapify(1)
		return k
	def PrintArray(self):
		for i in range (1,self.size+1):
			print(self.array[i],end=" "),
	def Sort(self) :
		n=self.size
		for i in range(1,self.size+1) :
			print(self.ExtractMax(),end = ' ')
		print(" 	")
	def update(self,x,a) :
		i = 1
		while self.array[i] != x :
			i = i + 1
		self.array[i] = a
		while i > 0 :
			if int(i/2) > 0:
				if self.array[int(i/2)] < self.array[i] :
					self.array[int(i/2)],self.array[i] = self.array[i],self.array[int(i/2)]
			i = int(i/2)
def main():
	H=MaxHeap()
	H.insert(8)
	H.insert(2)
	H.insert(7)
	H.insert(6)
	H.insert(0)
	H.update(2,1)
	H.Sort()
# 	H.PrintArray()
# 	print(" ")
# 	print(H.ExtractMax())
# 	print(" ")
# #	H.buildHeap()
# 	H.PrintArray()
# 	print(" ")
# 	print(H.ExtractMax())
# 	H.PrintArray()
if __name__ == '__main__':
	main()

			

			

