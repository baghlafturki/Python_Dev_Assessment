class Node:
    '''
    Node class to be used by LinkedList to store data and link reference to
    other nodes
    '''
    def __init__(self,data=None):
        self.data = data
        self.next = None


class Iterator:
    '''
    To be used to iterate values of nodes in LinkedList class
    '''
    
    def __init__(self, current_node):
        self.node = current_node

    def __next__(self):
        # function to find the next node's value

        # if there is a linked node
        if self.node != None:
            # get data
            data = self.node.data
            # record the reference to the next node
            self.node = self.node.next

            # retrn the data
            return data
        else:
            # if nothing is linked to the current node
            raise StopIteration

    def __iter__(self):
        return self


class LinkedList:
    '''
    Main class of the single linked list implementation
    the first node holds info about the length of the linked list
    and a reference to other nodes
    '''
    def __init__(self):
        # initialize head node to hold the number of linked nodes and
        # a reference of the next linked node
        self.head = Node(0)

    def add(self, data):
        # getting the head of the linked list
        pointer = self.head

        # traverse the linked list till the tail
        while pointer.next != None:
            pointer = pointer.next
        # add the new node to the tail
        pointer.next = Node(data)
        # increase the length
        self.head.data += 1

    def __len__(self):
        # return the current length of the linked list
        return self.head.data

    def __iter__(self):
        # use Iterator class implemented to iterate the values
        # of the nodes within the linked list except the first node
        # Note: first node only holds info about length and reference
        return Iterator(self.head.next)




        
def countPairs(N1, N2, x):
    '''
    Main function to find the number of pairs from N1 and N2 which sum
    equals to x
    '''
    n_pairs = 0

    
    # iterate each value in first linked list
    for n1_num in N1:

        # iterate each value in second linked list
        for n2_num in N2:

            # increment by 1 if the pair sums to x
            n_pairs = n_pairs+1 if n1_num+n2_num == x else n_pairs
            
    return n_pairs

    

L1, L2, x= LinkedList(), LinkedList(), 10

for i in [7,5,1,3]:
    L1.add(i)

for i in [3,5,2,8]:
    L2.add(i)

print(countPairs(L1, L2, x))


