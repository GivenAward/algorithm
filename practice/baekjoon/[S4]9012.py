import sys

N = int(sys.stdin.readline())
for _ in range(N):
    is_breaked = False
    ps = sys.stdin.readline().strip()
    ps_list = [1 if p == "(" else -1 for p in ps]
    result = 0
    for int_p in ps_list:
        result += int_p
        if result < 0:
            print("NO")
            is_breaked = True
            break
    if not is_breaked:
        if result != 0:
            print("NO")
        else:
            print("YES")
