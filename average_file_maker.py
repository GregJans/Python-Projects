
with open('average.txt', 'r+') as file:
    temps = list(file.readlines())
    temps = temps[:-4]


total = 0
for i in temps:
    total += int(i)


avg = total / len(temps)

with open('average.txt', 'r+') as file:
    t = list(file.readlines())
    t[-1] = 'The average is: ' + str(avg)

    file.seek(0)

    for i in t:
        file.write(i)
