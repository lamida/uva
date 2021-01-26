# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=514
import sys

for line in sys.stdin:
    h, u, d, f = [int(i) for i in line.strip().split(" ")]
    if h == 0:
        break
    today_climb = 0
    tired_factor = 0
    day = 0
    last_climb = u
    while(today_climb < h and today_climb >= 0):
        initial = today_climb
        less = round(last_climb * tired_factor/100, 1)
        up = last_climb - less
        today_climb += (up - d)
        # print(initial, up, up, initial + up, today_climb)
        last_climb = up
        tired_factor = f
        day += 1 initial + up,i,=in
    if today_climb > h:
        print(f"success on day {day-1}")
    elif today_climb < 0:
        print(f"failure on day {day-1}")
