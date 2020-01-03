class Node:

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def set_value(self, value):
        self.value = value

    def set_next(self, node):
        self.next = node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

class LinkedList:

    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        temp_node = Node(value)
        temp_node.set_next(self.head)
        self.head = temp_node
        del temp_node

    def add_to_tail(self, value):
        on = self.head
        temp_node = Node(value)
        while on.get_next():
            on = on.get_next()
        on.set_next(temp_node)
        del temp_node
        return True

    def status(self):
        on = self.head
        if on is None:
            print("The List is Empty!")
            return False

        while on:
            print(str(on.get_value()), end=" ")
            on = on.next
            if on:
                print("-->", end=" ")

        print()

    def length(self):
        on = self.head
        cont = 0

        while on:
            cont += 1
            on = on.get_next()
        
        return cont
    
    def remove(self, item):
        on = self.head
        prev = None
        found = False

        while not found:
            if on.get_value() == item:
                found = True
            else:
                prev = on
                on = on.get_next()

        if prev is None:
            self.head = on.get_next()
        else:
            prev.set_next(on.get_next())

        return found

    def max(self):
        on = self.head
        bigger = on.get_value()

        while on:
            if bigger < on.get_value():
                bigger = on.get_value()
            on = on.get_next()
        
        return bigger
    
    def min(self):
        on = self.head
        smaller = on.get_value()

        while on:
            if smaller > on.get_value():
                smaller = on.get_value()
            on = on.get_next()
        
        return smaller

    def pop(self):
        on = self.head
        prev = None

        while on.get_next():
            prev = on
            on = on.get_next()

        if prev is None:
            self.head = None
        else:
            prev.set_next(None)
            value = on.get_value()
            del on
            
            return value

    def node_at_index(self, pos):
        on = self.head
        pos = int(pos)
        aux_pos = 1

        while aux_pos != pos:
            on = on.get_next()
            aux_pos += 1

        value = on.get_value()
        return value

    def copy(self):
        temp = LinkedList()
        on = self.head

        temp.add_to_head(on.get_value())
        on = on.get_next()

        while on:
            temp.add_to_tail(on.get_value())
            on = on.get_next()

        return temp

    def clear(self):
        self.head = None
        return True
    
    def to_string(self, separator=""):
        on = self.head
        final_string = ""

        while on:
            temp_string = on.get_value()
            final_string += str(temp_string)
            on = on.get_next()

            if on:
                final_string += separator
        
        return final_string

    def count(self, element):
        on = head.self
        count = 0

        while on:
            if on.get_value() == element:
                count += 1
            
            on = on.get_next()

        return count

    def to_list(self):
        on = self.head
        temp_list = []

        while on:
            temp_element = on.get_value()
            temp_list.append(temp_element)
            on = on.get_next()
        
        return temp_list

    def to_set(self):
        on = self.head
        temp_set = set()

        while on:
            temp_element = on.get_value()
            if temp_element not in temp_set:
                temp_set.add(temp_element)
            on = on.get_next()

        return temp_set

    def reverse(self):
        on = self.head
        temp_node = None
        prev = None

        while on:
            temp_node = on.get_next()
            on.set_next(prev)
            prev = on
            on = temp_node

        self.head = prev
        return True

    def sort(self):
        on = self.head
        aux_node = on

        while aux_node:
            temp_node = aux_node
            temp_node2 = aux_node

            smaller = aux_node.get_value()

            while temp_node:
                if smaller > temp_node.get_value():
                    smaller = temp_node.get_value()
                    temp_node2 = temp_node
                temp_node = temp_node.get_next()

            temp = aux_node.get_value()
            aux_node.set_value(temp_node2.get_value())
            temp_node2.set_value(temp)

            aux_node = aux_node.get_next()


# Tests

my_list = LinkedList()

my_list.add_to_head(5)
my_list.add_to_head(4)
my_list.add_to_head(3)
my_list.add_to_head(2)
my_list.add_to_head(1)

my_list.status()

my_list.add_to_tail(10)
my_list.add_to_tail(20)
my_list.add_to_tail(13)

my_list.status()

print(my_list.length())

print(my_list.node_at_index(3))

print(my_list.remove(10))

my_list.status()

print(my_list.max())

print(my_list.min())

my_list.pop()

my_list.status()

my_list.reverse()

my_list.status()

my_list.sort()

my_list.status()





