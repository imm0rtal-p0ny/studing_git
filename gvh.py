def permutations(s):
    result = []
    result.append(s)
    s_lst = list(s)
    a = len(s_lst)
    for i in range(len(s_lst) - 1):
        for j in range(a):
            s = ''
            s_lst.append(s_lst.pop(i))
            for k in s_lst:
                s += k
            if s not in result:
                result.append(s)
        a += 1
    return result


print(permutations('aabb'))
