from Lab3 import *

import queue as qu


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
    size = 10
    len_ = 0
    head = 0
    tail = 0
    queue = ['*' for _ in range(size)]


    def add(data):
        global queue, size, tail, head, len_
        if len_ < size:
            if tail >= len_:
                queue[tail % size] = data
                tail += 1
                len_ += 1
            else:
                queue[tail] = data
                tail += 1
                len_ += 1


    def pop():
        global queue, size, tail, head, len_
        if len(queue):
            el = queue[head]
            queue[head] = '*'
            head += 1
            len_ -= 1
            return el

    for i in range(10):
        add(i)

    print(queue)

    pop()
    pop()
    pop()
    print(queue)
    add(11)
    add(12)
    print(queue)



    # a = Queue(10)
    #
    # for i in range(1):
    #     a.add(i)
    #
    # for i in a:
    #     print(i)
    #
    # a.pop()
    # a.pop()
    #
    # for i in a:
    #     print(i)

    q = qu.Queue(5)

    for i in range(5):
        q.put(i)

    print('size', q.qsize())

    for i in range(q.qsize()):
        print(q.get())

    q.empty()

    for i in range(q.qsize()):
        print(q.get())
