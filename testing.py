size = 4
array = []
count = 0
while True:
    count = 0
    arrays = []
    while count < size:
        arrays.append(0)
        count += 1
    array.append(arrays)
    if len(array) == size:
        break

