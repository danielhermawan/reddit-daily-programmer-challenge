def number_needed(a, b):
    mapa = {}
    mapb = {}
    sorted(a)
    sorted(b)
    if len(a) > len(b):
        num = len(a)
    else:
        num = len(b)
    for i in range(num):
        if i < len(a):
            mapa[a[i]] = mapa.get(a[i], 0) + 1
        if i < len(b):
            mapb[b[i]] = mapb.get(b[i], 0) + 1
    res = 0
    for key in mapa.keys():
        res += abs(mapa.get(key, 0) - mapb.get(key, 0))
        mapa[key] = 0
        mapb[key] = 0
    for key in mapb.keys():
        res += abs(mapa.get(key, 0) - mapb.get(key, 0))
        mapa[key] = 0
        mapb[key] = 0
    return res


def ransom_note(magazine, ransom):
    map = {}
    s = ""
    i = 0
    while i < len(magazine):
        if magazine[i] != " ":
            s += magazine[i]
        else:
            map[s] = map.get(s, 0) + 1
            s = ""
        i += 1
    if s != "":
        map[s] = map.get(s, 0) + 1
        s = ""
    i = 0
    while i < len(ransom):
        if ransom[i] != " ":
            s += ransom[i]
        else:
            if map.get(s, 0) == 0:
                return False
            else:
                map[s] -= 1
                s = ""
        i += 1
    return True


print(ransom_note("two times three is not four", "two times two is four"))
