game_field = []
gamers = ['♩', '♪', '♫']

for _ in range (4):
    game_field.append( ['o'] * 5)
"""
Вывод игрового поля
"""
def game_print():
    for row in game_field:
        for symbol in row:
            print("{:^2}".format(symbol), end = '')
        print()

points = [0]*3
"""
Подсчет очков
"""
def game_points(game_field):
    game_field = [['.'] * 5] + game_field + [['.'] * 5]
    for number in range (6):
        game_field[number] = ['.'] + game_field[number] + ['.']  
    for string in range(1, 5):
        for column in range(1, 6):
            count = 0
            for s_shift in range(-1, 2):
                for c_shift in range(-1, 2):
                    if s_shift != 0 and c_shift != 0 and game_field[string][column] == game_field[string + s_shift][column + c_shift]:
                        count += 1
            points[gamers.index(game_field[string][column])] += count
            game_field[string][column] = 'o'
    return points
            
"""
Ход игры + результат
"""
step=0
def game_go():
    global step
    name = gamers[step%3]
    if step <= 19:
        try:
            string, column = map(int, input(f'Введи свой ход (номер строки и столбца через пробел), игрок {name} ').split(' ')) 
            int(game_field[string-1][column-1], 30)
            game_field[string-1][column-1] = gamers[step%3] 
            step += 1
            game_print(); game_go()
        except:
            print('Некорректный ввод! Попробуйте снова.')
            game_go()
    else:
        game_points(game_field) 
        winners=[]
        for point in range (len(points)):
            if points[point] == min(points):
                winners.append(gamers[point]) 
        print('Победил(и) игрок(и)', *winners,'очки каждого игрока:', *points)
game_print()
game_go()
