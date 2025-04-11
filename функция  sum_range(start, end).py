def sum_range(start,end):
    list = []
    for i in range(start,end+1):
        list.append(i)
        result = sum(list)
    print(result)
sum_range(2,6)


