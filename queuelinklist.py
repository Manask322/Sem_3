class Node:    
    def __init__(self,data=None,nxt=None):
        self.data=data;
        self.nxt=nxt;

class Queue:
    def __init__(self):
        self.head=Node()
        self.front=None
        self.rear=None
        self.size=0

    def enque(self,x):
        temp=Node(x,None)
        if(self.head.nxt==None):
            self.head.nxt=temp
            self.front=temp
            self.rear=temp
        else:
            self.rear.nxt=temp
            self.rear=temp
        self.size+=1

    def deque(self):
        if (self.head.nxt==None):
            print ("Empty Queue")
            
        else:            
            k=self.head.nxt
            self.front=self.head.nxt.nxt
            self.head.nxt=self.head.nxt.nxt
            self.size=self.size-1
            return k
        self.size=self.size-1
    def qprint(self):
        while(self.head.nxt!=None):
            print(self.head.nxt.data)
            self.head.nxt=self.head.nxt.nxt
        
     


def main():
    q=Queue()
    q.enque(2)
    q.enque(3)
    q.enque(5)
    print("size is:")
    print(q.size)
    print("elements are:")
    q.qprint()
if __name__ == '__main__':
    main()
