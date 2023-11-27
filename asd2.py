class ArrayList:
    def __init__(self):
        self.__capacity = 2
        self.__length = 0
        self.__arr = [0] * self.__capacity

    def add(self, value):
        if self.__length == self.__capacity:
            self.__expand()
        self.__arr[self.__length] = value
        self.__length += 1

    def swap(self, index1, index2):
        self.__arr[index1], self.__arr[index2] = self.__arr[index2], self.__arr[index1]

    def remove(self, index):
        if index < self.__length:
            for i in range(index + 1, self.__length + 1):
                self.__arr[i - 1] = self.__arr[i]
        self.__length -= 1

    def get(self, index):
        return self.__arr[index]

    def get_length(self):
        return self.__length

    def __expand(self):
        self.__capacity *= 2
        new_arr = [0] * self.__capacity
        for i in range(self.__length):
            new_arr[i] = self.__arr[i]
        self.__arr = new_arr


def get_min_run(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return r + n


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr.get(j) < arr.get(j - 1):
            arr.swap(j, j - 1)
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


def tim_sort(arr):
    n = arr.get_length()
    min_run = get_min_run(n)
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2


array = ArrayList()
array.add(1)
array.add(-1)
array.add(0)
array.add(123)
array.add(-331)
array.add(234)
array.add(0)
array.add(-1)

tim_sort(array)
for i in range(array.get_length()):
    print(array.get(i), end=" ")
