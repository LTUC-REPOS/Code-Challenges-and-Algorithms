class MyQueue:

    """
    Implementing a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:

    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

    """
    def __init__(self):
        self.stackPush = []
        self.stackPop = []
        self.length =0
        
    def move_values(self):
        if len(self.stackPush):
            while(len(self.stackPush)):
                val = self.stackPush.pop()
                self.stackPop.append(val)
 
    def move_back(self):
        while(len(self.stackPop) != 0):
            val = self.stackPop.pop()
            self.stackPush.append(val) 
        
        
    def push(self, x: int) -> None:
        if ( len(self.stackPop) != 0 ):
            self.move_back()
            self.stackPush.append(x)
            self.length +=1
        else:
            self.stackPush.append(x)
            self.length +=1
            
    def pop(self) -> int:
        self.move_values()
        self.length -=1         
        return self.stackPop.pop()
        
        

    def peek(self) -> int:
        self.move_values()
        return self.stackPop[self.length -1]
        

    def empty(self) -> bool:
        return self.length ==0
