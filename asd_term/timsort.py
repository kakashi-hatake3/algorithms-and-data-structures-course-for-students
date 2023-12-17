from arrayList import ArrayList


def get_min_run(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return r + n


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left = ArrayList()
    right = ArrayList()
    for i in range(0, len1):
        left.add(arr.get(l + i))
    for i in range(0, len2):
        right.add(arr.get(m + 1 + i))
    i, j, k = 0, 0, l
    while i < len1 or j < len2:
        if left.get(i) <= right.get(j):
            arr[k] = left.get(i)
            i += 1
        else:
            arr[k] = right.get(j)
            j += 1
        k += 1


def tim_sort(array):
    dynamic_array = ArrayList()
    for item in array:
        dynamic_array.add(item)
    n = dynamic_array.get_length()
    min_run = get_min_run(n)
    for i in range(0, n, min_run):
        insertion_sort(dynamic_array.data, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size
            merge(dynamic_array, dynamic_array.get(start), dynamic_array.get(mid), dynamic_array.get(size - 1))
        size *= 2
    return dynamic_array.data
