'''
Т16.1 Побудувати ітератор, який проходить всі елементи діапазону від 1 до n,
повертаючи тільки
а) парні числа
'''
class Even:
    def __init__(self, n):
        self._max = n
    def __iter__(self):
        self._current = 0
        return self
    def __next__(self):
        self._current += 2
        if self._current > self._max:
            raise StopIteration
        return self._current
# array declaration
array = Even(17)
# 1 approach
y = iter(array)
try:
    while True:
        x = next(y)
        print(x)
except StopIteration:
    pass
# 2 approach
for x in array:
    print(x)
