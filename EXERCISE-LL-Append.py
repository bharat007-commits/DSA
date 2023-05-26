class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    ## Printing the list 
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    ## making an empty linked list        
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    ## appending at the end    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1 
        return True
    
    ## poping the element at the end of the linked list
    def pop_optimatl(self):
        if self.length ==0:
            return None
        temp =self.head 
        pre =self.head
        while temp.next is not None:
            pre =temp
            temp =temp.next 
        self.length -=1
        self.tail =pre
        self.tail.next =None 
        if self.length ==0:
            empty_node =Node(None)
            self.head =empty_node
            self.tail =empty_node
        return True
    
    # def pop_end_ele(self):
    #     if self.length == 0:
    #         return None
    #     temp =self.head
    #     while temp.next is not None:
    #         temp =temp.next    
    #     self.length=-1
    #     self.tail = temp 
    #     self.tail.next =None 
    #     if self.length ==1:
    #         empty_node = Node(None)
    #         self.head = empty_node
    #         self.tail  = empty_node
    #     return True
    


        

    ##Prepand of the element adding element at the start of the linked list 
    def prepand(self,value):
        new_node =Node(value)
        if self.length==0:
            empty_node =Node(None)
            self.head =empty_node
            self.tail =empty_node
            
        else:
            temp =self.head 
            self.head = new_node
            self.head.next = temp
        self.length += 1
        return True
    
    ## poping out the element from the start of the linked list 
    def pop_first(self):
        if self.length ==0:
            return None   
        temp=self.head
        self.head =self.head.next
        temp.next =None ## Disconnecting the first node with rest of the linked list
        self.length -=1
        if self.length==0:
            self.tail =None
        # return True
    
    ## geting the element of particular index returning the node of that index
    def get_index(self,index):
        if index < 0 and index >= self.length:
            return None 
        else:
            temp = self.head
            for _ in range(index): # here we are not using any i because later we are not using it 
                temp=temp.next 
        return temp
    
    ## setting the value in a linked list at a particular index with  particular value 
    def set_ele(self,index,value):
             temp=self.get_index(index)
             if temp: # we can write here if temp is not none and in else temp is none
                 temp.value = value
                 return True
             return False
    
    ## inserting a new node at a given index.
    def insert(self,index,value):
        if index < 0  and index > self.length:
            return False 
        if index ==0:
            return self.prepand(value)
        if index == self.length:
            return self.append(value)
        new_node =Node(value)
        temp=self.get_index(index-1)
        pre =temp.next 
        temp.next = new_node 
        new_node.next =pre 
        self.length +=1 

    ## removing a node present at a particular index 
    def remove(self,index):
        if index < 0 and index > self.length:
            return None 
        if index ==0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop_optimatl()
        pre = self.get_index(index-1)
        temp=pre.next
        pre.next =temp.next
        temp.next =None 
        self.length -=1 
        return temp.value

    ## reversing a linked list 
    def reverse(self):
        temp =self.head
        self.head =self.tail
        self.tail = temp
        before = None 
        after =temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before =temp 
            temp = after 

        




          





my_linked_list = LinkedList(1)
# my_linked_list.make_empty()

my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
# my_linked_list.append(44)
my_linked_list.reverse()

# my_linked_list.prepand(5)
# my_linked_list.append(500)
# print(my_linked_list.pop_first())

# print(my_linked_list.set_ele(2,35))
# print(my_linked_list.pop_optimatl())
# print("temp:", my_linked_list.tail.value)
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()


