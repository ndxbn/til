selected = ['エイト', 'あーすと', 'しとりー']
result = ['エイト', 'ぴぴぷ', 'しとりー']

def get_score(result, selected):
    score = 0
    if(result == selected):
        score = 1
    if (result == selected and result == "しとりー"):
        score = 2

    return score

selectedList = []
resultList = []
counter = 1
while True:
    select = input(str(counter) + "にんめ: ")
    if(select == ""): break

    selectedList.append(select)
    counter += 1

print(selectedList)
