vclass TrieNode() :
	def __init__(self,data = None) :
		self.data = data
		self.child = [None for i in range(26)]
		self.end = False

class Trie() :
	def __init__(self) :
		self.root = TrieNode()

	def insert(self,word) :
		temp = self.root 
		for c in word :
			index  = ord(c) - ord('a')
			if not temp.child[index] :
		#		print(c)
				node = TrieNode(c)
				# print(node.data)
				temp.child[index] = node
			temp = temp.child[index]
		temp.end = True

	def search(self,word) :
		temp = self.root
		for c in word :
			index = ord(c) - ord('a')
		#	print(temp.child[index].data)
			if not temp.child[index] :
				return False
			temp = temp.child[index]
		return temp.end


def main():
    T = Trie()
    T.insert('manas')
    T.insert('nitk')
    T.insert('dsa')
    if T.search('mana') :
    	print("Found")
    else :
    	print("Not Found")
   

    


if __name__ == '__main__':
    main()
