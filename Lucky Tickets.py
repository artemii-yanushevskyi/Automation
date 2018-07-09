string = input("n suma: ")
# convert input to integers
n, suma = map(int, string.split(" "))

def num_sum(number, n):
    """ 4256 -> 17
    """
    num_sum = 0
    for i in range(n, 0, -1):
        rest = number % 10
        num_sum += rest
        number = (number - rest) // 10
    return num_sum

def num_to_str(number, n):
    """ 2309 -> "002309"
    """
    number = str(number)
    zeros = "0" * (n - len(number))
    return zeros + number
    
suma_part = suma / 2 # suma must be even

parts = []

for i in range(10**n):
    if suma_part == num_sum(i, n):
        # select the parts that have suma_part sum of its digits
        parts.append(num_to_str(i, n)) 

# number of lucky tickets
print(len(parts)**2)

# output lucky numbers
for p1 in parts:
    for p2 in parts:
        # combine the parts in all possible ways
        print(p1+p2)    
