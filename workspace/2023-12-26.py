def get_score(result, selected):
    score = 0
    if(result == selected):
        score = 1
    if (result == selected and result == "しとりー"):
        score = 2

    return score

selectedList = []
counter = 1
while True:
    select = input(str(counter) + "にんめ: ")
    if(select == ""): break

    selectedList.append(select)
    counter += 1

resultList = []
counter = 1
while True:
    result = input(str(counter) + "にんめ: ")
    if(result == ""): break

    resultList.append(result)
    counter += 1

my_score = 0
for n in range(len(resultList)):
    my_score += get_score(resultList[n], selectedList[n])
    print(my_score)