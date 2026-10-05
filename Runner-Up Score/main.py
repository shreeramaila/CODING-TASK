scores = [10, 20, 30, 40, 50]

highest = scores[0]
second = scores[0]

for score in scores:
    if score > highest:
        second = highest
        highest = score
    elif score > second and score != highest:
        second = score

print(second)