#https://www.codewars.com/kata/55807f415ff687ecac00005f

def pivot(report , index):
    keys = sorted(list(set([r[index] for r in report])))
    ans = []
    for key in keys:
        item = []
        for i in range(len(report[0])):
            if i == index:
                item.append(key)
                continue
            try:
                value = sum(float(r[i]) for r in report if r[index] == key)
                item.append(value)
            except:
                item.append('-')
        ans.append(item)
    return ans