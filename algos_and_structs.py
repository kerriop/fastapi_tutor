# Массив (список) это набор значений одного типа, сохранённых под тем же именем
def my_array():
    cars = ["Toyota", "Tesla", "Hyundai"]
    print(len(cars))
    cars.append("Honda")
    print(cars)
    print(cars.pop(0))
    print(cars)
    # for x in cars:
    #     print(x)


# Очередь это линейная структура данных,
# в которой данные хранятся в порядке 'первым пришёл — первым ушёл» (FIFO).
def my_queue():
    from collections import deque
    # Initializing a queue
    q = deque()
    # Adding elements to a queue
    q.append('a')
    q.append('b')
    q.append('c')
    print('Initial queue')
    print(q)
    # Removing elements from a queue
    print('\nElements dequeued from the queue')
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    print('\nQueue after removing elements')
    print(q)
    # Uncommenting q.popleft()
    # will raise an IndexError
    # as queue is now empty


# Стек - 'пос'едний пришёл — первым ушёл» (LIFO)
def my_stack():
    stack = []
    # append() function to push
    # element in the stack
    stack.append('a')
    stack.append('b')
    stack.append('c')
    print('Initial stack')
    print(stack)
    # pop() function to pop
    # element from stack in
    # LIFO order
    print('\nElements popped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print('\nStack after elements are popped: ')
    print(stack)
    # uncommenting print(stack.pop())
    # will cause an IndexError
    # as the stack is now empty


# Связанный списокэто последовательный набор данных,
# который использует реляционные указатели на каждом узле данных для связи со следующим
# узлом в списке. Первый узел в связанном списке называется головным узлом,
# а последний — хвостовым узлом, который имеет null указатель.
def my_linked_list():
    class Node:
        def __init__(self, dataval=None):
            self.dataval = dataval
            self.nextval = None

    class SLinkedList:
        def __init__(self):
            self.headval = None

    list1 = SLinkedList()
    list1.headval = Node('Mon')
    e2 = Node('Tue')
    e3 = Node('Wed')
    # Link first Node to second node
    list1.headval.nextval = e2
    # Link second Node to third node
    e2.nextval = e3


# Дерево Как и связанный список, они заполняются Node объектами, которые содержат значение данных
# и один или несколько указателей для определения его отношения к непосредственным узлам.
#  У двоичных деревьев не может быть узлов с более чем двумя дочерними узлами.

def my_tree():
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

        def insert(self, data):
            # Compare the new value with the parent node
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data

        # Print the tree
        def PrintTree(self):
            if self.left:
                self.left.PrintTree()
            print(self.data)
            if self.right:
                self.right.PrintTree()

    # Use the insert method to add nodes
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.PrintTree()


# Граф это структура данных, используемая для визуального представления взаимосвязей между
# вершинами данных (узлами графа). Связи, соединяющие вершины вместе, называются рёбрами
def my_graph():
    # Create the dictionary with graph elements
    graph = {'a': ['b', 'c'],
             'b': ['a', 'd'],
             'c': ['a', 'd'],
             'd': ['e'],
             'e': ['d']
             }
    # Print the graph
    print(graph)


if __name__ == '__main__':
    pass
    # my_array()
    # my_queue()
    # my_stack()
    # my_linked_list()
    # my_tree()
    # my_graph()
