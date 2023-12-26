#おためしrange
select_1st = 'エイト'
select_2nd = 'あーすと'
select_3rd = 'しとりー'

top_1st = 'エイト'
top_2nd = 'ぴぴぷ'
top_3rd = 'しとりー'

x = [select_1st,select_2nd,select_3rd,'スイカselect','泥試合select','エキシビジョンselect'] #順位予想
y = [top_1st,top_2nd,top_3rd,'スイカtop','泥試合top','エキシビジョンtop'] #順位結果

def compare(n):
    if (x[n] == y[n]):
        a = 1
    else:
        a = 0
    print(a)

for n in range(3):
    compare(n)
