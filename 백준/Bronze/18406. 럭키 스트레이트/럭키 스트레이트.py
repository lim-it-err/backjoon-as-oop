data = [*input()]
data = [int(data[i]) for i in range(len(data))]
if sum(data[:len(data)//2]) == sum(data[len(data)//2:]):
    print("LUCKY")
else:
    print("READY")