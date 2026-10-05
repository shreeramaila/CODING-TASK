numbers = (10, 20, 30)

try:
    numbers[1] = 50
except TypeError:
    print("Tuple cannot be changed")