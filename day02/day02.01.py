import string
file = open("/home/mj/Documents/GitHub/AoC2023/day02/in.txt", "r").readlines()
sum = 0
for line in file:
    works = True
    for game in line.split(':')[1].split(';'):
        myBag = {'red': 12, 'green': 13, 'blue': 14}
        for move in game.split(','):
            myBag[move.replace('\n', '').strip().split(' ')[1]] -= int(move.replace('\n', '').strip().split(' ')[0])
        if myBag['blue'] < 0 or myBag['green'] < 0 or myBag['red'] < 0:
            works = False
    if works:
        sum += int(''.join(c for c in line.split(':')[0].replace('\n', '').strip() if c not in string.ascii_letters))
print(sum)