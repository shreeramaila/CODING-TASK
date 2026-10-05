number = 2
count = 0

while count < 10:
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number)
        count += 1

    number += 1