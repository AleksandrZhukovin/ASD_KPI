import timeit


__all__ = ('Element', 'List', )


"""Клас елементу"""
class Element:
    def __init__(self, data, key: int, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        self.key = key

    def __str__(self):
        return f'Element #{self.key}. Data: {self.data}'


"""Клас списку"""
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        self.next_key = 0

    def search(self, key: int, element: Element, if_not_found=-1):
        if not element.next:
            return if_not_found
        elif element.key == key:
            return element
        return self.search(key, element.next)

    """Метод додавання в кінець списку"""
    def add(self, data):
        if not self.head:
            self.head = Element(data, 0)
            self.tail = self.head
        else:
            new_element = Element(data, self.next_key)
            self.tail.next, new_element.prev, self.tail = new_element, self.tail, new_element
        self.len += 1
        self.next_key += 1

    def remove(self, index: int):
        if index >= self.len:
            raise IndexError('Invalid index')
        elif index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            self.tail = self.tail.prev
        else:
            element = self.search(index, self.head)
            element.prev.next, element.next.prev = element.next, element.prev
            del element
        self.len -= 1

    """Метод додавання на вказану позицію"""
    def insert(self, key: int, data, place='a'):
        element = -1
        if self.len > 0:
            element = self.search(key, self.head)
        if element == -1:
            raise IndexError('The element does not exist')
        if place == 'a':
            new = Element(data, self.next_key)
            element.next, element.next.prev, new.next, new.prev = new, new, element.next, element
            if element == self.tail:
                self.tail = new
            self.len += 1
            self.next_key += 1
        elif place == 'b':
            new = Element(data, self.next_key)
            element.prev, element.prev.next, new.next, new.prev = new, new, element, element.prev
            if element == self.head:
                self.head = new
            self.len += 1
            self.next_key += 1
        else:
            raise ValueError('Incorrect place identifier')

    """Метод розбиття тексту по словам"""
    def split(self, text: str):
        word = ''
        for char in text:
            if char == '.':
                self.add(word)
                break
            if char != ' ':
                word += char
            else:
                self.add(word)
                word = ''

    """Ітератор"""
    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        res = self.current
        self.current = self.current.next
        return res

if __name__ == '__main__':
    l = List()

    t = input('Enter text: ')

    if t[-1] != '.':
        raise ValueError('"." symbol is required!')

    start = timeit.default_timer()
    l.split(t)

    l.tail.prev.data = l.tail.data

    for i in l:
        print(i)

    for i in l:
        if not len(i.data) % 2:
            print((i.data + i.data[-1]).replace('o', ''))
    end_list = timeit.default_timer() - start


    start = timeit.default_timer()
    words = []

    word = ''
    for char in t:
        if char == '.':
            words.append(word)
            break
        if char != ' ':
            word += char
        else:
            words.append(word)
            word = ''

    for word in words:
        if not len(word) % 2:
            print((word + word[-1]).replace('o', ''))
    end_array = timeit.default_timer() - start

    print(end_list, end_array)
