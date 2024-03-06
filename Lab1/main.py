#  Жуковін Олександр ФІ-21 Лаба 1 Варіант 5


# 6. Рекурсивно обчислити суму цифр заданого натурального числа.
def digit_sum(num, ind=0):
    if ind == len(str(num)):
        return 0
    return int(str(num)[ind]) + digit_sum(num, ind+1)


print(digit_sum(25123))
print(digit_sum(123))
print(digit_sum(298))


# 14. Реалізувати алгоритм для розв’язання задачі «Ханойські вежі».
def hanoi_tower(n, count=0, moves=0, **kwargs):
    kwargs['b'].append(kwargs['a'].pop(-1))
    print(kwargs, moves)
    moves += 1
    kwargs['c'].append(kwargs['a'].pop(-1))
    print(kwargs, moves)
    moves += 1
    kwargs['c'].append(kwargs['b'].pop(-1))
    print(kwargs, moves)
    moves += 1
    if len(kwargs['c']) == n:
        return kwargs
    if count == 0 or count == 3 or count == 6 or count == 9:
        kwargs['b'].append(kwargs['a'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['b'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['a'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['a'].append(kwargs['b'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['c'].append(kwargs['b'].pop(-1))
        print(kwargs, moves)
        moves += 1
        return hanoi_tower(n, count+1, moves, **kwargs)
    elif count == 1 or count == 4 or count == 10:
        kwargs['b'].append(kwargs['a'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['b'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['a'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['a'].append(kwargs['b'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['b'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        return hanoi_tower(n, count+1, moves, **kwargs)
    elif count == 2 or count == 8 or count == 11:
        kwargs['a'].append(kwargs['b'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['b'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['a'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['a'].append(kwargs['b'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['c'].append(kwargs['b'].pop(-1))
        print(kwargs, moves)
        moves += 1
        if count == 11:
            return hanoi_tower(n, 0, moves, **kwargs)
        else:
            return hanoi_tower(n, count+1, moves, **kwargs)
    elif count == 5 or count == 7:
        kwargs['a'].append(kwargs['b'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['b'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['a'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['a'].append(kwargs['b'].pop(-1))
        print(kwargs, moves)
        moves += 1
        kwargs['b'].append(kwargs['c'].pop(-1))
        print(kwargs, moves)
        moves += 1
        return hanoi_tower(n, count+1, moves, **kwargs)


# print(hanoi_tower(4, a=['4', '3', '2', '1'], b=[], c=[]))

def new_hanoi(n, **kwargs):
    if n == 1:
        return kwargs
    kwargs['c'].append(kwargs['a'].pop(0))
    new_hanoi(n-1, **kwargs)
    print(kwargs)


def anoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    anoi(n-1, source, auxiliary, target)
    print("Move disk", n, "from", source, "to", target)
    anoi(n-1, auxiliary, target, source)


# Example usage:
num_disks = 5
anoi(num_disks, 'A', 'C', 'B')

