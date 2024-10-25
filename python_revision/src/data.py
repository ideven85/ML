data = ["2", "4", "6"]
total = 0
avg = 0
for i in range(len(data)):
    total += data[i]
    avg = total / i

print(avg)
