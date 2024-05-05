def f(src, i, tgt, j):
    while i < len(src) and j < len(tgt):
        if src[i] == tgt[j]:
            j += 1
        i += 1
    return j

def q2(source, target):
    num = 0
    k = 0
    while k < len(target):
        nex = f(source, 0, target, k)
        if nex == k:
            return -1
        k = nex
        num += 1
    return num
    