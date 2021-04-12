def build_suff_arr(s):
    suff = []
    for i in range(len(s)-1, -1, -1):
        suff.append(s[i:])

    return(list(sorted(suff)))

def get_all_possible_p(p):
    count = 0
    res = []
    for i in range(len(p)):
        if p[i] == '?':
            count += 1

    for i in range(2**count):
        mask = list(map(int, str(bin(i))[2:].zfill(count)))
        s = []
        k = 0
        for j in range(len(p)):
            if p[j] == '?':
                if not mask[k]:
                    s.pop()
                k += 1
            else:
                s.append(p[j])

        res.append("".join(s))

    return res

def compare(s, p):
    i = 0
    j = 0
    while j != len(p):
        if i == len(s):
            return 1
        if s[i] != p[j]:
            if s[i] < p[j]:
                return 1
            else:
                return -1
        else:
            i += 1
            j += 1
    return 0


def find_p(suff_arr, p):
    count = 0
    idx = []
    l = 0
    r = len(suff_arr)-1
    i = l + (r - l) // 2
    while l <= r:
        count += 1
        if count > 10:
            break
        dir = compare(suff_arr[i], p)
        if dir < 0:
            r = i - 1
            i = l + (r - l) // 2
        elif dir > 0:
            l = i + 1
            i = l + (r - l) // 2
        else:
            idx.append(i)
            #check neighbors:
            i_new = i - 1
            while 0 <= i_new < len(suff_arr):
                dir = compare(suff_arr[i_new], p)
                if dir != 0:
                    break
                idx.append(i_new)
                i_new -= 1

            i_new = i + 1
            while 0 <= i_new < len(suff_arr):
                dir = compare(suff_arr[i_new], p)
                if dir != 0:
                    break
                idx.append(i_new)
                i_new += 1

            break

    return idx

if __name__ == "__main__":
    s = input("Введите строку: ")
    suff_arr = build_suff_arr(s)
    p = ""
    while(True):
        p = input("Введите паттерн или exit для выхода: ")
        if p == 'exit':
            break
        all_p = get_all_possible_p(p)
        idx = set()
        for p in all_p:
            new_idx = find_p(suff_arr, p)
            corrected_idx = [len(s) - len(suff_arr[i]) for i in new_idx]
            idx = idx.union(set(corrected_idx))
        if idx == set():
            print("Не удалось найти паттерн")
        else:
            print("Индексы вхождения паттерна в строку:", idx)
