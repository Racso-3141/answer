def q2(s):
    stk = []
    res = [' ' for _ in range(len(s))]
    for i, c in enumerate(s):
        if c == '(':
            stk.append(i)
        elif c == ')':
            if len(stk) > 0 and s[stk[-1]] == '(':
                stk.pop()
            else:
                res[i] = '?'
    for left_idx in stk:
        res[left_idx] = 'x'
    return ''.join(res)