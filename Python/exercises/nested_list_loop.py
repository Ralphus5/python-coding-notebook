practice_list = [[10,40,20,50],[2,42,10],[101,10,4]]
for element in practice_list:
    for number in element:
        if number < 50 and number > 10:
            print(number)
        if number > 100:
            break