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
        result[i] = x * v[i]

    return result


def mult_mtx(m, v):
    result = []
    for i in range(len(v)):
        result[i] = mult(m[i], v)

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
    result = []
    for i in range(len(v)):
        result[i] = u[i] + v[i]

    return result


def minus(u, v):
    result = []
    for i in range(len(v)):
        result[i] = u[i] - v[i]

    return result
