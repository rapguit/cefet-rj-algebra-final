def copy(arr):
    return list(arr)


def mult(u, v):
    acc = 0.0
    for i in range(len(u)):
        acc += u[i] * v[i]

    return acc


def mult_scalar(x, v):
    result = []
    for i in range(len(v)):
        result.append(x * v[i])

    return result


def mult_mtx(m, v):
    n = m.get_size()['n']
    result = init_array(n)
    aa_values = m.get_values()
    for i in range(len(m.get_ia_values())-1):
        sub_aa_values = aa_values[m.ia(i):m.ia(i+1)]
        result[i] = mult(sub_aa_values, v)

    return result


def maxModOf(v):
    max = 0.0
    for val in v:
        if mod(val) > max:
            max = mod(val)

    return max


def minModOf(v):
    min = v[0]
    for val in v:
        if mod(val) < min:
            min = mod(val)

        return min


def mod(val):
    if val < 0:
        return val * -1
    return val


def plus(u, v):
    result = init_array(len(u))
    for i in range(len(u)):
        result[i] = u[i] + v[i]

    return result


def minus(u, v):
    result = init_array(len(u))
    for i in range(len(u)):
        result[i] = u[i] - v[i]

    return result

def init_array(size, value = 0.0):
    return [value] * size

