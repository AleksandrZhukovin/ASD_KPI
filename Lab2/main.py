import random
import timeit


def selection(arr):
    n = len(arr)
    c = 0
    m = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            c += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            m += 1
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, c, m


test_100 = [random.randint(0, 100) for _ in range(100)]
test_1000 = [random.randint(0, 1000) for _ in range(1000)]
test_10000 = [random.randint(0, 10000) for _ in range(10000)]

c_100 = 100 * 99 / 2
m_100 = 99 / 2
c_1000 = 1000 * 999 / 2
m_1000 = 999 / 2
c_10000 = 10000 * 9999 / 2
m_10000 = 9999 / 2

print('Unsorted 100 elements array', test_100)
print('Unsorted 1000 elements array', test_1000)
print('Unsorted 10000 elements array', test_10000)

start = timeit.default_timer()
res = selection(test_100)
time_100 = timeit.default_timer() - start

start = timeit.default_timer()
res_1 = selection(test_1000)
time_1000 = timeit.default_timer() - start

start = timeit.default_timer()
res_2 = selection(test_10000)
time_10000 = timeit.default_timer() - start

print(f'Expected compares: {c_100}. Expected moves: {m_100}')
print(f'Sorted: {res[0]}\nCompares: {res[1]}\nMoves: {res[2]}\nTime: {time_100}\n')

print(f'Expected compares: {c_1000}. Expected moves: {m_1000}')
print(f'Sorted: {res_1[0]}\nCompares: {res_1[1]}\nMoves: {res_1[2]}\nTime: {time_1000}\n')

print(f'Expected compares: {c_10000}. Expected moves: {m_10000}')
print(f'Sorted: {res_2[0]}\nCompares: {res_2[1]}\nMoves: {res_2[2]}\nTime: {time_10000}\n')


def shell_sort(arr):
    compares = 0
    m = 0
    s = 0
    steps = []
    i = 1
    while s <= len(arr) // 2:
        s = int(9 * 2 ** i - 9 * 2 ** (i / 2) + 1) if i % 2 == 0 else int(8 * 2 ** i - 6 * 2 ** ((i + 1) / 2) + 1)
        if s <= len(arr) // 2:
            steps.append(s)
        i += 1
    steps.reverse()
    steps.append(1)
    print(steps)
    i = 0
    el = 0
    for step in steps:
        while el < len(arr):
            compares += 1
            el = 0 + i
            start = el
            for c in range(len(arr[::step])):
                move = el
                while arr[el] < arr[move - step]:
                    compares += 1
                    if move - step <= start:
                        move = start
                        break
                    move -= step
                if move != el:
                    m += 1
                    arr.insert(move, arr.pop(el))
                el += step
            i += 1
        el = 0
        i = 0
    return compares, m


test_100 = [random.randint(0, 100) for _ in range(100)]
test_1000 = [random.randint(0, 1000) for _ in range(1000)]
test_10000 = [random.randint(0, 10000) for _ in range(10000)]


c_100 = 100 ** (7/6)
m_100 = 100 ** (7/6)


c_1000 = 1000 ** (7/6)
m_1000 = 1000 ** (7/6)


c_10000 = 10000 ** (7/6)
m_10000 = 10000 ** (7/6)

print('Unsorted 100 elements array', test_100)
print('Unsorted 1000 elements array', test_1000)
print('Unsorted 10000 elements array', test_10000)

start = timeit.default_timer()
res = shell_sort(test_100)
time_100 = timeit.default_timer() - start

start = timeit.default_timer()
res_1 = shell_sort(test_1000)
time_1000 = timeit.default_timer() - start

start = timeit.default_timer()
res_2 = shell_sort(test_10000)
time_10000 = timeit.default_timer() - start

print(f'C_exp/C_theor: {c_100 / res[0]}. M_exp/M_theor: {m_100 / res[1]}')
print(f'C_theor: {c_100}. M_theor: {m_100}')
print(f'Sorted: {test_100}\nCompares: {res[0]}\nMoves: {res[1]}\nTime: {time_100}\n')

print(f'C_exp/C_theor: {c_1000 / res_1[0]}. M_exp/M_theor: {m_1000 / res_1[1]}')
print(f'C_theor: {c_1000}. M_theor: {m_1000}')
print(f'Sorted: {test_1000}\nCompares: {res_1[0]}\nMoves: {res_1[1]}\nTime: {time_1000}\n')

print(f'C_exp/C_theor: {c_10000 / res_2[0]}. M_exp/M_theor: {m_10000 / res_2[1]}')
print(f'C_theor: {c_10000}. M_theor: {m_10000}')
print(f'Sorted: {test_10000}\nCompares: {res_2[0]}\nMoves: {res_2[1]}\nTime: {time_10000}\n')


# def insert_sort(arr):
#     n = 0
#     c = 0
#     m = 0
#     while n != len(arr):
#         move = n
#         while arr[n] < arr[move - 1]:
#             c += 1
#             if move - 1 == -1:
#                 move = 0
#                 break
#             move -= 1
#         if move != n:
#             m += 1
#             arr.insert(move, arr.pop(n))
#         n += 1
#     return arr, c, m
# def shell(arr):
#     m = 0
#     c = 0
#     s = 0
#     steps = []
#     i = 1
#     while s <= len(arr) // 2:
#         s = int(9*2**i - 9*2**(i/2) + 1) if i % 2 == 0 else int(8*2**i - 6*2**((i+1)/2) + 1)
#         steps.append(s)
#         i += 1
#     steps.reverse()
#     for step in steps:
#         start = -1
#         sl = arr[::step]
#         while len(sl) == len(arr[start+1::step]):
#             sl = arr[start+1::step]
#             res = insert_sort(sl)
#             m += res[2]
#             c += res[1]
#             for i in range(len(sl)):
#                 arr[(i-1)+step if i > 0 else 0] = sl[i]
#             start += 1
#     final_res = insert_sort(arr)
#     m += final_res[2]
#     c += final_res[1]
#     return final_res[0], c, m
