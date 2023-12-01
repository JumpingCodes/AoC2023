import string
f = open("/home/mj/Documents/GitHub/AoC2023/day01/in.txt", "r").readlines()
r = 0
letnu = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
for l in f:
    for le, nu in letnu.items():
        l = l.replace(le, le + nu+ nu)
    s = ''.join(n for n in l if n not in string.ascii_letters)
    r += int(s[0] + s[len(s)-2])
print(r)
