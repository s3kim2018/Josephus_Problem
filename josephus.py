class Node: 
    def __init__(self, label):
        self.label = label
        self.rest = None

class Link: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.length = 0
    
    def addnode(self, label):
        instance = Node(label)
        if self.length == 0:
            self.head = instance
            self.tail = instance
            self.cursor = instance
            instance.rest = instance
        else:
            self.tail.rest = instance 
            self.tail = instance
            self.tail.rest = self.head
        self.length += 1 

    def removenode(self):
        temp = self.cursor
        if self.cursor is self.head:
            self.head = self.head.rest
            self.cursor = self.cursor.rest
            self.tail.rest = self.head 
        elif self.cursor is self.tail: 
            prev = self.head
            while prev.rest is not self.tail:
                prev = prev.rest
            self.tail = prev
            self.tail.rest = self.head 
            self.cursor = self.cursor.rest
            temp.rest = None
        else:
            prev = self.head
            while prev.rest is not temp:
                prev = prev.rest
            prev.rest = self.cursor.rest
            self.cursor = self.cursor.rest
            temp.rest = None
        self.length -= 1
        del temp 
            
joseph = []

def main(): 
    main_input = input()
    inputed_list = getting_input(main_input)
    looper = int(inputed_list[0])
    step = int(inputed_list[1])
    sequence = Link()
    buildlink(looper, sequence)
    skipper(step, sequence)
    print_joseph()


def getting_input(main_input):
    looper = ''
    for element in range(0, len(main_input)):
        if main_input[element] == ' ':
            step = main_input[element + 1: len(main_input)] 
            return [looper, step]
        else: 
            looper += main_input[element]


def buildlink(looper, sequence):
    for element in range (1, looper + 1): 
        sequence.addnode(element)

def skipper(step, sequence, count = 0): #don't use recursion 
    while sequence.length > 0: 
        count += 1
        if count == step: 
            joseph.append(sequence.cursor.label) 
            sequence.removenode()
            count = 0
        else:
            sequence.cursor = sequence.cursor.rest 

def print_joseph(): 
    element = 0 
    print_dis = "<"
    for element in range(0, len(joseph)):
        if element == len(joseph) - 1:
            print_dis += str(joseph[element])
        else:
            add = str(joseph[element]) + ", "
            print_dis += add

    print_dis += ">"
    print(print_dis)
        
main()
