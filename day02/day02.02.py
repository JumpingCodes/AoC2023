import string
file = open("/home/mj/Documents/GitHub/AoC2023/day02/in.txt", "r").readlines()
res = 0
for line in file:
    myBag = {'red': 0, 'green': 0, 'blue': 0}
    for game in line.split(':')[1].split(';'):
        for move in game.split(','):
            myBag[move.replace('\n', '').strip().split(' ')[1]] = max(int(move.replace('\n', '').strip().split(' ')[0]), myBag[move.replace('\n', '').strip().split(' ')[1]])
    sum += (myBag['blue']* myBag['green'] * myBag['red'])
print(sum)