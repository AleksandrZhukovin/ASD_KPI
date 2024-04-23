from Lab3 import *


class Queue(List):
    def __init__(self, size: int) -> None:
        super().__init__()
        self.__size = size

    def add(self, data) -> None:
        if self.len < self.__size:
            super().add(data)
        else:
            raise OverflowError('The queue if full!')

    def pop(self) -> None:
        if self.len:
            res = self.head
            self.head = self.head.next
        else:
            raise ValueError('The queue is empty')
        self.len -= 1
        return res


if __name__ == '__main__':
    queue = []
    size = 0
    head = 0
    tail = 0


    def add(data):
        global queue, size, tail, head
        if len(queue) < size:
            queue.insert(0, data)
            tail = 0
            head = len(queue) - 1


    def pop():
        global queue, size, tail, head
        if len(queue):
            return queue.pop(0)


    a = Queue(10)

    for i in range(1):
        a.add(i)

    for i in a:
        print(i)

    a.pop()
    a.pop()

    for i in a:
        print(i)
