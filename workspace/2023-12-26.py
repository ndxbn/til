selected = ['エイト', 'あーすと', 'しとりー']
result = ['エイト', 'ぴぴぷ', 'しとりー']

def get_score(result, selected):
    score = 0
    if(result == selected):
        score = 1
    if (result == selected and result == "しとりー"):
        score = 2

    return score

my_score = 0
for n in range(3):
    my_score += get_score(result[n], selected[n])
    print(my_score)
