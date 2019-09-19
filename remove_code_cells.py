# Читаем файл посимвольно, если встречаем '<div class="input"', запоминаем позицию первого элемента и ставим счетчик 1.
# С каждым следующим входжением '<div' увеличиваем счетчик на 1, с '</div' -- уменьшаем.
# Когда счетчик обнуляется, запоминаем позицию и удаляем все, что между первой и второй позициями /ставим комментарии.

# !!! del s[i:j:k]

print('Type something, than press ENTER:')
from_ , to_ = input().split()

inf = open(from_, 'r')
s = inf.read()
inf.close()

#s = list(input())

class_str = 'input'
init_str = '<div class="' + class_str + '"'
plus_str = '<div'
minus_str = '</div>'

n = len(s) - max(len(init_str), len(plus_str), len(minus_str))
i = 0

init_pos = []
del_pos = []
stkc = -1
for i in range(n):
    if s[i:i+len(init_str)] == init_str:
        init_pos.append(i)
        stkc = 0

    if s[i:i+len(plus_str)] == plus_str:
        stkc += 1

    if s[i:i+len(minus_str)] == minus_str:
        stkc -= 1
        if stkc == 0:
            if len(init_pos) == 0:
                continue
            if len(del_pos) < len(init_pos):
                del_pos.append(i+len(minus_str)) 
            

init_pos.reverse()
del_pos.reverse()

for i in range(len(init_pos)):
    print('Deleting text from position', init_pos[i], 'to position', del_pos[i])

for i in range(len(init_pos)):
    s = s[:init_pos[i]-1] + s[del_pos[i]:]
            
outf = open(to_, 'w')
outf.write(s)
outf.close()


    
