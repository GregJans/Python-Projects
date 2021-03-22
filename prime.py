
dividends = []
num = 1_000

while True:
    num += 1
    #print(f"Working on {num}")
    if (str(num)[-1] == "2" or str(num)[-1] == "5" or str(num)[-1] == "0"):
        continue

    else:
        for i in range(1, num + 1):
            if ((num % i) == 0):
                dividends.append(i)

        if (len(dividends) == 2):
            print(f"{num} is prime")
            

    dividends.clear()
