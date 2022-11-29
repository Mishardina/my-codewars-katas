#https://www.codewars.com/kata/56a1c63f3bc6827e13000006

def merge(ans, a, start, mid, end):
    f = [0] * (mid - start + 1)
    s = [0] * (end - mid)

    n = mid - start + 1
    m = end - mid

    for i in range(start, mid + 1):
        f[i - start] = a[i]
    for i in range ( mid + 1, end + 1):
        s[i - mid - 1] = a[i]

    i = 0
    j = 0
    k = start
    cnt = 0

    while (i < n and j < m):
        if (f[i][1] <= s[j][1]):
            ans[f[i][0]] += cnt
            a[k] = f[i]
            k += 1
            i += 1

        else:
            cnt += 1
            a[k] = s[j]
            k += 1
            j += 1

    while (i < n):
        ans[f[i][0]] += cnt
        a[k] = f[i];
        k += 1
        i += 1
    
    while (j < m):
        a[k] = s[j]
        k += 1
        j += 1
    
def mergesort(ans, item, low, high):
    
    if (low >= high):
        return
         
    mid = (low + high) // 2
    mergesort(ans, item, low, mid)
    mergesort(ans, item, mid + 1, high)
    merge(ans, item, low, mid, high)
    
    
def smaller(arr):
    n = len(arr)
    ans = [0] * n
    a = [[0 for x in range(2)]
            for y in range(n)]

    for i in range(n):
        a[i][1] = arr[i]
        a[i][0] = i
    
    mergesort(ans, a, 0, n - 1)
    return ans